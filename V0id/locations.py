import random

class Location:
    def __init__(self, name, description, secrets):
        self.name = name
        self.description = description
        self.secrets = secrets

    def describe(self):
        return f"{self.name}: {self.description}"

    def reveal_secret(self):
        if self.secrets:
            return random.choice(self.secrets)
        return "Non ci sono più segreti da svelare in questo luogo."

    def environmental_effect(self):
        return {
            'sanity': random.randint(-5, 0),
            'corruption': random.randint(0, 3)
        }

class VoidPortal(Location):
    def environmental_effect(self):
        return {
            'sanity': random.randint(-3, 3),
            'corruption': random.randint(1, 5)
        }

class CorruptedForest(Location):
    def environmental_effect(self):
        return {
            'sanity': random.randint(-7, -2),
            'corruption': random.randint(2, 6)
        }

class FloatingIslands(Location):
    def environmental_effect(self):
        return {
            'sanity': random.randint(-5, 5),
            'corruption': random.randint(0, 4)
        }

class ScreamingAbyss(Location):
    def environmental_effect(self):
        return {
            'sanity': random.randint(-10, -5),
            'corruption': random.randint(3, 8)
        }

class EyeTemple(Location):
    def environmental_effect(self):
        return {
            'sanity': random.randint(-15, -8),
            'corruption': random.randint(5, 10)
        }

locations = {
    "Portale del Void": VoidPortal("Portale del Void", "Un vortice di energia oscura che pulsa con malevolenza.", 
                                   ["Il portale sussurra segreti cosmici incomprensibili.", "Vedi brevemente altre realtà attraverso il vortice."]),
    "Foresta Corrotta": CorruptedForest("Foresta Corrotta", "Alberi contorti e malati, con foglie che gocciolano un liquido viola.",
                                        ["Gli alberi sembrano muoversi quando non li guardi.", "Senti voci provenire dal cuore della foresta."]),
    "Isole Fluttuanti": FloatingIslands("Isole Fluttuanti", "Frammenti di terra che galleggiano nel vuoto, collegati da ponti precari.",
                                        ["Alcune isole nascondono antiche rovine.", "Il vuoto sotto le isole sembra chiamarti."]),
    "Abisso Urlante": ScreamingAbyss("Abisso Urlante", "Un'enorme voragine da cui provengono suoni indescrivibili.",
                                     ["Gli urli sembrano formare parole in una lingua sconosciuta.", "Vedi ombre muoversi nelle profondità dell'abisso."]),
    "Tempio dell'Occhio": EyeTemple("Tempio dell'Occhio", "Una struttura aliena che ospita l'entità nota come l'Occhio.",
                                        ["L'Occhio sembra seguire ogni tuo movimento.", "Antiche iscrizioni sul muro raccontano la storia del Void."])
}