from tropo.network import VirtualNetwork, addressSpace


def test_vnet():
    vnet = VirtualNetwork(name="vnet1",
                          addressSpace=addressSpace(["192.168.0.0/24"]))
    
    expected = {'apiVersion': '2016-03-30', 
                'type': 'Microsoft.Network/virtualNetworks', 
                'name': 'vnet1', 
                'location': '[resourceGroup().location]',
                'properties': {'addressSpace': {'addressPrefixes': ['192.168.0.0/24']}}}
    assert vnet._asdict() == expected


def test_address_space():
    a = addressSpace(["192.168.0.0/24"])
    expected = {'addressPrefixes': ['192.168.0.0/24']}
    assert a._asdict() == expected

    
    a = addressSpace(addressPrefixes=["192.168.0.0/24"])
    expected = {'addressPrefixes': ['192.168.0.0/24']}
    assert a._asdict() == expected
