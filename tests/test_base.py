import json
from tropo.base import Template, Resource, dump

def test_template():
    t = Template()
    d = t._asdict()
    expected = {'$schema': 'https://schema.management.azure.com/schemas/2015-01-01/deploymentTemplate.json#', 
                'contentVersion': '1.0.0.0',
                'resources': []}
    assert d == expected

    s = str(t)
    assert s == json.dumps(t._asdict(), indent=2)

def test_resource():
    t = Resource()
    d = t._asdict()
    expected = {}
    assert d == expected


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
