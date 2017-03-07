from tropo.base import Resource


class StorageAccount(Resource):
    """Microsoft.Storage/storageAccounts

    Args:
        name (str): The name of the resource
        location (str): The location of the resource
        description (str): a description of the resource
        tags: ({str}): a dictionary of tags
        dependsOn: ([]): a list of resources
        sku: todo
        kind: todo  

    """

    _type = 'Microsoft.Storage/storageAccounts'
    _apiVersion = '2016-01-01'
    _attribute_map = {
        '_apiVersion': {'key': 'apiVersion', 'type': 'str'},
        '_type': {'key': 'type', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'dependsOn': {'key': 'dependsOn', 'type': '[]'},
        'sku': {'key': 'sku', 'type': '_'},
        'kind': {'key': 'kind', 'type': '_'}   
    }

    def __init__(self, name, location=None, description=None, tags=None, dependsOn=None, sku=None, kind=None):
        self.name = name
        if location is None:
            location = '[resourceGroup().location]'
        self.location = location
        self.description = description
        self.tags = tags
        self.dependsOn = dependsOn
        self.sku = sku
        self.kind = kind
        

class Sku(Resource):
    """The SKU of the storage account.

    Args:
        name (string|str):  Gets or sets the sku name. Required for account creation, optional for update.
            Note that in older versions, sku name was called accountType.
            Possible values include: 'Standard_LRS', 'Standard_GRS',
            'Standard_RAGRS', 'Standard_ZRS', 'Premium_LRS' 
    """
    _attribute_map = {
        'name': {'key': 'name', 'type': 'string|str', 'required': True}   
    }

    def __init__(self, name=None):
        self.name = name

