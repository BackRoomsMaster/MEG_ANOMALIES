import random
from player import Player
from locations import locations
from entities import entities
from items import items
from events import random_events
from puzzles import puzzles
from combat import boss_encounter

def main():
    print("Benvenuto nelle profondità insondabili del Void. La tua sanità mentale è l'unica barriera contro l'oblio eterno.")
    player_name = input("Sussurra il tuo nome nell'oscurità: ")
    player = Player(player_name)

    while player.is_alive() and not player.is_fully_corrupted() and not player.has_escaped():
        current_location = locations[player.current_location]
        print(f"\n{current_location.describe()}")
        
        # Evento casuale
        if random.random() < 0.3:  # 30% di possibilità di un evento casuale
            random_events[random.choice(list(random_events.keys()))](player)
        
        # Effetto ambientale costante
        player.apply_environmental_effect(current_location)
        
        # Possibilità di incontro con il boss
        if player.knowledge >= 20 and random.random() < 0.1:  # 10% di possibilità quando la conoscenza è alta
            print("Senti una presenza cosmica avvicinarsi...")
            boss_encounter(player)
        
        action = input("Cosa osi fare nel regno del caos? [esplorare/riposare/inventario/usare/muovere/meditare/analizzare]: ").lower()
        
        if action == "esplorare":
            explore(player, current_location)
        elif action == "riposare":
            player.rest()
        elif action == "inventario":
            player.show_inventory()
        elif action == "usare":
            use_item(player)
        elif action == "muovere":
            move_player(player)
        elif action == "meditare":
            player.meditate()
        elif action == "analizzare":
            analyze_surroundings(player, current_location)
        else:
            print("La tua indecisione alimenta il Void. La corruzione cresce.")
            player.corruption += 1
        
        player.show_status()
        
        # Controllo condizioni di fine gioco
        if player.corruption >= 90:
            print("La corruzione ti sta consumando. Senti la tua volontà svanire...")
        if player.sanity <= 10:
            print("La tua mente vacilla sull'orlo dell'abisso. La follia ti chiama...")

    if not player.is_alive():
        print("La tua mente si è frantumata come vetro nell'infinito. Sei diventato uno con il Void, per sempre perduto nell'oblio.")
    elif player.is_fully_corrupted():
        print("La corruzione ha divorato la tua essenza. Sei ora un'entità del Void, condannato a vagare per l'eternità.")
    elif player.has_escaped():
        print("Contro ogni probabilità, sei riuscito a sfuggire al Void. Ma a quale costo? Le cicatrici sulla tua anima non guariranno mai completamente.")

def explore(player, location):
    print(f"Ti addentri nelle profondità di {location.name}...")
    player.sanity -= random.randint(3, 8)
    player.corruption += random.randint(1, 5)
    
    if random.random() < 0.4:  # 40% di possibilità di trovare un oggetto
        item = random.choice(list(items.values()))
        print(f"Tra l'orrore, scorgi: {item.name}")
        player.add_item(item)
    
    if random.random() < 0.4:  # 40% di possibilità di incontrare un'entità
        entity = random.choice(list(entities.values()))
        entity.encounter(player)
    
    if random.random() < 0.2:  # 20% di possibilità di trovare un puzzle
        puzzle = random.choice(list(puzzles.values()))
        puzzle.solve(player)

def use_item(player):
    player.show_inventory()
    item_name = input("Quale reliquia del Void desideri utilizzare? ")
    player.use_item(item_name)

def move_player(player):
    print("Portali verso l'ignoto:")
    for loc in locations:
        if loc != player.current_location:
            print(f"- {loc}")
    new_location = input("Verso quale abisso desideri avventurarti? ")
    if new_location in locations and new_location != player.current_location:
        player.move_to(new_location)
    else:
        print("Il Void distorce la tua percezione. Non riesci a raggiungere quel luogo.")
        player.sanity -= 5

def analyze_surroundings(player, location):
    print("Concentri la tua mente frammentata per comprendere l'incomprensibile...")
    insight = random.randint(1, 10)
    if insight > 7:
        print(location.reveal_secret())
        player.sanity += 5
        print("La comprensione porta un momento di lucidità. Guadagni 5 punti sanità.")
    elif insight > 3:
        print("Scorgi pattern nel caos, ma il loro significato ti sfugge.")
    else:
        print("L'analisi ti porta sull'orlo della follia. Perdi 10 punti sanità.")
        player.sanity -= 10

if __name__ == "__main__":
    main()