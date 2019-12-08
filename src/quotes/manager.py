import os
import logging

from src.configloader.settings import SettingsReader
from src.dynamicloader.loader import DynamicLoader

from ui.messager import msg, msg_ignore_cancel, Severity

import src.general.general as g

class QuoteManager(object):
    def __init__(self):
        super(QuoteManager, self).__init__()
        self.loader   = DynamicLoader()
        self.settings = SettingsReader()
        self.context  = self.settings.get_default_context()
        self.switch_context(self.context, no_cache=True)

    def find(self, sentence):
        return self.quotelist.find(sentence, self.settings.get_acceptance_score())

    def fun(self, i):
        if i.text().lower() == 'ignore':
            try:
                l = self.loader.load(context, None)
                self.quotelist = l
                self.context = context
            except Exception as e:
                msg(f'Could not load package: {str(e)}', severity=Severity.CRITICAL)

    def switch_context(self, context, no_cache=False):
        if context != self.context or no_cache:
            full_path = os.path.join(g.dat_loc, f'{context}.dat')
            if not os.path.isfile(full_path):
                msg_ignore_cancel(f'We did not find a dataset for this item (expected: {full_path}. Ignore?', self.fun)
            else:
                self.quotelist = self.loader.load(context, full_path)
                self.context = context
    
    def get_contexts(self):
        return [x for x in self.loader.options]