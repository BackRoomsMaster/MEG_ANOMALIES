import random

class Combat:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy
        self.turn = 0

    def start_combat(self):
        print(f"Inizia lo scontro con {self.enemy.name}!")
        print(self.enemy.description)
        
        while self.player.is_alive() and self.enemy.is_alive():
            self.turn += 1
            print(f"\n--- Turno {self.turn} ---")
            self.player_turn()
            if self.enemy.is_alive():
                self.enemy_turn()
            
        if self.player.is_alive():
            print(f"Hai sconfitto {self.enemy.name}!")
            self.enemy.on_defeat(self.player)
        else:
            print("Sei stato sconfitto...")

    def player_turn(self):
        print(f"La tua sanità: {self.player.sanity}, Corruzione: {self.player.corruption}")
        print(f"Salute del {self.enemy.name}: {self.enemy.health}")
                action = input("Cosa vuoi fare? [attacca/difendi/oggetto/abilità]: ").lower()
        
        if action == "attacca":
            damage = self.player.calculate_damage()
            self.enemy.take_damage(damage)
            print(f"Infliggi {damage} danni a {self.enemy.name}!")
        elif action == "difendi":
            self.player.defend()
        elif action == "oggetto":
            self.use_item()
        elif action == "abilità":
            self.use_ability()
        else:
            print("Azione non valida. Perdi il turno!")

    def enemy_turn(self):
        action = self.enemy.choose_action()
        if action == "attack":
            damage = self.enemy.calculate_damage()
            self.player.take_damage(damage)
            print(f"{self.enemy.name} ti infligge {damage} danni!")
        else:
            self.enemy.special_action(self.player)

    def use_item(self):
        self.player.show_inventory()
        item_name = input("Quale oggetto vuoi usare? ")
        self.player.use_item(item_name)

    def use_ability(self):
        self.player.show_abilities()
        ability_name = input("Quale abilità vuoi usare? ")
        self.player.use_ability(ability_name, self.enemy)

class Enemy:
    def __init__(self, name, description, health, damage):
        self.name = name
        self.description = description
        self.health = health
        self.max_health = health
        self.damage = damage

    def is_alive(self):
        return self.health > 0

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def calculate_damage(self):
        return random.randint(self.damage - 5, self.damage + 5)

    def choose_action(self):
        return "attack"

    def special_action(self, player):
        pass

    def on_defeat(self, player):
        pass

class Boss(Enemy):
    def __init__(self, name, description, health, damage, special_attacks):
        super().__init__(name, description, health, damage)
        self.special_attacks = special_attacks
        self.phase = 1

    def choose_action(self):
        if self.health < self.max_health * 0.5 and self.phase == 1:
            self.phase = 2
            return "phase_change"
        elif random.random() < 0.3:
            return random.choice(list(self.special_attacks.keys()))
        else:
            return "attack"

    def special_action(self, player):
        action = self.choose_action()
        if action in self.special_attacks:
            self.special_attacks[action](player)
        elif action == "phase_change":
            self.phase_change(player)

    def phase_change(self, player):
        print(f"{self.name} entra in una nuova fase!")
        self.damage += 10
        self.health += self.max_health * 0.2
        print(f"{self.name} diventa più potente!")

# Esempio di boss: L'Occhio del Void
def eye_beam(player):
    damage = random.randint(20, 30)
    player.take_damage(damage)
    player.corruption += 5
    print(f"L'Occhio del Void emette un raggio di energia corrotta! Subisci {damage} danni e guadagni 5 corruzione.")

def mind_shatter(player):
    sanity_loss = random.randint(15, 25)
    player.sanity -= sanity_loss
    print(f"L'Occhio del Void frantuma la tua mente! Perdi {sanity_loss} sanità.")

def summon_minions(player):
    print("L'Occhio del Void evoca dei servitori!")
    for _ in range(2):
        minion = Enemy("Servitore dell'Occhio", "Un essere corrotto al servizio dell'Occhio", 30, 10)
        damage = minion.calculate_damage()
        player.take_damage(damage)
        print(f"Un servitore ti attacca per {damage} danni!")

eye_of_void = Boss("L'Occhio del Void", "Un'entità cosmica di pura malvagità e conoscenza proibita", 500, 25, 
                   {"eye_beam": eye_beam, "mind_shatter": mind_shatter, "summon_minions": summon_minions})

def boss_encounter(player):
    combat = Combat(player, eye_of_void)
    combat.start_combat()