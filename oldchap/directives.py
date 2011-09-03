from oldchap.extend import directive, register_directive

@directive('tags')
def tags(parts, value):
    value = ','.split(value)
    value = map(str.strip, value)
    value.sort()
    parts['tags'] = value

register_directive('title', dict.__setitem__)    
