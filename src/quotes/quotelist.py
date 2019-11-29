from abc import ABC, abstractmethod
from difflib import get_close_matches

from src.quotes.quote import Quote
#https://docs.python.org/3/library/difflib.html#difflib.get_close_matches

#self.PLUGIN,self.QUEST,self.NPCID,self.CATEGORY,self.TYPE
#self.TOPIC,self.RESPONSE_INDEX,self.FILENAME,self.FULLPATH
#self.TOPIC_TEXT,self.PROMPT,self.RESPONSE_TEXT
class QuoteList(ABC):
    def __init__(self):
        super(QuoteList, self).__init__()
        self.map = dict()

    @abstractmethod
    def find(self, wordlist, acceptscore):
        raise NotImplementedError('subclasses must override find()!')

class SkyQuoteList(QuoteList):
    def __init__(self, file):
        super(SkyQuoteList, self).__init__()
        with open(file, 'r') as quotefile:
                next(quotefile)
                for line in quotefile:
                    obj = Quote(line)
                    self.map[obj.RESPONSE_TEXT] = obj

    def find(self, sentence, acceptscore):
        response = get_close_matches(sentence, self.map, n=1, cutoff=0.6)
        return None if len(response)==0 else self.map[response[0]]