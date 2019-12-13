import os
import logging

from src.configloader.settings import SettingsReader
from src.dynamicloader.loader import DynamicLoader

from ui.messager import msg, msg_ignore_cancel, Severity

import src.general.general as g

class QuoteManager(object):
    '''Manages currently loaded (dataset) context, and handles switching to other datasets'''

    def __init__(self):
        super(QuoteManager, self).__init__()
        self.loader   = DynamicLoader()
        self.settings = SettingsReader()
        self.context  = self.settings.get_default_context()
        self.switch_context(self.context, no_cache=True)

    # Find a sentence in the currently loaded context
    def find(self, sentence):
        return self.quotelist.find(sentence, self.settings.get_acceptance_score())

    # Function to receive callbacks from calls to 'msg_ignore_cancel'
    def fun(self, i):
        if i.text().lower() == 'ignore':
            try:
                l = self.loader.load(context, None)
                self.quotelist = l
                self.context = context
            except Exception as e:
                msg(f'Could not load package: {str(e)}', severity=Severity.CRITICAL)

    # Switches context to another context. Set no_cache to True if you want the dataset to be read in, even if it is already active
    def switch_context(self, context, no_cache=False):
        if context != self.context or no_cache:
            full_path = os.path.join(g.dat_loc, f'{context}.dat')
            if not os.path.isfile(full_path):
                msg_ignore_cancel(f'We did not find a dataset for this item (expected: {full_path}. Ignore?', self.fun)
            else:
                self.quotelist = self.loader.load(context, full_path)
                self.context = context
    
    # Return available contexts to load from
    def get_contexts(self):
        return [x for x in self.loader.options]

    # Return the current context
    def get_current_context(self):
        return self.context