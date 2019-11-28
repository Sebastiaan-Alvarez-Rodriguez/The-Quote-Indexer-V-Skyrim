import configparser

# https://docs.python.org/3.4/library/configparser.html
def read_path(path):
    config = configparser.ConfigParser()
    config.read(path)
    if 'Dictionary Locations' not in config.sections():
        raise KeyError(f'{path} does not contain "Dictionary Locations" section')
    return config['Dictionary Locations']

# Returns the different keys we can read. e.g: Skyrim = foo/bar.tsv returns ['Skyrim']
def read_options(path):
    return [x for x in read_path(path)]

# Returns the path for a key. e.g: Skyrim = foo/bar.tsv returns ['Skyrim']
def read_location(path,key):
    tmp = read_path(path)[key]
    if key not in tmp:
        return KeyError(f'Error: "{key}" not found in {path}')
    return tmp[key]