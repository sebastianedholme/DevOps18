$Users = Import-Csv -Path $Path -Encoding UTF8
$DC = "DC=gispark,DC=se"
$UserPassword = "Linux4Ever"
$MailDomain = "@gispark.se"
$TitleList = @{
    Användare = "sanvändare"
    Chef = "schefer"
    Ekonom = "sekonomer"
    Konsult = "skonsulter"
    Seniorkonsult = "sseniorkonsulter"
    Säljare = "ssäljare"
    Vaktis = "sadmins"
    Ledning = "sledning"
}

$Cities = $Users.City | Get-Unique

Write-Host "Importing sequence completed"

Write-Host "Creating user groups"
foreach ($City in $Cities) {
    foreach ($Group in $TitleList.Values) {
        $GroupName = "$City$Group"
        if(Get-ADGroup -Filter 'Name -eq $Group') {
            Write-Host "Group exists"
        } else {
            New-ADGroup `
                -Path "ou=grupper,ou=$City,$DC" `
                -Name $GroupName `
                -GroupScope Global
        }
    }
}

foreach ($User in $Users) {
    $GivenName = $User.GivenName
    $Surname = $User.Surname
    $DisplayName = $GivenName + " " + $Surname
    $StreetAddress = $User.StreetAddress
    $PostalCode = $User.PostalCode
    $City = $User.Phone
    $Title = $User.Title
    $EmpID = $User.EmpID
    $MobilePhone = $User.Phone
    $Email = $GivenName + "." + $Surname + $MailDomain

    $Loggon = $User.Loggon
    $UPN = $Loggon + $MailDomain
    $OUPath = "OU=Användare,OU=$City,$DC"

    if (Get-ADUser -Filter "SamAccountName -eq '$Loggon") {
        Write-Host "Loggin username already exists... Skipping $DisplayName, $Loggon"
    }
    else {
        New-ADUser `
        -Name $DisplayName `
        -DisplayName $DisplayName `
        -SamAccountName $Loggon `
        -GiveName $GivenName `
        -Surname $Surname `
        -Title $Title `
        -MobilePhone $MobilePhone `
        -EmailAddress $Email `
        -StreetAddress $StreetAddress `
        -PostalCode $PostalCode `
        -City $City `
        -EmployeeID $EmpID`
        -AccountPassword (ConvertTo-SecureString $UserPassword -AsPlainText -Force) `
        -Enabled $true `
        -Path $OUPath `
        -ChangePasswordAtLogon $false `
        -PasswordNeverExpires $true `
        -UserPrincipalName $UPN `
        -Server dc.gispark.se
    }

    Write-Host "Adding user to city group"
    $GroupName = $City + "sanvändare"
    Add-ADGroupMember -Identity $GroupName -Members $User

    Write-Host "Adding user after his/her title"
    $TitleGroupName = $City + $TitleList[$Title]
    Add-ADGroupMember -Identity $TitleGroupName -Members $User
}