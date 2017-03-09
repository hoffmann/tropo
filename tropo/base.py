import json

def dump(obj):
    if isinstance(obj, AzureObject):
        res = {}
        for k, d in obj._attribute_map.items():
            if hasattr(obj, k) and (getattr(obj, k) or d.get("required", False)):
                value = getattr(obj, k)
                key = d["key"]
                parts = key.split(".")
                if len(parts) == 2:
                    sub, key = parts
                    if not sub in res:
                        res[sub] = {}
                    res[sub][key] = dump(value)
                else:
                    res[key] = dump(value)
    elif isinstance(obj, TemplateFunction):
        res = "[{}]".format(obj)
    elif isinstance(obj, dict):
        res = {key: dump(value) for key, value in obj.items()}
    elif isinstance(obj, list):
        res = [dump(value) for value in obj]
    else:
        res = obj
    return res

def dumps(obj):
    return json.dumps(dump(obj), indent=2)

class AzureObject(object):
    _attribute_map = {}


class Template(AzureObject):
    _attribute_map = {"schema": {"key": "$schema", "type": "str"},
                      "contentVersion": {"key": "contentVersion", "type": "str"},
                      "parameters": {"key": "parameters", "type": "[]"},
                      "variables": {"key": "variables", "type": "[]"},
                      "resources": {"key": "resources", "type": "[]", "required": True}
                      }

    def __init__(self, parameters=None, variables=None, resources=None, outputs=None):
        self.schema = "https://schema.management.azure.com/schemas/2015-01-01/deploymentTemplate.json#"
        self.contentVersion = "1.0.0.0"
        if parameters is None:
            parameters = {}
        self.parameters = parameters
        if variables is None:
            variables = {}
        self.variables = variables
        if resources is None:
            resources = []
        self.resources = resources
        if outputs is None:
            outputs = {}
        self.outputs = outputs

    def __str__(self):
        return dumps(t)


class Resource(AzureObject):
    pass

class SubResource(AzureObject):
    pass


class TemplateFunction(object):
    pass
