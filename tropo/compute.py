from tropo.base import Resource

class VirtualMachine(Resource):
    """Microsoft.Compute/virtualMachines

    Args:
        name (str): The name of the resource
        location (str): The location of the resource
        description (str): a description of the resource
        tags: ({str}): a dictionary of tags
        dependsOn: ([]): a list of resources
        availabilitySet (id|str):  Microsoft.Compute/virtualMachines - Availability set
        hardwareProfile (hardwareProfile|str):  Microsoft.Compute/virtualMachines - Hardware profile
        storageProfile (storageProfile|str):  Microsoft.Compute/virtualMachines - Storage profile
        osProfile (osProfile|str):  Mirosoft.Compute/virtualMachines - Operating system profile
        networkProfile (networkProfile|str):  Microsoft.Compute/virtualMachines - Network profile  

    """

    _type = 'Microsoft.Compute/virtualMachines'
    _apiVersion = '2015-06-15'
    _attribute_map = {
        '_apiVersion': {'key': 'apiVersion', 'type': 'str'},
        '_type': {'key': 'type', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'dependsOn': {'key': 'dependsOn', 'type': '[]'},
        'availabilitySet': {'key': 'properties.availabilitySet', 'type': '_'},
        'hardwareProfile': {'key': 'properties.hardwareProfile', 'type': '_'},
        'storageProfile': {'key': 'properties.storageProfile', 'type': '_'},
        'osProfile': {'key': 'properties.osProfile', 'type': '_'},
        'networkProfile': {'key': 'properties.networkProfile', 'type': '_'}   
    }

    def __init__(self, name, location=None, description=None, tags=None, dependsOn=None, availabilitySet=None, hardwareProfile=None, storageProfile=None, osProfile=None, networkProfile=None):
        self.name = name
        if location is None:
            location = '[resourceGroup().location]'
        self.location = location
        self.description = description
        self.tags = tags
        self.dependsOn = dependsOn
        self.availabilitySet = availabilitySet
        self.hardwareProfile = hardwareProfile
        self.storageProfile = storageProfile
        self.osProfile = osProfile
        self.networkProfile = networkProfile
        


class NetworkInterface(Resource):
    """Microsoft.Network/networkInterfaces

    Args:
        name (str): The name of the resource
        location (str): The location of the resource
        description (str): a description of the resource
        tags: ({str}): a dictionary of tags
        dependsOn: ([]): a list of resources
        enableIPForwarding (boolean|str):  Microsoft.Network/networkInterfaces: Enable IP forwarding
        networkSecurityGroup (id|str):  Microsoft.Network/networkInterfaces: Network security group
        ipConfigurations ([ipConfiguration]|str):  Microsoft.Network/networkInterfaces: IP configurations
        dnsSettings (networkInterfaceDnsSettings|str):  Microsoft.Network/networkInterfaces: DNS settings  

    """

    _type = 'Microsoft.Network/networkInterfaces'
    _apiVersion = '2016-03-30'
    _attribute_map = {
        '_apiVersion': {'key': 'apiVersion', 'type': 'str'},
        '_type': {'key': 'type', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'dependsOn': {'key': 'dependsOn', 'type': '[]'},
        'enableIPForwarding': {'key': 'properties.enableIPForwarding', 'type': '_'},
        'networkSecurityGroup': {'key': 'properties.networkSecurityGroup', 'type': '_'},
        'ipConfigurations': {'key': 'properties.ipConfigurations', 'type': '_'},
        'dnsSettings': {'key': 'properties.dnsSettings', 'type': '_'}   
    }

    def __init__(self, name, location=None, description=None, tags=None, dependsOn=None, enableIPForwarding=None, networkSecurityGroup=None, ipConfigurations=None, dnsSettings=None):
        self.name = name
        if location is None:
            location = '[resourceGroup().location]'
        self.location = location
        self.description = description
        self.tags = tags
        self.dependsOn = dependsOn
        self.enableIPForwarding = enableIPForwarding
        self.networkSecurityGroup = networkSecurityGroup
        self.ipConfigurations = ipConfigurations
        self.dnsSettings = dnsSettings
        

class HardwareProfile(Resource):
    """

    Args:
        vmSize (string):   
    """
    _attribute_map = {
        'vmSize': {'key': 'vmSize', 'type': 'string', 'required': True}   
    }

    def __init__(self, vmSize=None):
        self.vmSize = vmSize

class OsProfile(Resource):
    """

    Args:
        computerName (string):  
        adminUsername (string):  
        adminPassword (string):  
        customData (string):  
        windowsConfiguration (windowsConfiguration):  
        linuxConfiguration (linuxConfiguration):  
        secrets ([secret]):   
    """
    _attribute_map = {
        'computerName': {'key': 'computerName', 'type': 'string', 'required': True},
        'adminUsername': {'key': 'adminUsername', 'type': 'string', 'required': True},
        'adminPassword': {'key': 'adminPassword', 'type': 'string', 'required': True},
        'customData': {'key': 'customData', 'type': 'string'},
        'windowsConfiguration': {'key': 'windowsConfiguration', 'type': 'windowsConfiguration'},
        'linuxConfiguration': {'key': 'linuxConfiguration', 'type': 'linuxConfiguration'},
        'secrets': {'key': 'secrets', 'type': '[secret]'}   
    }

    def __init__(self, computerName=None, adminUsername=None, adminPassword=None, customData=None, windowsConfiguration=None, linuxConfiguration=None, secrets=None):
        self.computerName = computerName
        self.adminUsername = adminUsername
        self.adminPassword = adminPassword
        self.customData = customData
        self.windowsConfiguration = windowsConfiguration
        self.linuxConfiguration = linuxConfiguration
        self.secrets = secrets

class LinuxConfiguration(Resource):
    """

    Args:
        disablePasswordAuthentication (str|boolean):  
        ssh (ssh):   
    """
    _attribute_map = {
        'disablePasswordAuthentication': {'key': 'disablePasswordAuthentication', 'type': 'str|boolean'},
        'ssh': {'key': 'ssh', 'type': 'ssh'}   
    }

    def __init__(self, disablePasswordAuthentication=None, ssh=None):
        self.disablePasswordAuthentication = disablePasswordAuthentication
        self.ssh = ssh

class Ssh(Resource):
    """

    Args:
        publicKeys ([publicKey]):   
    """
    _attribute_map = {
        'publicKeys': {'key': 'publicKeys', 'type': '[publicKey]'}   
    }

    def __init__(self, publicKeys=None):
        self.publicKeys = publicKeys

class PublicKey(Resource):
    """

    Args:
        path (string):  
        keyData (string):   
    """
    _attribute_map = {
        'path': {'key': 'path', 'type': 'string'},
        'keyData': {'key': 'keyData', 'type': 'string'}   
    }

    def __init__(self, path=None, keyData=None):
        self.path = path
        self.keyData = keyData

class StorageProfile(Resource):
    """

    Args:
        imageReference (imageReference|str):  
        osDisk (osDisk):  
        dataDisks ([dataDisk]):   
    """
    _attribute_map = {
        'imageReference': {'key': 'imageReference', 'type': 'imageReference|str'},
        'osDisk': {'key': 'osDisk', 'type': 'osDisk', 'required': True},
        'dataDisks': {'key': 'dataDisks', 'type': '[dataDisk]'}   
    }

    def __init__(self, imageReference=None, osDisk=None, dataDisks=None):
        self.imageReference = imageReference
        self.osDisk = osDisk
        self.dataDisks = dataDisks

class ImageReference(Resource):
    """

    Args:
        publisher (string):  
        offer (string):  
        sku (string):  
        version (string):   
    """
    _attribute_map = {
        'publisher': {'key': 'publisher', 'type': 'string', 'required': True},
        'offer': {'key': 'offer', 'type': 'string', 'required': True},
        'sku': {'key': 'sku', 'type': 'string', 'required': True},
        'version': {'key': 'version', 'type': 'string', 'required': True}   
    }

    def __init__(self, publisher=None, offer=None, sku=None, version=None):
        self.publisher = publisher
        self.offer = offer
        self.sku = sku
        self.version = version

class OsDisk(Resource):
    """

    Args:
        name (string):  
        vhd (vhd):  
        osType (string):  
        image (vhd):  
        caching (string):  
        createOption (string|str):   
    """
    _attribute_map = {
        'name': {'key': 'name', 'type': 'string', 'required': True},
        'vhd': {'key': 'vhd', 'type': 'vhd', 'required': True},
        'osType': {'key': 'osType', 'type': 'string'},
        'image': {'key': 'image', 'type': 'vhd'},
        'caching': {'key': 'caching', 'type': 'string'},
        'createOption': {'key': 'createOption', 'type': 'string|str', 'required': True}   
    }

    def __init__(self, name=None, vhd=None, osType=None, image=None, caching=None, createOption=None):
        self.name = name
        self.vhd = vhd
        self.osType = osType
        self.image = image
        self.caching = caching
        self.createOption = createOption

class DataDisk(Resource):
    """

    Args:
        name (string):  
        diskSizeGB (string):  
        lun (number):  
        vhd (vhdUri):  
        caching (string):  
        createOption (string|str):   
    """
    _attribute_map = {
        'name': {'key': 'name', 'type': 'string', 'required': True},
        'diskSizeGB': {'key': 'diskSizeGB', 'type': 'string'},
        'lun': {'key': 'lun', 'type': 'number', 'required': True},
        'vhd': {'key': 'vhd', 'type': 'vhdUri', 'required': True},
        'caching': {'key': 'caching', 'type': 'string'},
        'createOption': {'key': 'createOption', 'type': 'string|str', 'required': True}   
    }

    def __init__(self, name=None, diskSizeGB=None, lun=None, vhd=None, caching=None, createOption=None):
        self.name = name
        self.diskSizeGB = diskSizeGB
        self.lun = lun
        self.vhd = vhd
        self.caching = caching
        self.createOption = createOption

class NetworkProfile(Resource):
    """

    Args:
        networkInterfaces ([networkInterfaces]):   
    """
    _attribute_map = {
        'networkInterfaces': {'key': 'networkInterfaces', 'type': '[networkInterfaces]', 'required': True}   
    }

    def __init__(self, networkInterfaces=None):
        self.networkInterfaces = networkInterfaces

class Vhd(Resource):
    """

    Args:
        uri (string):   
    """
    _attribute_map = {
        'uri': {'key': 'uri', 'type': 'string', 'required': True}   
    }

    def __init__(self, uri=None):
        self.uri = uri

