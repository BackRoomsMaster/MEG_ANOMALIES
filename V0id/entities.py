import random

class Entity:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def encounter(self, player):
        print(f"Ti trovi faccia a faccia con {self.name}!")
        print(self.description)
        self.effect(player)

    def effect(self, player):
        pass

class Corrupted(Entity):
    def effect(self, player):
        damage = random.randint(10, 25)
        corruption = random.randint(5, 15)
        player.sanity -= damage
        player.corruption += corruption
        print(f"Il Corrotto ti assale con orrori indicibili! Perdi {damage} sanità mentale e guadagni {corruption} corruzione.")

class Spychard(Entity):
    def effect(self, player):
        if random.random() < 0.6:
            damage = random.randint(15, 30)
            player.sanity -= damage
            print(f"Lo Spychard penetra nella tua mente! Perdi {damage} sanità mentale.")
        else:
            print("Resisti al controllo mentale dello Spychard, ma l'esperienza ti lascia scosso.")
            player.sanity -= 10

class Kraken(Entity):
    def effect(self, player):
        damage = random.randint(25, 40)
        corruption = random.randint(10, 20)
        player.sanity -= damage
        player.corruption += corruption
        print(f"Il Kraken emerge dalle profondità, la sua presenza è devastante! Perdi {damage} sanità mentale e guadagni {corruption} corruzione.")

class VoidWalker(Entity):
    def effect(self, player):
        if player.knowledge > 5:
            print("Il tuo Void Walker ti offre una visione del futuro. Guadagni 10 punti sanità.")
            player.sanity += 10
        else:
            damage = random.randint(10, 20)
            player.sanity -= damage
            print(f"Il Void Walker ti mostra verità che non sei pronto a comprendere. Perdi {damage} sanità mentale.")

class EyeServant(Entity):
    def effect(self, player):
        corruption = random.randint(15, 25)
        player.corruption += corruption
        print(f"Il Servitore dell'Occhio ti avvolge in un'aura di corruzione! Guadagni {corruption} corruzione.")
        if random.random() < 0.4:
            knowledge = random.randint(1, 3)
            player.knowledge += knowledge
            print(f"Nonostante l'orrore, acquisisci {knowledge} punti di conoscenza del Void.")

entities = {
    "Corrupted": Corrupted("Corrupted", "Un essere contorto e corrotto, un tempo umano."),
    "Spychard": Spychard("Spychard", "Una creatura simile a un ragno con poteri di controllo mentale."),
    "Kraken": Kraken("Kraken", "Un'enorme bestia tentacolare che domina il Void."),
    "Void Walker": VoidWalker("Void Walker", "Un'entità eterea che fluttua tra le dimensioni del Void."),
    "Servitore dell'Occhio": EyeServant("Servitore dell'Occhio", "Un essere devoto all'Occhio, emanante un'aura di pura corruzione.")
}