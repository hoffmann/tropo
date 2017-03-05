import json

from tropo import Template

t = Template(resources=[])

print(json.dumps(t._asdict(), indent=2))
