from abc import ABC, abstractmethod
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