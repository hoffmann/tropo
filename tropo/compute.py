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
        

