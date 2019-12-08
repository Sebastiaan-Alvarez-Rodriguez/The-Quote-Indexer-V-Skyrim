import os

import src.general.general as g
from src.configloader.loader import ConfigLoader

class SettingsReader(object):
    def __init__(self):
        super(SettingsReader, self).__init__()
        self.ini = ConfigLoader(os.path.join(g.cnf_loc, 'settings.ini'))
    
    def get_default_context(self):
        return self.ini['Preferences']['dictionary'].lower()

    def get_acceptance_score(self):
        return self.ini['Precision']['acceptscore']