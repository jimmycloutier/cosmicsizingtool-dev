import json
from types import SimpleNamespace as Namespace

#Convert JSON to Object
def json2obj(data) : return json.loads(data, object_hook=lambda d: Namespace(**d))