from abc import ABC, abstractmethod

class QuoteList(ABC):
    def __init__(self):
        super(QuoteList, self).__init__()
        self.map = dict()

    @abstractmethod
    def find(self, wordlist, acceptscore):
        raise NotImplementedError('subclasses must override find()!')