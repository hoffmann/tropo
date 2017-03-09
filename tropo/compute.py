from tropo.base import Resource, SubResource


class VirtualMachine(Resource):
    """Microsoft.Compute/virtualMachines

    Args:
        name (str): The name of the resource
        location (str): The location of the resource
        description (str): a description of the resource
        tags: ({str}): a dictionary of tags
        dependsOn: ([]): a list of resources
        plan (Plan):  The purchase plan when deploying virtual machine from VM Marketplace images.
        resources ([Nitions/extensionsChild]):  
        hardwareProfile (HardwareProfile):  The hardware profile.
        storageProfile (StorageProfile):  The storage profile.
        osProfile (OSProfile):  The OS profile.
        networkProfile (NetworkProfile):  The network profile.
        diagnosticsProfile (DiagnosticsProfile):  The diagnostics profile.
        availabilitySet (SubResource):  The reference Id of the availability set to which the virtual machine belongs.
        licenseType (str):  Specifies that the image or disk that is being used was licensed on-premises.
            This element is only used for images that contain the Windows Server
            operating system.  

    """

    type = 'Microsoft.Compute/virtualMachines'
    apiVersion = '2016-04-30-preview'
    
    _attribute_map = {
        'apiVersion': {'key': 'apiVersion', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'tags': {'key': 'tags', 'type': 'str'},
        'dependsOn': {'key': 'dependsOn', 'type': '[str]'},
        'plan': {'key': 'plan', 'type': 'Plan'},
        'resources': {'key': 'resources', 'type': '[Nitions/extensionsChild]'},
        'hardwareProfile': {'key': 'properties.hardwareProfile', 'type': 'HardwareProfile'},
        'storageProfile': {'key': 'properties.storageProfile', 'type': 'StorageProfile'},
        'osProfile': {'key': 'properties.osProfile', 'type': 'OSProfile'},
        'networkProfile': {'key': 'properties.networkProfile', 'type': 'NetworkProfile'},
        'diagnosticsProfile': {'key': 'properties.diagnosticsProfile', 'type': 'DiagnosticsProfile'},
        'availabilitySet': {'key': 'properties.availabilitySet', 'type': 'SubResource'},
        'licenseType': {'key': 'properties.licenseType', 'type': 'str'}   
    }

    def __init__(self, name, location=None, description=None, tags=None, dependsOn=None, plan=None, resources=None, hardwareProfile=None, storageProfile=None, osProfile=None, networkProfile=None, diagnosticsProfile=None, availabilitySet=None, licenseType=None):
        self.name = name
        if location is None:
            location = '[resourceGroup().location]'
        self.location = location
        self.description = description
        self.tags = tags
        self.dependsOn = dependsOn
        self.plan = plan
        self.resources = resources
        self.hardwareProfile = hardwareProfile
        self.storageProfile = storageProfile
        self.osProfile = osProfile
        self.networkProfile = networkProfile
        self.diagnosticsProfile = diagnosticsProfile
        self.availabilitySet = availabilitySet
        self.licenseType = licenseType
        
class HardwareProfile(SubResource):
    """Describes a hardware profile.

    Args:
        vmSize (str):  The virtual machine size name.

    """

    _attribute_map = {
        'vmSize': {'key': 'vmSize', 'type': 'str'}
    }

    def __init__(self, vmSize=None):
        self.vmSize = vmSize
        
class OSProfile(SubResource):
    """Describes an OS profile.

    Args:
        computerName (str):  Specifies the host OS name of the virtual machine.
        adminUsername (str):  Specifies the name of the administrator account.
        adminPassword (str):  Specifies the password of the administrator account.
        customData (str):  Specifies a base-64 encoded string of custom data. The base-64 encoded string is
            decoded to a binary array that is saved as a file on the Virtual
            Machine. The maximum length of the binary array is 65535 bytes
        windowsConfiguration (WindowsConfiguration):  The Windows configuration of the OS profile.
        linuxConfiguration (LinuxConfiguration):  The Linux configuration of the OS profile.
        secrets ([VaultSecretGroup]):  The list of certificates for addition to the VM.

    """

    _attribute_map = {
        'computerName': {'key': 'computerName', 'type': 'str'},
        'adminUsername': {'key': 'adminUsername', 'type': 'str'},
        'adminPassword': {'key': 'adminPassword', 'type': 'str'},
        'customData': {'key': 'customData', 'type': 'str'},
        'windowsConfiguration': {'key': 'windowsConfiguration', 'type': 'WindowsConfiguration'},
        'linuxConfiguration': {'key': 'linuxConfiguration', 'type': 'LinuxConfiguration'},
        'secrets': {'key': 'secrets', 'type': '[VaultSecretGroup]'}
    }

    def __init__(self, computerName=None, adminUsername=None, adminPassword=None, customData=None, windowsConfiguration=None, linuxConfiguration=None, secrets=None):
        self.computerName = computerName
        self.adminUsername = adminUsername
        self.adminPassword = adminPassword
        self.customData = customData
        self.windowsConfiguration = windowsConfiguration
        self.linuxConfiguration = linuxConfiguration
        self.secrets = secrets
        
class LinuxConfiguration(SubResource):
    """Describes Linux configuration of the OS Profile.

    Args:
        disablePasswordAuthentication (bool):  Specifies whether password authentication should be disabled.
        ssh (SshConfiguration):  The SSH configuration for linux VMs.

    """

    _attribute_map = {
        'disablePasswordAuthentication': {'key': 'disablePasswordAuthentication', 'type': 'bool'},
        'ssh': {'key': 'ssh', 'type': 'SshConfiguration'}
    }

    def __init__(self, disablePasswordAuthentication=None, ssh=None):
        self.disablePasswordAuthentication = disablePasswordAuthentication
        self.ssh = ssh
        
class SshConfiguration(SubResource):
    """SSH configuration for Linux based VMs running on Azure

    Args:
        publicKeys ([SshPublicKey]):  The list of SSH public keys used to authenticate with linux based VMs.

    """

    _attribute_map = {
        'publicKeys': {'key': 'publicKeys', 'type': '[SshPublicKey]'}
    }

    def __init__(self, publicKeys=None):
        self.publicKeys = publicKeys
        
class SshPublicKey(SubResource):
    """Contains information about SSH certificate public key and the path on the Linux VM where the public key is placed.

    Args:
        path (str):  Specifies the full path on the created VM where SSH public key is stored. If the
            file already exists, the specified key is appended to the file.
        keyData (str):  Certificate public key used to authenticate to the VM through SSH. The
            certificate must be in Pem format with or without headers.

    """

    _attribute_map = {
        'path': {'key': 'path', 'type': 'str'},
        'keyData': {'key': 'keyData', 'type': 'str'}
    }

    def __init__(self, path=None, keyData=None):
        self.path = path
        self.keyData = keyData
        
class StorageProfile(SubResource):
    """Describes a storage profile.

    Args:
        imageReference (ImageReference):  The image reference.
        osDisk (OSDisk):  The OS disk.
        dataDisks ([DataDisk]):  The data disks.

    """

    _attribute_map = {
        'imageReference': {'key': 'imageReference', 'type': 'ImageReference'},
        'osDisk': {'key': 'osDisk', 'type': 'OSDisk'},
        'dataDisks': {'key': 'dataDisks', 'type': '[DataDisk]'}
    }

    def __init__(self, imageReference=None, osDisk=None, dataDisks=None):
        self.imageReference = imageReference
        self.osDisk = osDisk
        self.dataDisks = dataDisks
        
class ImageReference(SubResource):
    """The image reference.

    Args:
        id (str):  Resource Id
        publisher (str):  The image publisher.
        offer (str):  The image offer.
        sku (str):  The image SKU.
        version (str):  The image version. The allowed formats are Major.Minor.Build or 'latest'. Major,
            Minor and Build are decimal numbers. Specify 'latest' to use the
            latest version of the image.

    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'publisher': {'key': 'publisher', 'type': 'str'},
        'offer': {'key': 'offer', 'type': 'str'},
        'sku': {'key': 'sku', 'type': 'str'},
        'version': {'key': 'version', 'type': 'str'}
    }

    def __init__(self, id=None, publisher=None, offer=None, sku=None, version=None):
        self.id = id
        self.publisher = publisher
        self.offer = offer
        self.sku = sku
        self.version = version
        
class OSDisk(SubResource):
    """Describes an Operating System disk.

    Args:
        osType (str):  The Operating System type.
        encryptionSettings (DiskEncryptionSetting):  The disk encryption settings.
        name (str):  The disk name.
        vhd (VirtualHardDisk):  The virtual hard disk.
        image (VirtualHardDisk):  The source user image virtual hard disk. The virtual hard disk will be copied
            before using it to attach to the virtual machine. If SourceImage is
            provided, the destination virtual hard disk must not exist.
        caching (str):  The caching type.
        createOption (str):  The create option.
        diskSizeGB (int):  The initial disk size, in GB, for blank data disks, and the new desired size for
            resizing existing OS and data disks.
        managedDisk (ManagedDiskParameter):  The managed disk parameters.

    """

    _attribute_map = {
        'osType': {'key': 'osType', 'type': 'str'},
        'encryptionSettings': {'key': 'encryptionSettings', 'type': 'DiskEncryptionSetting'},
        'name': {'key': 'name', 'type': 'str'},
        'vhd': {'key': 'vhd', 'type': 'VirtualHardDisk'},
        'image': {'key': 'image', 'type': 'VirtualHardDisk'},
        'caching': {'key': 'caching', 'type': 'str'},
        'createOption': {'key': 'createOption', 'type': 'str', 'required': True},
        'diskSizeGB': {'key': 'diskSizeGB', 'type': 'int'},
        'managedDisk': {'key': 'managedDisk', 'type': 'ManagedDiskParameter'}
    }

    def __init__(self, osType=None, encryptionSettings=None, name=None, vhd=None, image=None, caching=None, createOption=None, diskSizeGB=None, managedDisk=None):
        self.osType = osType
        self.encryptionSettings = encryptionSettings
        self.name = name
        self.vhd = vhd
        self.image = image
        self.caching = caching
        self.createOption = createOption
        self.diskSizeGB = diskSizeGB
        self.managedDisk = managedDisk
        
class DataDisk(SubResource):
    """Describes a data disk.

    Args:
        lun (int):  The logical unit number.
        name (str):  The disk name.
        vhd (VirtualHardDisk):  The virtual hard disk.
        image (VirtualHardDisk):  The source user image virtual hard disk. This virtual hard disk will be copied
            before using it to attach to the virtual machine. If SourceImage is
            provided, the destination virtual hard disk must not exist.
        caching (str):  The caching type.
        createOption (str):  The create option.
        diskSizeGB (int):  The initial disk size in GB for blank data disks, and the new desired size for
            resizing existing OS and data disks.
        managedDisk (ManagedDiskParameter):  The managed disk parameters.

    """

    _attribute_map = {
        'lun': {'key': 'lun', 'type': 'int', 'required': True},
        'name': {'key': 'name', 'type': 'str'},
        'vhd': {'key': 'vhd', 'type': 'VirtualHardDisk'},
        'image': {'key': 'image', 'type': 'VirtualHardDisk'},
        'caching': {'key': 'caching', 'type': 'str'},
        'createOption': {'key': 'createOption', 'type': 'str', 'required': True},
        'diskSizeGB': {'key': 'diskSizeGB', 'type': 'int'},
        'managedDisk': {'key': 'managedDisk', 'type': 'ManagedDiskParameter'}
    }

    def __init__(self, lun=None, name=None, vhd=None, image=None, caching=None, createOption=None, diskSizeGB=None, managedDisk=None):
        self.lun = lun
        self.name = name
        self.vhd = vhd
        self.image = image
        self.caching = caching
        self.createOption = createOption
        self.diskSizeGB = diskSizeGB
        self.managedDisk = managedDisk
        
class NetworkProfile(SubResource):
    """Describes a network profile.

    Args:
        networkInterfaces ([NetworkInterfaceReference]):  Specifies the list of resource IDs for the network interfaces associated with
            the virtual machine.

    """

    _attribute_map = {
        'networkInterfaces': {'key': 'networkInterfaces', 'type': '[NetworkInterfaceReference]'}
    }

    def __init__(self, networkInterfaces=None):
        self.networkInterfaces = networkInterfaces
        
class VirtualHardDisk(SubResource):
    """Describes the uri of a disk.

    Args:
        uri (str):  The virtual hard disk's URI. Must be a valid URI to a virtual hard disk.

    """

    _attribute_map = {
        'uri': {'key': 'uri', 'type': 'str'}
    }

    def __init__(self, uri=None):
        self.uri = uri
        