from difflib import get_close_matches

from src.quotes.quotelist import QuoteList
from src.quotes.quote import Quote

class OtherQuote(Quote):
    def __init__(self, line):
        self.QUOTE,self.PERSON = line.split('\t')


    def get_quote(self):
        return str(self)

    def get_url(self):
        return None

    def get_extra_info(self):
        return None

    def get_audio_path(self, basepath):
        return None

    def __hash__(self):
        return hash(self.QUOTE)

    def __str__(self):
        return f'"{self.QUOTE}"\n- {self.PERSON}'


class QList(QuoteList):
    def __init__(self, file):
        super(QList, self).__init__()
        self.map = dict()
        with open(file, 'r') as quotefile:
                next(quotefile)
                for line in quotefile:
                    obj = OtherQuote(line[:-1])
                    self.map[obj.QUOTE] = obj

    def find(self, sentence, acceptscore):
        response = get_close_matches(sentence, self.map, n=1, cutoff=0.6)
        return None if len(response)==0 else self.map[response[0]]