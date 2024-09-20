import random
from combat import Combat

class Player:
    def __init__(self, name):
        self.name = name
        self.sanity = 100
        self.corruption = 0
        self.inventory = []
        self.current_location = "Portale del Void"
        self.knowledge = 0
        self.escaped = False
        self.abilities = {
            "Focalizzazione Mentale": self.mental_focus,
            "Purificazione del Void": self.void_purification,
            "Risonanza Eldritch": self.eldritch_resonance
        }

    def is_alive(self):
        return self.sanity > 0

    def is_fully_corrupted(self):
        return self.corruption >= 100

    def has_escaped(self):
        return self.escaped

    def add_item(self, item):
        if len(self.inventory) < 5:
            self.inventory.append(item)
            print(f"Hai acquisito: {item.name}")
        else:
            print("Il peso del Void ti opprime. Non puoi portare altri oggetti.")

    def remove_item(self, item):
        self.inventory.remove(item)

    def show_inventory(self):
        print("I tuoi possedimenti corrotti:")
        for item in self.inventory:
            print(f"- {item.name}: {item.description}")

    def use_item(self, item_name):
        for item in self.inventory:
            if item.name.lower() == item_name.lower():
                item.use(self)
                self.remove_item(item)
                return
        print("Quell'oggetto esiste solo nella tua mente distorta.")

    def rest(self):
        if random.random() < 0.7:
            sanity_gain = random.randint(5, 15)
            corruption_loss = random.randint(1, 5)
            self.sanity += sanity_gain
            self.corruption -= corruption_loss
            print(f"Trovi un momento di pace nell'caos. Recuperi {sanity_gain} sanità e perdi {corruption_loss} corruzione.")
        else:
            sanity_loss = random.randint(10, 20)
            self.sanity -= sanity_loss
            print(f"I tuoi sogni sono infestati da visioni del Void. Perdi {sanity_loss} sanità.")

    def move_to(self, location):
        self.current_location = location
        print(f"Ti avventuri verso: {location}")
        self.sanity -= random.randint(1, 5)
        self.corruption += random.randint(1, 3)

    def show_status(self):
        print(f"Sanità mentale: {self.sanity}, Corruzione: {self.corruption}, Conoscenza del Void: {self.knowledge}")

    def meditate(self):
        print("Cerchi di focalizzare la tua mente frammentata...")
        if random.random() < 0.5:
            sanity_gain = random.randint(5, 15)
            self.sanity += sanity_gain
            self.knowledge += 1
            print(f"Raggiungi una comprensione più profonda del Void. Guadagni {sanity_gain} sanità e 1 punto conoscenza.")
        else:
            sanity_loss = random.randint(5, 15)
            corruption_gain = random.randint(1, 5)
            self.sanity -= sanity_loss
            self.corruption += corruption_gain
            print(f"Le verità del Void ti sopraffanno. Perdi {sanity_loss} sanità e guadagni {corruption_gain} corruzione.")

    def apply_environmental_effect(self, location):
        effect = location.environmental_effect()
        self.sanity += effect['sanity']
        self.corruption += effect['corruption']
        print(f"L'ambiente di {location.name} influenza il tuo essere.")
        if effect['sanity'] < 0:
            print(f"Senti la tua mente vacillare. Perdi {-effect['sanity']} sanità.")
        if effect['corruption'] > 0:
            print(f"La corruzione si insinua più a fondo. Guadagni {effect['corruption']} corruzione.")

    def calculate_damage(self):
        base_damage = 15
        knowledge_bonus = self.knowledge * 2
        return random.randint(base_damage, base_damage + knowledge_bonus)

    def take_damage(self, damage):
        self.sanity -= damage
        if self.sanity < 0:
            self.sanity = 0

    def defend(self):
        self.sanity += 10
        print("Ti concentri per difenderti. Recuperi 10 punti sanità.")

    def show_abilities(self):
        print("Le tue abilità:")
        for ability in self.abilities:
            print(f"- {ability}")

    def use_ability(self, ability_name, target):
        if ability_name in self.abilities:
            self.abilities[ability_name](target)
        else:
            print("Abilità non trovata.")

    def mental_focus(self, target):
        sanity_gain = random.randint(20, 40)
        self.sanity += sanity_gain
        print(f"Ti concentri profondamente, recuperando {sanity_gain} punti sanità.")

    def void_purification(self, target):
        corruption_loss = random.randint(10, 25)
        self.corruption -= corruption_loss
        damage = self.corruption // 2
        target.take_damage(damage)
        print(f"Purifichi parte della tua corruzione, riducendola di {corruption_loss} e infliggendo {damage} danni al nemico.")

    def eldritch_resonance(self, target):
        if self.knowledge >= 10:
            damage = self.knowledge * 3
            target.take_damage(damage)
            self.corruption += 5
            print(f"Usi la tua conoscenza del Void per infliggere {damage} danni al nemico, ma guadagni 5 corruzione.")
        else:
            print("Non hai abbastanza conoscenza per usare questa abilità.")