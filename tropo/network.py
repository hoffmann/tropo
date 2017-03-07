from tropo.base import Resource


class VirtualNetwork(Resource):
    """Microsoft.Network/virtualNetworks

    Args:
        name (str): The name of the resource
        location (str): The location of the resource
        description (str): a description of the resource
        tags: ({str}): a dictionary of tags
        dependsOn: ([]): a list of resources
        addressSpace (addressSpace|str):  Microsoft.Network/virtualNetworks: Address space
        dhcpOptions (dhcpOptions|str):  Microsoft.Network/virtualNetworks: DHCP options
        subnets ([subnet]|str):  Microsoft.Network/virtualNetworks: Subnets  

    """

    _type = 'Microsoft.Network/virtualNetworks'
    _apiVersion = '2016-03-30'
    _attribute_map = {
        '_apiVersion': {'key': 'apiVersion', 'type': 'str'},
        '_type': {'key': 'type', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'dependsOn': {'key': 'dependsOn', 'type': '[]'},
        'addressSpace': {'key': 'properties.addressSpace', 'type': '_'},
        'dhcpOptions': {'key': 'properties.dhcpOptions', 'type': '_'},
        'subnets': {'key': 'properties.subnets', 'type': '_'}   
    }

    def __init__(self, name, location=None, description=None, tags=None, dependsOn=None, addressSpace=None, dhcpOptions=None, subnets=None):
        self.name = name
        if location is None:
            location = '[resourceGroup().location]'
        self.location = location
        self.description = description
        self.tags = tags
        self.dependsOn = dependsOn
        self.addressSpace = addressSpace
        self.dhcpOptions = dhcpOptions
        self.subnets = subnets
        


class PublicIPAddress(Resource):
    """Microsoft.Network/publicIPAddresses

    Args:
        name (str): The name of the resource
        location (str): The location of the resource
        description (str): a description of the resource
        tags: ({str}): a dictionary of tags
        dependsOn: ([]): a list of resources
        publicIPAllocationMethod (string|str):  Microsoft.Network/publicIPAddresses: Public IP allocation method
        idleTimeoutInMinutes (_):  Microsoft.Network/publicIPAddresses: Idle timeout in minutes
        dnsSettings (publicIPAddressDnsSettings|str):  Microsoft.Network/publicIPAddresses: DNS settings  

    """

    _type = 'Microsoft.Network/publicIPAddresses'
    _apiVersion = '2016-03-30'
    _attribute_map = {
        '_apiVersion': {'key': 'apiVersion', 'type': 'str'},
        '_type': {'key': 'type', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'dependsOn': {'key': 'dependsOn', 'type': '[]'},
        'publicIPAllocationMethod': {'key': 'properties.publicIPAllocationMethod', 'type': '_'},
        'idleTimeoutInMinutes': {'key': 'properties.idleTimeoutInMinutes', 'type': '_'},
        'dnsSettings': {'key': 'properties.dnsSettings', 'type': '_'}   
    }

    def __init__(self, name, location=None, description=None, tags=None, dependsOn=None, publicIPAllocationMethod=None, idleTimeoutInMinutes=None, dnsSettings=None):
        self.name = name
        if location is None:
            location = '[resourceGroup().location]'
        self.location = location
        self.description = description
        self.tags = tags
        self.dependsOn = dependsOn
        self.publicIPAllocationMethod = publicIPAllocationMethod
        self.idleTimeoutInMinutes = idleTimeoutInMinutes
        self.dnsSettings = dnsSettings
        


class NetworkSecurityGroup(Resource):
    """Microsoft.Network/networkSecurityGroups

    Args:
        name (str): The name of the resource
        location (str): The location of the resource
        description (str): a description of the resource
        tags: ({str}): a dictionary of tags
        dependsOn: ([]): a list of resources
        securityRules ([securityRules]|str):  Microsoft.Network/networkSecurityGroups: Security rules  

    """

    _type = 'Microsoft.Network/networkSecurityGroups'
    _apiVersion = '2016-03-30'
    _attribute_map = {
        '_apiVersion': {'key': 'apiVersion', 'type': 'str'},
        '_type': {'key': 'type', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'dependsOn': {'key': 'dependsOn', 'type': '[]'},
        'securityRules': {'key': 'properties.securityRules', 'type': '_'}   
    }

    def __init__(self, name, location=None, description=None, tags=None, dependsOn=None, securityRules=None):
        self.name = name
        if location is None:
            location = '[resourceGroup().location]'
        self.location = location
        self.description = description
        self.tags = tags
        self.dependsOn = dependsOn
        self.securityRules = securityRules
        

class Subnet(Resource):
    """

    Args:
        name (string):  
        addressPrefix (string):  
        networkSecurityGroup (id):  
        routeTable (id):   
    """
    _attribute_map = {
        'name': {'key': 'name', 'type': 'string', 'required': True},
        'addressPrefix': {'key': 'properties.addressPrefix', 'type': 'string', 'required': True},
        'networkSecurityGroup': {'key': 'properties.networkSecurityGroup', 'type': 'id'},
        'routeTable': {'key': 'properties.routeTable', 'type': 'id'}   
    }

    def __init__(self, name=None, addressPrefix=None, networkSecurityGroup=None, routeTable=None):
        self.name = name
        self.addressPrefix = addressPrefix
        self.networkSecurityGroup = networkSecurityGroup
        self.routeTable = routeTable

class Id(Resource):
    """

    Args:
        id (string):   
    """
    _attribute_map = {
        'id': {'key': 'id', 'type': 'string', 'required': True}   
    }

    def __init__(self, id=None):
        self.id = id

class IpConfiguration(Resource):
    """

    Args:
        name (string):  
        subnet (id):  
        privateIPAddress (string):  
        privateIPAllocationMethod (string|str):  
        publicIPAddress (id):  
        loadBalancerBackendAddressPools ([id]):  
        loadBalancerInboundNatRules ([id]):   
    """
    _attribute_map = {
        'name': {'key': 'name', 'type': 'string', 'required': True},
        'subnet': {'key': 'properties.subnet', 'type': 'id', 'required': True},
        'privateIPAddress': {'key': 'properties.privateIPAddress', 'type': 'string'},
        'privateIPAllocationMethod': {'key': 'properties.privateIPAllocationMethod', 'type': 'string|str', 'required': True},
        'publicIPAddress': {'key': 'properties.publicIPAddress', 'type': 'id'},
        'loadBalancerBackendAddressPools': {'key': 'properties.loadBalancerBackendAddressPools', 'type': '[id]'},
        'loadBalancerInboundNatRules': {'key': 'properties.loadBalancerInboundNatRules', 'type': '[id]'}   
    }

    def __init__(self, name=None, subnet=None, privateIPAddress=None, privateIPAllocationMethod=None, publicIPAddress=None, loadBalancerBackendAddressPools=None, loadBalancerInboundNatRules=None):
        self.name = name
        self.subnet = subnet
        self.privateIPAddress = privateIPAddress
        self.privateIPAllocationMethod = privateIPAllocationMethod
        self.publicIPAddress = publicIPAddress
        self.loadBalancerBackendAddressPools = loadBalancerBackendAddressPools
        self.loadBalancerInboundNatRules = loadBalancerInboundNatRules

class NetworkInterfaceDnsSetting(Resource):
    """

    Args:
        dnsServers (str|[string]):  
        internalDnsNameLabel (string):   
    """
    _attribute_map = {
        'dnsServers': {'key': 'dnsServers', 'type': 'str|[string]'},
        'internalDnsNameLabel': {'key': 'internalDnsNameLabel', 'type': 'string'}   
    }

    def __init__(self, dnsServers=None, internalDnsNameLabel=None):
        self.dnsServers = dnsServers
        self.internalDnsNameLabel = internalDnsNameLabel

class SecurityRule(Resource):
    """

    Args:
        name (string):  
        description (string):  
        protocol (string|str):  
        sourcePortRange (string):  
        destinationPortRange (string):  
        sourceAddressPrefix (string):  
        destinationAddressPrefix (string):  
        access (string|str):  
        priority (number|expr):  
        direction (string|str):   
    """
    _attribute_map = {
        'name': {'key': 'name', 'type': 'string', 'required': True},
        'description': {'key': 'properties.description', 'type': 'string'},
        'protocol': {'key': 'properties.protocol', 'type': 'string|str', 'required': True},
        'sourcePortRange': {'key': 'properties.sourcePortRange', 'type': 'string', 'required': True},
        'destinationPortRange': {'key': 'properties.destinationPortRange', 'type': 'string', 'required': True},
        'sourceAddressPrefix': {'key': 'properties.sourceAddressPrefix', 'type': 'string', 'required': True},
        'destinationAddressPrefix': {'key': 'properties.destinationAddressPrefix', 'type': 'string', 'required': True},
        'access': {'key': 'properties.access', 'type': 'string|str', 'required': True},
        'priority': {'key': 'properties.priority', 'type': 'number|expr', 'required': True},
        'direction': {'key': 'properties.direction', 'type': 'string|str', 'required': True}   
    }

    def __init__(self, name=None, description=None, protocol=None, sourcePortRange=None, destinationPortRange=None, sourceAddressPrefix=None, destinationAddressPrefix=None, access=None, priority=None, direction=None):
        self.name = name
        self.description = description
        self.protocol = protocol
        self.sourcePortRange = sourcePortRange
        self.destinationPortRange = destinationPortRange
        self.sourceAddressPrefix = sourceAddressPrefix
        self.destinationAddressPrefix = destinationAddressPrefix
        self.access = access
        self.priority = priority
        self.direction = direction

class AddressSpace(Resource):
    """

    Args:
        addressPrefixes ([string]):   
    """
    _attribute_map = {
        'addressPrefixes': {'key': 'addressPrefixes', 'type': '[string]', 'required': True}   
    }

    def __init__(self, addressPrefixes=None):
        self.addressPrefixes = addressPrefixes

