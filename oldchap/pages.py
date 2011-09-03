from oldchap.extend import page
import jinja2

template = jinja2.Template(open('templates/base.html').read())

@page('post')
def post(files, config):
    articles = map(parse, files)
    with open('build/index.html') as f:
        f.write(template.render(articles=articles, config=config))

def parse(filepath):
    with open(filepath, 'r') as f:
        article = parse(f.read())
    return article
    
