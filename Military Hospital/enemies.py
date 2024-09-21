import random

class Enemy:
    def __init__(self, name, health, damage, description):
        self.name = name
        self.health = health
        self.damage = damage
        self.description = description

    def attack(self):
        return random.randint(self.damage[0], self.damage[1])

enemies = [
    Enemy("Ombra Strisciante", 30, (5, 10), 
          "Una massa oscura che si muove lungo le pareti, quasi indistinguibile dall'ombra."),
    Enemy("Mannequin Animato", 50, (10, 15), 
          "Un manichino che si muove a scatti, con un sorriso inquietante dipinto sul volto."),
    Enemy("Eco Distorto", 40, (8, 12), 
          "Una creatura fatta di suoni distorti e echi, che confonde e disorientata."),
    Enemy("Infermiere Deformato", 60, (12, 18), 
          "Un essere che un tempo poteva essere un infermiere, ora orribilmente mutato."),
    Enemy("Paziente Zero", 70, (15, 20), 
          "Un paziente trasformato in una creatura aggressiva e contagiosa.")
]

class Boss(Enemy):
    def __init__(self, name, health, damage, description, special_attack):
        super().__init__(name, health, damage, description)
        self.special_attack = special_attack

    def use_special_attack(self):
        return self.special_attack()

final_boss = Boss("Il Guardiano dell'Ospedale", 500, (30, 50),
                  "Una mostruosa fusione di carne, metallo e architettura ospedaliera. Sembra essere parte integrante dell'edificio stesso.",
                  lambda: random.randint(50, 100))  # Attacco speciale che causa danni massicci