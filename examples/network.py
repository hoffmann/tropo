from netaddr import IPNetwork

from tropo import Template
from tropo.network import VirtualNetwork

ip = IPNetwork('192.168.0.0/24')

subnets = []
for (n, subnet) in enumerate(ip.subnet(26)):
    subnets.append({"name": "sn{}".format(n),
                    "properties": {"addressPrefix": str(subnet.cidr)}})

vnet = VirtualNetwork(name="vnet1",
                      addressSpace={"addressPrefixes": [str(ip.cidr)]},
                      subnets=subnets)

t = Template(resources=[vnet])
print(t)
