from src.quotes.quote import Quote

#self.PLUGIN,self.QUEST,self.NPCID,self.CATEGORY,self.TYPE
#self.TOPIC,self.RESPONSE_INDEX,self.FILENAME,self.FULLPATH
#self.TOPIC_TEXT,self.PROMPT,self.RESPONSE_TEXT
class QuoteList(object):
    """docstring for QuoteList"""
    def __init__(self, file):
        super(QuoteList, self).__init__()
        with open(file, 'r') as quotefile:
            next(quotefile)
            for line in quotefile:
                obj = Quote(line)
                #TODO: store

    def find(wordlist):
        pass #TODO: search quotelist for candidates