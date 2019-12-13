from abc import ABC, abstractmethod

class QuoteList(ABC):
    '''Abstract object, where all dynamic loaders should inherit from'''

    def __init__(self):
        super(QuoteList, self).__init__()

    # Called when we want to find a certain sentence in the dataset of this file. Acceptscore is a
    # float in [0,1], specifying how much correlation there must be with a candidate quote
    @abstractmethod
    def find(self, sentence, acceptscore):
        raise NotImplementedError('subclasses must override find()!')