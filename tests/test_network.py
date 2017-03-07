from tropo.network import VirtualNetwork, NetworkSecurityGroup, AddressSpace, SecurityRule, PublicIPAddress, Subnet, Id, IpConfiguration, NetworkInterfaceDnsSetting


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


def test_public_ip_address():
    ip = PublicIPAddress(name="testip",
                         publicIPAllocationMethod="Dynamic",
                         idleTimeoutInMinutes=4)

    expected = {
        "apiVersion": "2016-03-30",
        "type": "Microsoft.Network/publicIPAddresses",
        "name": "testip",
        "location": "[resourceGroup().location]",
        "properties": {
            "publicIPAllocationMethod": "Dynamic",
            "idleTimeoutInMinutes": 4
        }
    }
    assert ip._asdict() == expected


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
                'properties': {
                    'securityRules': [
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


def test_subnet():
    sn = Subnet("default", addressPrefix="192.168.0.1/24")

    expected = {
        "name": "default",
        "properties": {
            "addressPrefix": "192.168.0.1/24"
        }
    }
    assert sn._asdict() == expected


def test_id():
    i = Id("foo")
    expected = {
        "id": "foo"
    }
    assert i._asdict() == expected


def test_ip_configuration():
    ipc = IpConfiguration(
        name="testhost",
        subnet=Id("test"),
        privateIPAllocationMethod="Static",
        privateIPAddress="192.168.0.2",
        publicIPAddress=Id("public_ip"))

    expected = {
        "name": "testhost",
        "properties": {
            "subnet": {
                "id": "test"
            },
            "privateIPAddress": "192.168.0.2",
            "privateIPAllocationMethod": "Static",
            "publicIPAddress": {
                "id": "public_ip"
            }
        }
    }
    assert ipc._asdict() == expected


def test_network_interface_dns_setting():
    dns = NetworkInterfaceDnsSetting(dnsServers=["8.8.8.8"],
                                     internalDnsNameLabel="host.local")
    expected = {
        "dnsServers": [
            "8.8.8.8"
        ],
        "internalDnsNameLabel": "host.local"
    }

    assert dns._asdict() == expected


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
