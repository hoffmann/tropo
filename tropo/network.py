from tropo.base import Resource, SubResource


class VirtualNetwork(Resource):
    """Microsoft.Network/virtualNetworks

    Args:
        name (str): The name of the resource
        location (str): The location of the resource
        description (str): a description of the resource
        tags: ({str}): a dictionary of tags
        dependsOn: ([]): a list of resources
        addressSpace (AddressSpace):  Microsoft.Network/virtualNetworks: Address space
        dhcpOptions (DhcpOption):  Microsoft.Network/virtualNetworks: DHCP options
        subnets ([Subnet]):  Microsoft.Network/virtualNetworks: Subnets  

    """

    type = 'Microsoft.Network/virtualNetworks'
    apiVersion = '2016-03-30'
    
    _attribute_map = {
        'apiVersion': {'key': 'apiVersion', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'tags': {'key': 'tags', 'type': 'str'},
        'addressSpace': {'key': 'properties.addressSpace', 'type': 'AddressSpace'},
        'dhcpOptions': {'key': 'properties.dhcpOptions', 'type': 'DhcpOption'},
        'subnets': {'key': 'properties.subnets', 'type': '[Subnet]'}   
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
        publicIPAllocationMethod (str):  Microsoft.Network/publicIPAddresses: Public IP allocation method
        idleTimeoutInMinutes (str|float):  
        dnsSettings (PublicIPAddressDnsSetting):  Microsoft.Network/publicIPAddresses: DNS settings  

    """

    type = 'Microsoft.Network/publicIPAddresses'
    apiVersion = '2016-03-30'
    
    _attribute_map = {
        'apiVersion': {'key': 'apiVersion', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'tags': {'key': 'tags', 'type': 'str'},
        'publicIPAllocationMethod': {'key': 'properties.publicIPAllocationMethod', 'type': 'str'},
        'idleTimeoutInMinutes': {'key': 'properties.idleTimeoutInMinutes', 'type': 'str|float'},
        'dnsSettings': {'key': 'properties.dnsSettings', 'type': 'PublicIPAddressDnsSetting'}   
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
        securityRules ([SecurityRule]):  Microsoft.Network/networkSecurityGroups: Security rules  

    """

    type = 'Microsoft.Network/networkSecurityGroups'
    apiVersion = '2016-03-30'
    
    _attribute_map = {
        'apiVersion': {'key': 'apiVersion', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'tags': {'key': 'tags', 'type': 'str'},
        'securityRules': {'key': 'properties.securityRules', 'type': '[SecurityRule]'}   
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
        
class NetworkInterface(Resource):
    """Microsoft.Network/networkInterfaces

    Args:
        name (str): The name of the resource
        location (str): The location of the resource
        description (str): a description of the resource
        tags: ({str}): a dictionary of tags
        dependsOn: ([]): a list of resources
        enableIPForwarding (bool):  Microsoft.Network/networkInterfaces: Enable IP forwarding
        networkSecurityGroup (Id):  Microsoft.Network/networkInterfaces: Network security group
        ipConfigurations ([IpConfiguration]):  Microsoft.Network/networkInterfaces: IP configurations
        dnsSettings (NetworkInterfaceDnsSetting):  Microsoft.Network/networkInterfaces: DNS settings  

    """

    type = 'Microsoft.Network/networkInterfaces'
    apiVersion = '2016-03-30'
    
    _attribute_map = {
        'apiVersion': {'key': 'apiVersion', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'tags': {'key': 'tags', 'type': 'str'},
        'enableIPForwarding': {'key': 'properties.enableIPForwarding', 'type': 'bool'},
        'networkSecurityGroup': {'key': 'properties.networkSecurityGroup', 'type': 'Id'},
        'ipConfigurations': {'key': 'properties.ipConfigurations', 'type': '[IpConfiguration]'},
        'dnsSettings': {'key': 'properties.dnsSettings', 'type': 'NetworkInterfaceDnsSetting'}   
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
        
class Subnet(SubResource):
    """

    Args:
        name (str):  
        addressPrefix (str):  
        networkSecurityGroup (Id):  
        routeTable (Id):  

    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str', 'required': True},
        'addressPrefix': {'key': 'properties.addressPrefix', 'type': 'str'},
        'networkSecurityGroup': {'key': 'properties.networkSecurityGroup', 'type': 'Id'},
        'routeTable': {'key': 'properties.routeTable', 'type': 'Id'}
    }

    def __init__(self, name=None, addressPrefix=None, networkSecurityGroup=None, routeTable=None):
        self.name = name
        self.addressPrefix = addressPrefix
        self.networkSecurityGroup = networkSecurityGroup
        self.routeTable = routeTable
        
class Id(SubResource):
    """

    Args:
        id (str):  

    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str', 'required': True}
    }

    def __init__(self, id=None):
        self.id = id
        
class IpConfiguration(SubResource):
    """

    Args:
        name (str):  
        subnet (Id):  
        privateIPAddress (str):  
        privateIPAllocationMethod (str):  
        publicIPAddress (Id):  
        loadBalancerBackendAddressPools ([Id]):  
        loadBalancerInboundNatRules ([Id]):  

    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str', 'required': True},
        'subnet': {'key': 'properties.subnet', 'type': 'Id'},
        'privateIPAddress': {'key': 'properties.privateIPAddress', 'type': 'str'},
        'privateIPAllocationMethod': {'key': 'properties.privateIPAllocationMethod', 'type': 'str'},
        'publicIPAddress': {'key': 'properties.publicIPAddress', 'type': 'Id'},
        'loadBalancerBackendAddressPools': {'key': 'properties.loadBalancerBackendAddressPools', 'type': '[Id]'},
        'loadBalancerInboundNatRules': {'key': 'properties.loadBalancerInboundNatRules', 'type': '[Id]'}
    }

    def __init__(self, name=None, subnet=None, privateIPAddress=None, privateIPAllocationMethod=None, publicIPAddress=None, loadBalancerBackendAddressPools=None, loadBalancerInboundNatRules=None):
        self.name = name
        self.subnet = subnet
        self.privateIPAddress = privateIPAddress
        self.privateIPAllocationMethod = privateIPAllocationMethod
        self.publicIPAddress = publicIPAddress
        self.loadBalancerBackendAddressPools = loadBalancerBackendAddressPools
        self.loadBalancerInboundNatRules = loadBalancerInboundNatRules
        
class NetworkInterfaceDnsSetting(SubResource):
    """

    Args:
        dnsServers ([str]):  
        internalDnsNameLabel (str):  

    """

    _attribute_map = {
        'dnsServers': {'key': 'dnsServers', 'type': '[str]'},
        'internalDnsNameLabel': {'key': 'internalDnsNameLabel', 'type': 'str'}
    }

    def __init__(self, dnsServers=None, internalDnsNameLabel=None):
        self.dnsServers = dnsServers
        self.internalDnsNameLabel = internalDnsNameLabel
        
class SecurityRule(SubResource):
    """

    Args:
        name (str):  
        description (str):  
        protocol (str):  
        sourcePortRange (str):  
        destinationPortRange (str):  
        sourceAddressPrefix (str):  
        destinationAddressPrefix (str):  
        access (str):  
        priority (str|float):  
        direction (str):  

    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str', 'required': True},
        'description': {'key': 'properties.description', 'type': 'str'},
        'protocol': {'key': 'properties.protocol', 'type': 'str'},
        'sourcePortRange': {'key': 'properties.sourcePortRange', 'type': 'str'},
        'destinationPortRange': {'key': 'properties.destinationPortRange', 'type': 'str'},
        'sourceAddressPrefix': {'key': 'properties.sourceAddressPrefix', 'type': 'str'},
        'destinationAddressPrefix': {'key': 'properties.destinationAddressPrefix', 'type': 'str'},
        'access': {'key': 'properties.access', 'type': 'str'},
        'priority': {'key': 'properties.priority', 'type': 'str|float'},
        'direction': {'key': 'properties.direction', 'type': 'str'}
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
        
class AddressSpace(SubResource):
    """

    Args:
        addressPrefixes ([str]):  

    """

    _attribute_map = {
        'addressPrefixes': {'key': 'addressPrefixes', 'type': '[str]', 'required': True}
    }

    def __init__(self, addressPrefixes=None):
        self.addressPrefixes = addressPrefixes
        