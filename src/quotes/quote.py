from abc import ABC, abstractmethod
class Quote(ABC):
    def __init__(self):
        super(Quote, self).__init__()
        self.map = dict()

    @abstractmethod
    def get_quote(self):
        raise NotImplementedError('subclasses must override get_quote()!')

    @abstractmethod
    def get_url(self):
        raise NotImplementedError('subclasses must override get_url()!')

    @abstractmethod
    def get_extra_info(self):
        raise NotImplementedError('subclasses must override get_extra_info()!')

    @abstractmethod
    def get_audio_path(self):
        raise NotImplementedError('subclasses must override get_audio_path()!')