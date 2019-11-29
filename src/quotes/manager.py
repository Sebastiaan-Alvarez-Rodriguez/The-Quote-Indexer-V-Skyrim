import os
from enum import Enum

from src.quotes.storage.config import Config

from src.quotes.quotelist import SkyQuoteList
import src.general.general as g

class QuoteManager(object):

    class Context(Enum):
        SKYRIM = 0
        OTHER  = 1
            
    configpath = os.path.join(g.abs_loc, 'configs')

    def __init__(self):
        super(QuoteManager, self).__init__()
        self.prefs    = Config(os.path.join(self.configpath, 'prefs.ini'))
        self.settings = Config(os.path.join(self.configpath, 'settings.ini'))
        self.context  = self.Context[self.prefs['DEFAULT']['dictionary'].upper()]
        self.switch_context(self.context, no_cache=True)

    def find(self, sentence):
        return self.quotelist.find(sentence, self.acceptscore)

    def switch_context(self, context, no_cache=False):
        if context != self.context or no_cache:
            self.context = context
            full_path = os.path.join(g.abs_loc,self.settings['Locations'][context.name])
            if context == self.Context.SKYRIM:
                self.quotelist = SkyQuoteList(full_path)
            elif context == OTHER:
                raise NotImplementedError('There is no')