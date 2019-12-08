import os

from src.quotes.quote import Quote
import src.general.general as g

class SkyQuote(Quote):    
    def __init__(self, line):
        super(SkyQuote, self).__init__()
        self.PLUGIN,self.QUEST,self.NPCID,self.CATEGORY,self.TYPE,self.TOPIC,self.RESPONSE_INDEX,self.FILENAME,self.FULLPATH,self.TOPIC_TEXT,self.PROMPT,self.RESPONSE_TEXT = line.split('\t')

    def get_normal_NPC_name(self):
        loc1 = self.NPCID.find('"') +1
        npc_id_lower = self.NPCID.lower()
        if loc1 == 0:
            if 'bandit' in npc_id_lower:
                return 'Bandit'
            if 'sonsnord' in npc_id_lower:
                return 'Stormcloack soldier'
            if 'thief' in npc_id_lower:
                return 'Thief'
            if 'alikr' in npc_id_lower:
                return 'Alikr'
            if 'mercenary' in npc_id_lower:
                return 'Mercenary'
            if 'sovngardehero' in npc_id_lower:
                return 'Hero of Sovngarde'
            if 'warlock' in npc_id_lower:
                return 'Warlock' 
            if 'guard' in npc_id_lower:
                return 'Guard'
            if 'hagraven' in npc_id_lower:
                return 'hagraven'
            if 'thalmor' in npc_id_lower:
                return 'Thalmor soldier'
            else:
                return 'Unkown'
        loc2 = loc1 + self.NPCID[loc1:].find('"')
        return self.NPCID[loc1:loc2]

    def get_quote(self):
        return str(self)

    def get_url(self):
        if '"' in self.NPCID:
            if 'DLC0' in self.NPCID:
                plugin = 'skyrim' #'hearthfire'
            elif 'DLC1' in self.NPCID:
                plugin = 'skyrim' #'dawnguard'
            elif 'DLC2' in self.NPCID:
                plugin = 'dragonborn'
            else:
                plugin = 'skyrim'
        else:
            plugin = self.PLUGIN[:-4].lower()
            if plugin == 'dawnguard':
                plugin = 'skyrim'
            elif plugin == 'hearthfires':
                plugin = 'skyrim'
        if self.get_normal_NPC_name() != 'Unkown':
            return f"https://en.uesp.net/wiki/{plugin}:{self.get_normal_NPC_name().replace(' ', '_')}"
        else:
            return None

    def get_normal_quest_name(self):
        loc1 = self.QUEST.find('"')+1    
        loc2 = loc1 + self.QUEST[loc1:].find('"')
        return self.QUEST[loc1:loc2]

    def get_quest_info(self):
        quest_lower = self.QUEST.lower()
        if not '"' in self.QUEST:
            if 'tutorial' in quest_lower:
                return f'while following a tutorial on {self.QUEST[8:]}'
            elif 'rumor' in quest_lower:
                return 'when finding rumors'
            elif 'housepurchase' in quest_lower:
                return 'if you buy (interior for) a house'
        else:
            if 'skooma dealer' in quest_lower:
                return 'when speaking with a drug dealing Khajit'
            elif 'courier delivering an important message' in quest_lower:
                return 'if you speak with a running courier'
            elif 'taunting adventurer' in quest_lower:
                return 'when you encounter a taunting adventurer'
            elif 'adventurer on the way to' in quest_lower:
                return 'if you speak with an encountered fellow adventurer'
            elif 'nobles traveling with bodyguard' in quest_lower:
                return 
            elif 'thieves guild pre-quest handler' in quest_lower:
                return f'just before getting a quest from the Thieves Guild'
            elif 'thieves guild dialogue' in quest_lower:
                return 'when speaking with Thieves Guild members'
            elif 'post quest handler' in quest_lower:
                if 'beyond death' in quest_lower:
                    return f'after completing "Beyond Death" quest' #and speaking with Valerica
            elif 'bandits dressed as imperial soldiers' in quest_lower:
                return 'when you meet those bandits dressed as imperial soldiers'
            elif 'rumor' in quest_lower:
                return 'when finding rumors'
            elif 'twilight sepulcher dialogue' in quest_lower:
                return 'when near the Twilight Sepulcher'
            elif 'generic dialogue' in quest_lower:
                return 'on a regular basis, as it is generic dialogue'
            elif 'hide and seek' in quest_lower:
                return 'when children are playing hide and seek nearby'
            elif 'kid games' in quest_lower:
                return 'when you get involved in plaing games with kids'
            elif 'wizard duel' in quest_lower:
                return 'when a mage wants to duel you'
            elif 'magic student' in quest_lower:
                return 'if a magic students seeks you out'
            elif 'shout - guard says stop' in quest_lower:
                return 'when a guard is telling you to stop shouting in a city'
            elif 'scene' in quest_lower:
                return None
            elif 'dialogue' in quest_lower:
                return None
            else:
                return f'On quest "{self.get_normal_quest_name()}"'

    def get_extra_info(self):
        string = ''
        qstr = self.get_quest_info()
        if qstr != None:
            string += f'You can hear this dialogue {qstr}.'
        if self.CATEGORY == 'Topic' and self.TYPE=='CUST':
            pass
        elif self.CATEGORY == 'Combat':
            if self.TYPE == 'TAUT':
                string += 'Enemies taunt you with this quote.'
            elif self.TYPE == 'STFN':
                string += 'But only if you are spotted stealing something.'
            elif self.TYPE == 'PICN':
                string += 'If you are detected while pickpocketing, that is.'
            elif self.TYPE == 'MUCN':
                string += 'You will hear this when you are spotted while murdering someone.'
            elif self.TYPE == 'HIT_':
                string += 'You can hear this if you hit an enemy.'
            elif self.TYPE == 'FLEE':
                string += 'You can hear this when an enemy has low health and decides to flee.'
            elif self.TYPE == 'DETH':
                string += 'You can hear this when you kill an enemy.'
            elif self.TYPE == 'BLOC':
                string += 'When an enemy blocks an attack, they may say this.'
            elif self.TYPE == 'ATCK':
                string += 'When an enemy charges, they may shout this.'
            elif self.TYPE == 'BLED':
                string += 'When an enemy has bleeding effect, you may hear this.'
            elif self.TYPE == 'ACYI':
                string += 'When the player yields in combat and the enemy accepts, you may hear this.'
            elif self.TYPE == 'TRES':
                string += 'When the player is getting close to an enemy camp or fortification, potential enemies will say this.'
            elif self.TYPE == 'ASSA':
                string += 'When the player is detected "assaulting" someone (attacking passive npc), you may hear this.'
            elif self.TYPE == 'BASH':
                string += 'If an enemy performs a bashing attack, they will shout this.'
            # Detection NOTA
        elif self.CATEGORY == 'Detection':
            if self.TYPE == 'NOTA':
                string += 'Enemies will say this if the player is sneaking, and the enemies notice something.'
        elif self.CATEGORY == 'Miscellaneous':
            if self.TYPE == 'NOTI':
                string += "NPC's will say this if they find a dead body"
        return string

    def get_audio_path(self):
        if '"no voice".xwm' in self.FULLPATH:
            return None
        #Data\Sound\Voice\Skyrim.esm\MaleNord\MQ102__000D50EE_1.xwm
        #Skyrim.esm\MaleNord\MQ102__000D50EE_1.
        loc = os.path.join(g.snd_loc,'skyrim',self.FULLPATH[17:-3].lower().replace('\\', os.path.sep) + 'wav')
        if not os.path.isfile(loc):
            print(f'Expected audio file not found! Path: {loc}')
        return loc if os.path.isfile(loc) else None

    def __hash__(self):
        return hash(f'{self.RESPONSE_TEXT}{self.TOPIC}')

    def __str__(self): 
        return f'"{self.RESPONSE_TEXT}"\n- {self.get_normal_NPC_name()}'