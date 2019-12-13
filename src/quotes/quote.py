from abc import ABC, abstractmethod

class Quote(ABC):
    '''Abstract object, where all dynamic loader quotes should inherit from'''

    def __init__(self):
        super(Quote, self).__init__()

    # Return a human-readable quote
    @abstractmethod
    def get_quote(self):
        raise NotImplementedError('subclasses must override get_quote()!')

    # Return a url, or None
    @abstractmethod
    def get_url(self):
        raise NotImplementedError('subclasses must override get_url()!')

    # Return extra info about the quote, or None
    @abstractmethod
    def get_extra_info(self):
        raise NotImplementedError('subclasses must override get_extra_info()!')

    # Return a path to an audio file, or None
    @abstractmethod
    def get_audio_path(self, basepath):
        raise NotImplementedError('subclasses must override get_audio_path()!')