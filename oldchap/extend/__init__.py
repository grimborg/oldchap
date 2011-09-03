directive_handler = {}
page_handler = {}

def directive(name):
    def decorator(f):
        register_directive(name, f)
        return f
    return decorator

def register_directive(name, f):
    directive_handler[name] = f

def page(name):
    def decorator(f):
        register_page(name, f)
        return f
    return decorator

def register_page(name, f):
    page_handler[name] = f
