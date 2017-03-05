import json
from haikunator import Haikunator

from tropo import Template, StorageAccount
from tropo.storage import Sku

haikunator = Haikunator(seed='blue yonder storage')

name = haikunator.haikunate(delimiter='')
storage_type="Standard_LRS"

storage = StorageAccount(name=name, sku=Sku(name=storage_type))

t = Template(resources=[storage])

print(t)
