from tropo.base import Template, dump
from tropo.storage import StorageAccount

def test_template():
    sa = StorageAccount(name="storage-1", location="westeurope", sku={"name": "Standard_RAGRS"})
    t = Template(resources=[sa])
    expected = {'$schema': 'https://schema.management.azure.com/schemas/2015-01-01/deploymentTemplate.json#', 
                'contentVersion': '1.0.0.0', 
                'resources': [
                    {
                        "type": "Microsoft.Storage/storageAccounts",
                        "name": "storage-1",
                        "apiVersion": "2016-01-01",
                        "location": "westeurope",
                        "sku": {
                            "name": "Standard_RAGRS"
                        },
                    }
                    
                    ]}
    assert dump(t) == expected

