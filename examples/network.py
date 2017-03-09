from netaddr import IPNetwork

from tropo import Template, dumps
from tropo.network import VirtualNetwork, AddressSpace

ip = IPNetwork('192.168.0.0/24')

subnets = []
for (name, subnet) in zip(["frontend", "backend", "db"], ip.subnet(26)):
    subnets.append({"name": name,
                    "properties": {"addressPrefix": str(subnet.cidr)}})

vnet = VirtualNetwork(name="vnet1",
                      addressSpace=AddressSpace([str(ip.cidr)]),
                      subnets=subnets)

t = Template(resources=[vnet])
print(dumps(t))
