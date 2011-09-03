from oldchap import extend
def process(config):
    map(__import__, config['extensions'])
    p = extend.page_handler['post'](['content/a.rst'], {})
    
