$Users = Import-Csv -Path $Path -Encoding UTF8
$CityOUs = "Användare", "Datorer", "Grupper"
$DC = "DC=gispark,DC=se"

New-ADOrganizationalUnit -Name $Servers -Path $DC
New-ADOrganizationalUnit -Name $Resursgrupp -Path $DC

foreach ($User in $Users) {
    $City = $User.City
    if (Get-ADOrganizationalUNit -Filter "Name -eq $City") {
        Write-Host "OU for $City already exists"
    } else {
        Write-Host "Writing $City OUs"
        New-ADOrganizationalUnit -Name $City -Path $DC
        Write-Host "Writing OUs in $City"

        # To add more different OU add to the CityOUs list on the top
        foreach ($OU in $CityOUs){
            New-ADOrganizationalUnit -Name $OU -Path "OU=$City,$DC"
        }
    }
}