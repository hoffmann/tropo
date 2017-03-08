from tropo.base import TemplateFunction


def quote(e):
    if isinstance(e, TemplateFunction):
        return str(e)
    elif isinstance(e, str):
        return "'{}'".format(e)
    else:
        return str(e)

class _raw(TemplateFunction):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return self.value 


class parameters(TemplateFunction):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return "parameters('{}')".format(self.name)

class variables(TemplateFunction):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return "variables('{}')".format(self.name)

class uniqueString(TemplateFunction):
    def __init__(self, *args):
        self.args = args
    def __str__(self):
        return "uniqueString({})".format(", ".join(map(quote, self.args)))


class concat(TemplateFunction):
    def __init__(self, *args):
        self.args = args
    def __str__(self):
        return "concat({})".format(", ".join(map(quote, self.args)))

class resourceId(TemplateFunction):
    def __init__(self, type_, name):
        self.type_ = type_
        self.name = name
    def __str__(self):
        return "resourceId({}, {})".format(quote(self.type_), quote(self.name))

