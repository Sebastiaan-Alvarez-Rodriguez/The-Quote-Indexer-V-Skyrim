import configparser
import os

class ConfigLoader(object):
    ''' Helper to load a config'''

    def __init__(self, path):
        super(ConfigLoader, self).__init__()
        self.config = configparser.ConfigParser()
        self.config.read(path)

    # Get a specific key from a specific config section        
    def get(self, section, key):
        return self.config[section][key]

    def __getitem__(self, key):
        return self.config[key]