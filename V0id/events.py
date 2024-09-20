import random

def eye_gaze(player):
    print("Senti lo sguardo penetrante dell'Occhio su di te. La sua presenza è opprimente e onnisciente.")
    sanity_loss = random.randint(10, 25)
    corruption_gain = random.randint(5, 15)
    player.sanity -= sanity_loss
    player.corruption += corruption_gain
    print(f"Perdi {sanity_loss} sanità mentale e guadagni {corruption_gain} corruzione.")
    if random.random() < 0.3:
        player.knowledge += 1
        print("Nonostante l'orrore, acquisisci una nuova comprensione del Void.")

def void_whispers(player):
    print("Sussurri incomprensibili riempiono la tua mente, promettendo segreti cosmici.")
    if random.random() < 0.4:
        print("Resisti alla follia e decifri parte del messaggio!")
        player.sanity -= 10
        player.knowledge += 2
    else:
        print("I sussurri ti sopraffanno, portandoti sull'orlo della pazzia.")
        player.sanity -= 20
        player.corruption += 15

def reality_shift(player):
    print("La realtà intorno a te si distorce e cambia in modi impossibili.")
    effect = random.choice(["sanity", "corruption", "teleport", "item"])
    if effect == "sanity":
        change = random.randint(-20, 20)
        player.sanity += change
        print(f"La distorsione della realtà {"aumenta" if change > 0 else "diminuisce"} la tua sanità di {abs(change)} punti.")
    elif effect == "corruption":
        change = random.randint(-15, 15)
        player.corruption += change
        print(f"La distorsione della realtà {"aumenta" if change > 0 else "diminuisce"} la tua corruzione di {abs(change)} punti.")
    elif effect == "teleport":
        player.current_location = random.choice(list(locations.keys()))
        print(f"Ti ritrovi improvvisamente in: {player.current_location}")
    elif effect == "item":
        if random.random() < 0.5 and player.inventory:
            lost_item = random.choice(player.inventory)
            player.inventory.remove(lost_item)
            print(f"La distorsione della realtà fa scomparire il tuo {lost_item.name}!")
        else:
            new_item = random.choice(list(items.values()))
            player.add_item(new_item)
            print(f"La distorsione della realtà fa apparire un nuovo oggetto: {new_item.name}")

def void_storm(player):
    print("Una tempesta di energia del Void si abbatte su di te!")
    damage = random.randint(15, 30)
    corruption = random.randint(10, 20)
    player.sanity -= damage
    player.corruption += corruption
    print(f"La tempesta erode la tua sanità di {damage} punti e aumenta la tua corruzione di {corruption} punti.")
    if random.random() < 0.3:
        player.knowledge += 2
        print("Attraverso il dolore, acquisisci una nuova comprensione del Void.")

def eldritch_revelation(player):
    print("Una rivelazione cosmica si manifesta nella tua mente!")
    if player.knowledge > 10:
        print("La tua conoscenza del Void ti permette di comprendere la rivelazione.")
        player.sanity += 20
        player.knowledge += 3
    else:
        print("La rivelazione è troppo per la tua mente impreparata.")
        player.sanity -= 25
        player.corruption += 15

random_events = {
    "eye_gaze": eye_gaze,
    "void_whispers": void_whispers,
    "reality_shift": reality_shift,
    "void_storm": void_storm,
    "eldritch_revelation": eldritch_revelation
}