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


def test_resourceId():
    class Foo(Resource):
        def __init__(self, type, name):
            self.type = type
            self.name = name

    f = Foo("t1", "n1")
    assert str(f.resourceId()), "resourceId('t1', 'n1')"

def test_dump():

    assert dump("foo") == "foo"
    assert dump(2) == 2

    t = Template()
    d = dump(t)
    expected = {'$schema': 'https://schema.management.azure.com/schemas/2015-01-01/deploymentTemplate.json#', 
                'contentVersion': '1.0.0.0',
                'resources': []}
    assert d == expected
