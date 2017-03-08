from tropo.base import Template, dumps
from tropo.compute import OsDisk, ImageReference, OsProfile, StorageProfile, LinuxConfiguration, PublicKey, NetworkProfile, Vhd, Ssh, VirtualMachine, HardwareProfile, NetworkInterface
from tropo.storage import StorageAccount, Sku
from tropo.network import VirtualNetwork, PublicIPAddress, IpConfiguration, AddressSpace, Subnet, Id
from tropo.func import uniqueString, _raw, resourceId, concat

vmname = "testvm"
vmsize = "Standard_DS3_v2"
storagetype = "Standard_LRS"
storagename = "teststorage"
admin_user = "testuser"
ssh_key = open("id_rsa.pub").read()


vnet = VirtualNetwork(name="vnet1",
                      addressSpace=AddressSpace(['192.168.0.0/24']),
                      subnets=[Subnet("default", addressPrefix='192.168.0.0/24')])


public_ip = PublicIPAddress(name="{}public".format(vmname),
                            publicIPAllocationMethod="Dynamic",
                            idleTimeoutInMinutes=4
                            )

network_interface = NetworkInterface(
    name="{}ic".format(vmname),
    ipConfigurations=[
        IpConfiguration(
            name="{}-ip-config".format(vmname),
            subnet=Id(concat(resourceId(vnet._type, vnet.name), '/subnets/', 'default')),
            privateIPAllocationMethod="Static",
            privateIPAddress='192.168.0.5',
            publicIPAddress=Id(resourceId(public_ip._type, public_ip.name)))],
    enableIPForwarding=False,
    dependsOn=[resourceId(public_ip._type, public_ip.name),
               resourceId(vnet._type, vnet.name)]
)

storage = StorageAccount(
    name=concat(
        uniqueString(
            _raw("subscription().subscriptionId"),
            _raw("resourceGroup().name")),
        storagename),
    sku=Sku(name=storagetype))

osdisk = OsDisk(
    name="{}-osdisk".format(vmname),
    caching="None",
    createOption="FromImage",
    vhd=Vhd(
        concat(
            "https://",
            storage.name,
            ".blob.core.windows.net/vhds/",
            vmname,
            "-osdisk.vhd")))

storage_profile = StorageProfile(
    osDisk=osdisk,
    imageReference=ImageReference(
        publisher="credativ",
        offer="Debian",
        sku="8",
        version="latest"))

os_profile = OsProfile(
    computerName=vmname,
    adminUsername=admin_user,
    linuxConfiguration=LinuxConfiguration(disablePasswordAuthentication=True,
                                          ssh=Ssh([PublicKey("/home/{}/.ssh/authorized_keys".format(admin_user), ssh_key)])))

network_profile = NetworkProfile([Id(resourceId(network_interface._type, network_interface.name))])

vm = VirtualMachine(name=vmname,
                    dependsOn=[resourceId(storage._type, storage.name),
                               resourceId(network_interface._type, network_interface.name),
                               resourceId(public_ip._type, public_ip.name),
                               ],
                    hardwareProfile=HardwareProfile(vmSize=vmsize),
                    storageProfile=storage_profile,
                    osProfile=os_profile,
                    networkProfile=network_profile)

t = Template(resources=[vnet, vm, network_interface, public_ip, storage])
print(dumps(t))
