class Quote(object):
    def __init__(self, line):
        super(Quote, self).__init__()
        self.PLUGIN,self.QUEST,self.NPCID,self.CATEGORY,self.TYPE,self.TOPIC,self.RESPONSE_INDEX,self.FILENAME,self.FULLPATH,self.TOPIC_TEXT,self.PROMPT,self.RESPONSE_TEXT = line.split('\t')

    def __hash__(self):
        return hash(f'{self.RESPONSE_TEXT}{self.TOPIC}') #Also could do on topic and response_index

    def __str__(self):
        return f'"{self.RESPONSE_TEXT}" - {self.NPCID}'