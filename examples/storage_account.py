from tropo import Template, StorageAccount
from tropo.base import dumps
from tropo.storage import Sku
from tropo.func import uniqueString, _raw

storage_type="Standard_LRS"
name = uniqueString(_raw("subscription().subscriptionId"), _raw("resourceGroup().name"), "standardstorage")

storage = StorageAccount(name=name, sku=Sku(name=storage_type))

t = Template(resources=[storage])

print(dumps(t))
