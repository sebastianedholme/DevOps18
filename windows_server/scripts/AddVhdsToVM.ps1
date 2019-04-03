$NumDisk = 6
$Path = "C:\VM"
$vmHosts = "ServerSthlm", "ServerMalmö"
$VhdName = "Red"

foreach ($vmHost in $vmHosts) {
    for ($i = 0; $i -lt $NumDisk; $i++) {
        $DiskName = "$VhdName{0:00}" -f ($i + 1)
        Write-Host "Creating disk" ($i + 1) "of" $NumDisk ":" $DiskName
        New-VHD -Dynamic $Path\$DiskName.vhdx -SizeBytes 60GB
    }

    for ($i = 0; $i -lt $NumDisk; $i++) {
        $DiskName = "$VhdName{0:00}" -f ($i + 1)
        Write-Host "Adding $DiskName to $vmHost"

        Add-VMHardDiskDrive -VMName $VmHost -Path $Path\$DiskName.vhdx -ControllerType SCSI
    }
}