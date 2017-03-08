import json
from tropo.base import Template, Resource, dump, dumps

def test_template():
    t = Template()
    expected = {'$schema': 'https://schema.management.azure.com/schemas/2015-01-01/deploymentTemplate.json#', 
                'contentVersion': '1.0.0.0',
                'resources': []}
    assert dump(t) == expected


def test_resource():
    t = Resource()
    expected = {}
    assert dump(t) == expected


def test_dump():

    assert dump("foo") == "foo"
    assert dump(2) == 2

    t = Template()
    d = dump(t)
    expected = {'$schema': 'https://schema.management.azure.com/schemas/2015-01-01/deploymentTemplate.json#', 
                'contentVersion': '1.0.0.0',
                'resources': []}
    print(json.dumps(d, indent=2))
    assert d == expected
