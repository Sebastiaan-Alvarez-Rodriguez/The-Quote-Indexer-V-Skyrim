import configparser
import os


class Config(object):
    """docstring for Config"""
    def __init__(self, path):
        super(Config, self).__init__()
        self.config = configparser.ConfigParser()
        self.config.read(path)
        
    def get(self, section, key):
        return self.config[section][key]

    def __getitem__(self, key):
        return self.config[key]