import os

import src.general.general as g
from src.configloader.loader import ConfigLoader

class SettingsReader(object):
    '''Wrapper of ConfigLoader, to read settings-specific values'''

    def __init__(self):
        super(SettingsReader, self).__init__()
        self.ini = ConfigLoader(os.path.join(g.cnf_loc, 'settings.ini'))
    
    # Returns default context
    def get_default_context(self):
        return self.ini['Preferences']['dictionary'].lower()

    # Returns default acceptance score
    def get_acceptance_score(self):
        return self.ini['Precision']['acceptscore']