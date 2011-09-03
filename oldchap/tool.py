from opster import command
from oldchap.processor import process
import yaml

@command(usage='')
def main():
    config = yaml.load(open('config.yaml').read())
    process(config)
    print "test"
