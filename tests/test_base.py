from tropo.base import Template, Resource

def test_template():
    t = Template()
    d = t._asdict()
    expected = {'$schema': 'https://schema.management.azure.com/schemas/2015-01-01/deploymentTemplate.json#', 
                'contentVersion': '1.0.0.0'}
    assert d == expected

def test_resource():
    t = Resource()
    d = t._asdict()
    expected = {}
    assert d == expected


