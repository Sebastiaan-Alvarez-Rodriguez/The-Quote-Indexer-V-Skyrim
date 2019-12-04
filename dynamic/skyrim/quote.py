from src.quotes.quote import Quote

class SkyQuote(Quote):
    def __init__(self, line):
        super(SkyQuote, self).__init__()
        self.PLUGIN,self.QUEST,self.NPCID,self.CATEGORY,self.TYPE,self.TOPIC,self.RESPONSE_INDEX,self.FILENAME,self.FULLPATH,self.TOPIC_TEXT,self.PROMPT,self.RESPONSE_TEXT = line.split('\t')

    def get_normal_NPC_name(self):
        loc1 = self.NPCID.find('"') +1
        if loc1 == 0: #We found an instance like: DLC2PillarWorkerBandit03 [NPC_:0403CA28]
            if 'bandit' in self.NPCID.lower():
                return 'Bandit'
            if 'sonsnord' in self.NPCID.lower():
                return 'Stormcloack soldier'
            if 'thief' in self.NPCID.lower():
                return 'Thief'
            if 'alikr' in self.NPCID.lower():
                return 'Alikr'
            if 'mercenary' in self.NPCID.lower():
                return 'Mercenary'
            if 'sovngardehero' in self.NPCID.lower():
                return 'Hero of Sovngarde'
            if 'warlock' in self.NPCID.lower():
                return 'Warlock' 
            if 'guard' in self.NPCID.lower():
                return 'Guard'
            if 'hagraven' in self.NPCID.lower():
                return 'hagraven'
            if 'thalmor' in self.NPCID.lower():
                return 'Thalmor soldier'
        loc2 = loc1 + self.NPCID[loc1:].find('"')
        return self.NPCID[loc1:loc2]

    def get_quote(self):
        return str(self)

    def get_url(self):
        if '"' in self.NPCID:
            if 'DLC0' in self.NPCID:
                plugin = 'dawnguard'
            if 'DLC1' in self.NPCID:
                plugin = 'hearthfire'
            elif 'DLC2' in self.NPCID:
                plugin = 'dragonborn'
            else:
                plugin = self.PLUGIN[:-4].lower()
        else:
            plugin = 'skyrim'
        return f"https://en.uesp.net/wiki/{plugin}:{self.get_normal_NPC_name().replace(' ', '_')}"

    def get_extra_info(self):
        return None

    def __hash__(self):
        return hash(f'{self.RESPONSE_TEXT}{self.TOPIC}') #Also could do on topic and response_index

    def __str__(self): 
        return f'"{self.RESPONSE_TEXT}"\n- {self.get_normal_NPC_name()}'