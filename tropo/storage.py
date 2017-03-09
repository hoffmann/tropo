from tropo.base import Resource, SubResource


class StorageAccount(Resource):
    """Microsoft.Storage/storageAccounts

    Args:
        name (str): The name of the resource
        location (str): The location of the resource
        description (str): a description of the resource
        tags: ({str}): a dictionary of tags
        dependsOn: ([]): a list of resources
        sku (Sku):  Required. Gets or sets the sku type.
        kind (str):  Required. Indicates the type of storage account. Possible values include:
            'Storage', 'BlobStorage'
        customDomain (CustomDomain):  User domain assigned to the storage account. Name is the CNAME source. Only one
            custom domain is supported per storage account at this time. To
            clear the existing custom domain, use an empty string for the custom
            domain name property.
        encryption (Encryption):  Provides the encryption settings on the account. If left unspecified the account
            encryption settings will remain. The default setting is unencrypted.
        accessTier (str):  Required for StandardBlob accounts. The access tier used for billing. Access
            tier cannot be changed more than once every 7 days (168 hours).
            Access tier cannot be set for StandardLRS, StandardGRS,
            StandardRAGRS, or PremiumLRS account types. Possible values include:
            'Hot', 'Cool'  

    """

    type = 'Microsoft.Storage/storageAccounts'
    apiVersion = '2016-01-01'
    
    _attribute_map = {
        'apiVersion': {'key': 'apiVersion', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'tags': {'key': 'tags', 'type': 'str'},
        'dependsOn': {'key': 'dependsOn', 'type': '[str]'},
        'sku': {'key': 'sku', 'type': 'Sku', 'required': True},
        'kind': {'key': 'kind', 'type': 'str', 'required': True},
        'customDomain': {'key': 'properties.customDomain', 'type': 'CustomDomain'},
        'encryption': {'key': 'properties.encryption', 'type': 'Encryption'},
        'accessTier': {'key': 'properties.accessTier', 'type': 'str'}   
    }

    def __init__(self, name, location=None, description=None, tags=None, dependsOn=None, sku=None, kind=None, customDomain=None, encryption=None, accessTier=None):
        self.name = name
        if location is None:
            location = '[resourceGroup().location]'
        self.location = location
        self.description = description
        self.tags = tags
        self.dependsOn = dependsOn
        self.sku = sku
        self.kind = kind
        self.customDomain = customDomain
        self.encryption = encryption
        self.accessTier = accessTier
        
class Sku(SubResource):
    """The SKU of the storage account.

    Args:
        name (str):  Gets or sets the sku name. Required for account creation, optional for update.
            Note that in older versions, sku name was called accountType.
            Possible values include: 'Standard_LRS', 'Standard_GRS',
            'Standard_RAGRS', 'Standard_ZRS', 'Premium_LRS'

    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str', 'required': True}
    }

    def __init__(self, name=None):
        self.name = name
        
class CustomDomain(SubResource):
    """The custom domain assigned to this storage account. This can be set via Update.

    Args:
        name (str):  Gets or sets the custom domain name. Name is the CNAME source.
        useSubDomain (bool):  Indicates whether indirect CName validation is enabled. Default value is false.
            This should only be set on updates

    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str', 'required': True},
        'useSubDomain': {'key': 'useSubDomain', 'type': 'bool'}
    }

    def __init__(self, name=None, useSubDomain=None):
        self.name = name
        self.useSubDomain = useSubDomain
        