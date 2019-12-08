import os
import importlib
import importlib.util

import src.general.general as g

class DynamicLoader(object):
    
    def __init__(self):
        super(DynamicLoader, self).__init__()
        options_pre = os.listdir(g.dyn_loc)
        if 'skyrim' in options_pre:
            options_pre.remove('skyrim')
            options_pre.insert(0,'skyrim')

        self.options = dict()
        for item in options_pre:
            full_path = os.path.join(g.dyn_loc,item)
            if os.path.isdir(full_path) and 'quotelist.py' in os.listdir(full_path):
                self.options[item] = os.path.join(full_path, 'quotelist.py')

    def load(self, name, *args):
        if name in self.options:
            path = self.options[name]
            print(f'Importing {name} on path: {path}')
            spec = importlib.util.spec_from_file_location(f'{name}.dm', path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            return module.QList(*args)
        else:
            raise KeyError(f"There is no key named '{name}'. Available: {str(self.options)}")