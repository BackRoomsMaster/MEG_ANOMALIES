import random

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def use(self, player):
        pass

class SanityFragment(Item):
    def use(self, player):
        heal = random.randint(15, 30)
        player.sanity += heal
        print(f"Il Frammento di Sanità si dissolve nella tua mente. Recuperi {heal} punti sanità.")

class VoidEssence(Item):
    def use(self, player):
        player.corruption -= random.randint(10, 20)
        player.knowledge += 1
        print("L'Essenza del Void purifica la tua corruzione, ma ti lascia con una comprensione più profonda dell'abisso.")

class RealityAnchor(Item):
    def use(self, player):
        player.sanity += 10
        player.corruption -= 5
        print("L'Ancora di Realtà ti dà un momento di lucidità nel caos del Void.")

class EldritchTome(Item):
    def use(self, player):
        if random.random() < 0.7:
            player.knowledge += random.randint(2, 5)
            player.corruption += random.randint(5, 15)
            print("Le conoscenze proibite del Tomo Eldritch espandono la tua mente, al costo di una maggiore corruzione.")
        else:
            player.sanity -= random.randint(10, 20)
            print("Le rivelazioni del Tomo Eldritch sono troppo per la tua mente fragile.")

class VoidCompass(Item):
    def use(self, player):
        print("La Bussola del Void rivela brevemente la struttura del regno.")
        for loc in locations:
            print(f"- {loc}: {locations[loc].description}")

items = {
    "Frammento di Sanità": SanityFragment("Frammento di Sanità", "Un frammento cristallino di pura lucidità."),
    "Essenza del Void": VoidEssence("Essenza del Void", "Un liquido oscuro che pulsa con energia caotica."),
    "Ancora di Realtà": RealityAnchor("Ancora di Realtà", "Un oggetto che sembra appartenere al mondo reale."),
    "Tomo Eldritch": EldritchTome("Tomo Eldritch", "Un libro antico contenente conoscenze proibite."),
    "Bussola del Void": VoidCompass("Bussola del Void", "Uno strumento che sembra puntare in direzioni impossibili.")
}