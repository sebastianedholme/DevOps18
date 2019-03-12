$users = Import-Csv -Path F:\import.csv -Encoding UTF8
$DC = "DC=jultomten,DC=nu"

foreach ($user in $users) {
		$title = $user.Tittel
		$loggon = $user.loggon
		$givenName = $user.givenName
		$surname = $user.SN
		$tele = $user.Tele
		$addr = $user.Add
		$zip = $user.Zip
		$city = $user.City
		$displayName = "$givenName $surname"

		if(Get-ADOrganizationalUnit -Filter "Name -eq '$City'") {
				Write-Host "$City OU already exist"
		} else {
				Write-Host "Creating $city OU"
				New-ADOrganizationalUnit -Name $city -Path

				Write-Host "Creating OUs in $city"
				New-ADOrganizationalUnit -Name "Användare" -Path "DC=$city,$DC"
				New-ADOrganizationalUnit -Name "Datorer" -Path "DC=$city,$DC"
				New-ADOrganizationalUnit -Name "Grupper" -Path "DC=$city,$DC"
		}

		if (Get-ADOrganizationalUnit -Filter "Name -eq '$City'") {
			Write-Host "Användaren finns redan"
		} else {
			New-ADUser -Name $loggon `
			-Surname $surname `
			-DisplayName $displayName `
			-StreetAddress $addr `
			-City $city `
			-PostalCode $zip `
			-Title $title `
			-Path "DC=$city,$DC" `
			-AccountPassword (ConvertTo-SecureString Linux4Ever -asplaintext -force) -Enabled $true `
			-SamAccountName $loggon
		} 
}
