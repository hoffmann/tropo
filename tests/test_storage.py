from tropo.storage import StorageAccount, Sku
from tropo.base import dump

def test_storage():
    sku = Sku(name="Standard_LRS")
    assert dump(sku) == {"name": "Standard_LRS"}


    sa = StorageAccount("teststorage", sku=sku, kind="Storage")
    assert dump(sa) == {'name': 'teststorage',
                            'type': 'Microsoft.Storage/storageAccounts',
                            'apiVersion': '2016-01-01',
                            'location': "[resourceGroup().location]",
                            'sku': {'name': 'Standard_LRS'},
                            'kind': 'Storage'
                        }

    sa = StorageAccount("teststorage", sku=sku, description="Test Account", kind="Storage")
    assert dump(sa) == {'name': 'teststorage',
                            'type': 'Microsoft.Storage/storageAccounts',
                            'apiVersion': '2016-01-01',
                            'location': "[resourceGroup().location]",
                            'sku': {'name': 'Standard_LRS'},
                            'description': 'Test Account',
                            'kind': 'Storage'
                        }

    sa = StorageAccount("teststorage", sku=sku, tags={"env": "Production"}, kind='Storage')
    assert dump(sa) == {'name': 'teststorage',
                            'type': 'Microsoft.Storage/storageAccounts',
                            'apiVersion': '2016-01-01',
                            'location': "[resourceGroup().location]",
                            'sku': {'name': 'Standard_LRS'},
                            'tags': {'env': 'Production'},
                            'kind': 'Storage'
                        }


    sa = StorageAccount(name="storage-1", location="westeurope", sku={"name": "Standard_RAGRS"}, kind='Storage')
    expected = {
            "type": "Microsoft.Storage/storageAccounts",
            "apiVersion": "2016-01-01",
            "location": "westeurope",
            "name": "storage-1",
            "sku": {"name": "Standard_RAGRS"},
            "kind": "Storage"
        }
    assert dump(sa)  == expected

