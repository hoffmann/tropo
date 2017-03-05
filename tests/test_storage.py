from tropo.storage import StorageAccount, Sku

def test_storage():
    sku = Sku(name="Standard_LRS")
    assert sku._asdict() == {"name": "Standard_LRS"}


    sa = StorageAccount("teststorage", sku=sku)
    assert sa._asdict() == {'name': 'teststorage',
                            'type': 'Microsoft.Storage/storageAccounts',
                            'apiVersion': '2016-01-01',
                            'location': "[resourceGroup().location]",
                            'sku': {'name': 'Standard_LRS'}}

    sa = StorageAccount("teststorage", sku=sku, description="Test Account")
    assert sa._asdict() == {'name': 'teststorage',
                            'type': 'Microsoft.Storage/storageAccounts',
                            'apiVersion': '2016-01-01',
                            'location': "[resourceGroup().location]",
                            'sku': {'name': 'Standard_LRS'},
                            'description': 'Test Account'}

    sa = StorageAccount("teststorage", sku=sku, tags={"env": "Production"})
    assert sa._asdict() == {'name': 'teststorage',
                            'type': 'Microsoft.Storage/storageAccounts',
                            'apiVersion': '2016-01-01',
                            'location': "[resourceGroup().location]",
                            'sku': {'name': 'Standard_LRS'},
                            'tags': {'env': 'Production'}}


    sa = StorageAccount(name="storage-1", location="westeurope", sku={"name": "Standard_RAGRS"})
    expected = {
            "type": "Microsoft.Storage/storageAccounts",
            "apiVersion": "2016-01-01",
            "location": "westeurope",
            "name": "storage-1",
            "sku": {"name": "Standard_RAGRS"}
        }
    assert sa._asdict()  == expected

