import random

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.sanity = 100
        self.ammo = 50
        self.medical_supplies = 3
        self.inventory = []
        self.skills = {"combat": 1, "medical": 1, "technical": 1}

class NPC:
    def __init__(self, name, role, personality, backstory):
        self.name = name
        self.role = role
        self.health = 100
        self.trust = 50
        self.alive = True
        self.skills = self.assign_skills(role)
        self.personality = personality
        self.backstory = backstory

    def assign_skills(self, role):
        if role == "Medico":
            return {"combat": 1, "medical": 3, "technical": 2}
        elif role == "Soldato":
            return {"combat": 3, "medical": 1, "technical": 2}
        elif role == "Tecnico":
            return {"combat": 1, "medical": 1, "technical": 3}
        else:
            return {"combat": 1, "medical": 1, "technical": 1}

    def act(self, situation):
        if situation == "combat":
            return self.combat_action()
        elif situation == "medical":
            return self.medical_action()
        elif situation == "technical":
            return self.technical_action()

    def combat_action(self):
        if self.skills["combat"] > 2:
            return f"{self.name} combatte abilmente contro le entità!"
        elif self.skills["combat"] > 1:
            return f"{self.name} tenta di respingere le entità."
        else:
            return f"{self.name} cerca di nascondersi dal pericolo."

    def medical_action(self):
        if self.skills["medical"] > 2:
            return f"{self.name} fornisce cure esperte."
        elif self.skills["medical"] > 1:
            return f"{self.name} offre un primo soccorso di base."
        else:
            return f"{self.name} cerca di aiutare come può, ma non è molto efficace."

    def technical_action(self):
        if self.skills["technical"] > 2:
            return f"{self.name} ripara abilmente i sistemi danneggiati."
        elif self.skills["technical"] > 1:
            return f"{self.name} tenta di effettuare alcune riparazioni."
        else:
            return f"{self.name} cerca di capire come funzionano i sistemi."

    def get_dialogue(self):
        return random.choice(self.personality["dialogues"])

npcs = [
    NPC("Dr. Sarah", "Medico", 
        {"trait": "Compassionevole ma esausta",
         "dialogues": ["Dobbiamo prenderci cura l'uno dell'altro per sopravvivere qui.",
                       "Ho visto cose che nessun medico dovrebbe mai vedere...",
                       "A volte mi chiedo se stiamo davvero aiutando o solo prolungando l'inevitabile."]},
        "Ex chirurgo d'emergenza, intrappolata nelle Backrooms durante un turno di notte."),
    
    NPC("Capitano Mike", "Soldato",
        {"trait": "Determinato ma paranoico",
         "dialogues": ["Restiamo vigili. Le entità potrebbero attaccare in qualsiasi momento.",
                       "Ho combattuto in guerre, ma niente mi ha preparato per questo inferno.",
                       "Non fidarti di nessuno completamente. Questo posto cambia le persone."]},
        "Veterano di guerra, entrato nelle Backrooms durante una missione di ricognizione."),
    
    NPC("Emily", "Paziente",
        {"trait": "Spaventata ma intuitiva",
         "dialogues": ["Sento che le pareti ci osservano... non siamo soli qui.",
                       "Prima ero solo una studentessa, ora sono una sopravvissuta.",
                       "Ho dei sogni strani... credo che stiano cercando di dirci qualcosa."]},
        "Studentessa universitaria, finita nelle Backrooms dopo essersi persa nel campus."),
    
    NPC("Tom", "Tecnico",
        {"trait": "Curioso ma cauto",
         "dialogues": ["Questo posto sfida ogni legge della fisica che conosco.",
                       "Se riuscissimo a capire come funziona, forse potremmo controllarlo.",
                       "Ho una teoria su come uscire, ma è rischiosa..."]},
        "Ingegnere aerospaziale, entrato nelle Backrooms durante un esperimento fallito."),
    
    NPC("Zoe", "Esploratore",
        {"trait": "Avventurosa ma solitaria",
         "dialogues": ["Ho mappato gran parte di questo livello, ma cambia continuamente.",
                       "Ci sono altri livelli là fuori, alcuni bellissimi, altri mortali.",
                       "A volte penso che sia meglio restare in movimento che cercare una via d'uscita."]},
        "Ex guida di trekking, entrata nelle Backrooms durante un'escursione in solitaria."),
    
    NPC("Vecchio Jack", "Sopravvissuto",
        {"trait": "Saggio ma enigmatico",
         "dialogues": ["Ho visto questo posto cambiare più volte di quante possa contare.",
                       "Le risposte che cerchi sono dentro di te, ragazzo.",
                       "Non tutto ciò che sembra un mostro lo è, e non tutto ciò che sembra umano lo è."]},
        "Presenza misteriosa, sembra essere nelle Backrooms da più tempo di chiunque altro.")
]