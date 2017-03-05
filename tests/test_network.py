from tropo.network import VirtualNetwork, NetworkSecurityGroup, AddressSpace, SecurityRule


def test_vnet():
    vnet = VirtualNetwork(name="vnet1",
                          addressSpace=AddressSpace(["192.168.0.0/24"]))

    expected = {
        'apiVersion': '2016-03-30',
        'type': 'Microsoft.Network/virtualNetworks',
        'name': 'vnet1',
        'location': '[resourceGroup().location]',
        'properties': {
            'addressSpace': {
                'addressPrefixes': ['192.168.0.0/24']}}}
    assert vnet._asdict() == expected


def test_network_security_group():
    nsg = NetworkSecurityGroup("nsg1")
    # FIXME properties.securityRules is required
    expected = {'apiVersion': '2016-03-30',
                'type': 'Microsoft.Network/networkSecurityGroups',
                'name': 'nsg1',
                'location': '[resourceGroup().location]'}

    assert nsg._asdict() == expected

    rule = SecurityRule(name="rule1",
                        protocol="*",
                        sourcePortRange="*",
                        destinationPortRange="*",
                        sourceAddressPrefix="*",
                        destinationAddressPrefix="*",
                        access="ALLOW",
                        priority=2000,
                        direction='Inbound')

    nsg = NetworkSecurityGroup("nsg1", securityRules=[rule])

    expected = {'apiVersion': '2016-03-30',
                'type': 'Microsoft.Network/networkSecurityGroups',
                'name': 'nsg1',
                'location': '[resourceGroup().location]',
                'properties':{
                  'securityRules':[
                    {"name": "rule1",
                     "properties": {
                         "protocol": "*",
                         "sourcePortRange": "*",
                         "destinationPortRange": "*",
                         "sourceAddressPrefix": "*",
                         "destinationAddressPrefix": "*",
                         "access": "ALLOW",
                         "priority": 2000,
                         "direction": "Inbound"
                     }
                   }
                  ]
                  }
                }
    assert nsg._asdict() == expected


def test_security_rule():
    rule = SecurityRule(name="rule1",
                        protocol="*",
                        sourcePortRange="*",
                        destinationPortRange="*",
                        sourceAddressPrefix="*",
                        destinationAddressPrefix="*",
                        access="ALLOW",
                        priority=2000,
                        direction='Inbound')

    expected = {"name": "rule1",
                "properties": {
                    "protocol": "*",
                    "sourcePortRange": "*",
                    "destinationPortRange": "*",
                    "sourceAddressPrefix": "*",
                    "destinationAddressPrefix": "*",
                    "access": "ALLOW",
                    "priority": 2000,
                    "direction": "Inbound"
                }
                }

    assert rule._asdict() == expected


def test_address_space():
    a = AddressSpace(["192.168.0.0/24"])
    expected = {'addressPrefixes': ['192.168.0.0/24']}
    assert a._asdict() == expected

    a = AddressSpace(addressPrefixes=["192.168.0.0/24"])
    expected = {'addressPrefixes': ['192.168.0.0/24']}
    assert a._asdict() == expected
