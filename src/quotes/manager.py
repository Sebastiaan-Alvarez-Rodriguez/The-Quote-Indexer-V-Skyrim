import os

from src.quotes.storage.config import Config
from src.dynamicloader.loader import DynamicLoader

import src.general.general as g

class QuoteManager(object):            
    configpath = os.path.join(g.abs_loc, 'configs')

    def __init__(self):
        super(QuoteManager, self).__init__()
        self.loader   = DynamicLoader()
        self.prefs    = Config(os.path.join(self.configpath, 'prefs.ini'))
        self.settings = Config(os.path.join(self.configpath, 'settings.ini'))
        self.context  = self.prefs['DEFAULT']['dictionary'].lower()
        self.switch_context(self.context, no_cache=True)

    def find(self, sentence):
        return self.quotelist.find(sentence, self.settings['Precision']['acceptscore'])

    def switch_context(self, context, no_cache=False):
        if context != self.context or no_cache:
            self.context = context
            full_path = os.path.join(g.abs_loc,self.settings['Locations'][context])
            self.quotelist = self.loader.load(context, full_path)
        