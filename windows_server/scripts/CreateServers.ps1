<# 
These variables will be used throughout the script. Put more servers in the servers list to create
VM Hosts for those servers
#>
$Servers = "DC", "ServerSthlm", "SrvMalmo"
$Path = "C:\VM"
$Diffdisk = "$Path\Moderdiskar\ModerdiskW2016.vhdx"
$MemSize = "2GB"
$SwitchName = "VMnet"

# This will create a virtual network for the vm Hosts
Write-Host "Creating a virtual network for the servers"
if   (Get-VMSwitch -Name $SwitchName) {Write-Host "Switch already exists, using existing one"}
else {New-VMSwitch -Name $SwitchName -SwitchType Internal}

# Main loop, create all necessary servers from the server list
foreach ($Server in $Servers)
{
    $ServerPath = "$Path\$Server"
    $ServerVhdPath = "$Path\$Server\$Server.vhdx"

    Write-Host "Creating folder structure in C:\VM for $Server"
    mkdir -Force $ServerPath

    Write-Host "Making vhdx for $Server"
    New-VHD -ParentPath $Diffdisk -Path $ServerVhdPath -Differencing

    Write-Host "Creating new VMs from servers list"

    New-VM -Name "$Server" `
        -Path $ServerPath `
        -VHDPath $ServerVhdPath `
        -MemoryStartupBytes $MemSize `
        -Generation 1 `
        -SwitchName $SwitchName
}