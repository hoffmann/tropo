import json

class AzureObject(object):
    _attribute_map = {}
    def _asdict(self):
        record = {}
        for k, d in self._attribute_map.items():
            if hasattr(self, k) and (getattr(self, k) or d.get("required", False)):
                obj = getattr(self, k)
                if isinstance(obj, AzureObject):
                    value = obj._asdict()
                elif isinstance(obj, list):
                    value = []
                    for o in obj:
                        if isinstance(o, AzureObject):
                            value.append(o._asdict())
                        else:
                            value.append(o)
                else:
                    value = obj
                
                key = d["key"]
                parts = key.split(".")
                if len(parts) == 2:
                    sub, key = parts
                    if not sub in record:
                        record[sub] = {}
                    record[sub][key] = value
                else:
                    record[key] = value
        return record


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
        return json.dumps(self._asdict(), indent=2)


class Resource(AzureObject):
    pass

class SubResource(AzureObject):
    pass
