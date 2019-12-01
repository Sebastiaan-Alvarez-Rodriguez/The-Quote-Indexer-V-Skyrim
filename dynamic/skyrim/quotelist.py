from difflib import get_close_matches
from dynamic.skyrim.quote import SkyQuote

from src.quotes.quotelist import QuoteList

class QList(QuoteList):
    def __init__(self, file):
        super(QList, self).__init__()
        with open(file, 'r') as quotefile:
                next(quotefile)
                for line in quotefile:
                    obj = SkyQuote(line[:-1])
                    self.map[obj.RESPONSE_TEXT] = obj

    def find(self, sentence, acceptscore):
        response = get_close_matches(sentence, self.map, n=1, cutoff=0.6)
        return None if len(response)==0 else self.map[response[0]]