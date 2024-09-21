import time
import random

class Player:
    def __init__(self):
        self.health = 100
        self.sanity = 100
        self.team_members = 3
        self.artifacts = 0

def slow_print(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def make_choice(options):
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    while True:
        try:
            choice = int(input("Inserisci il numero della tua scelta: "))
            if 1 <= choice <= len(options):
                return choice
            else:
                print("Scelta non valida. Riprova.")
        except ValueError:
            print("Per favore, inserisci un numero.")

def check_game_over(player):
    if player.health <= 0:
        slow_print("Sei morto. La missione è fallita.")
        return True
    if player.sanity <= 0:
        slow_print("Hai perso la ragione. Sei diventato un'altra vittima del Dominio di Upsilon.")
        return True
    if player.team_members <= 0:
        slow_print("Hai perso tutti i tuoi compagni. Solo e abbandonato, la tua missione termina qui.")
        return True
    return False

def intro():
    slow_print("Inizializzazione del database MEG... Accesso ai ricordi traumatici...")
    time.sleep(1)
    slow_print("Attenzione: I seguenti ricordi contengono scene di violenza estrema e orrore cosmico.")
    time.sleep(1)
    slow_print("\n--- DOMINIO DI UPSILON: LA CADUTA DEGLI DEI ---")
    slow_print("Sei il Comandante, leader della squadra d'élite Omega del MEG.")
    slow_print("La vostra missione: infiltrarvi nel cuore pulsante del Dominio di Upsilon.")
    slow_print("Obiettivo: distruggere il Signore Pallido e il Dio dal Doppio Volto, liberando l'universo dalla loro influenza corrotta.")
    slow_print("Il destino di innumerevoli realtà dipende dal vostro successo.")

def flesh_sea(player):
    slow_print("\nVi ritrovate di fronte all'abominio cosmico noto come il Mare di Carne.")
    slow_print("Un oceano infinito di corpi contorti e anime urlanti si estende a perdita d'occhio.")
    slow_print("L'odore di putrefazione è insopportabile. Cosa fai?")
    
    choice = make_choice([
        "Attraversare a nuoto il mare di carne",
        "Costruire una zattera con i corpi",
        "Cercare un passaggio sotterraneo"
    ])
    
    if choice == 1:
        slow_print("Vi immergete nel mare di carne. Corpi si avvinghiano alle vostre gambe, trascinandovi verso il basso.")
        player.health -= 30
        player.sanity -= 20
        slow_print(f"Salute: {player.health}, Sanità: {player.sanity}")
        if random.random() < 0.3:
            slow_print("Uno dei tuoi compagni viene trascinato negli abissi, scomparendo per sempre.")
            player.team_members -= 1
        else:
            slow_print("Riuscite a sopravvivere, ma l'esperienza vi ha segnato profondamente.")
    elif choice == 2:
        slow_print("Costruite una zattera macabra. Durante il viaggio, i corpi iniziano a sussurrare segreti cosmici.")
        player.sanity -= 15
        slow_print(f"Salute: {player.health}, Sanità: {player.sanity}")
        if random.random() < 0.4:
            slow_print("Tra i corpi, trovate un antico artefatto. Potrebbe tornarvi utile.")
            player.artifacts += 1
    else:
        slow_print("Trovate un passaggio, ma è infestato da creature indicibili. Combattete per la vostra vita.")
        player.health -= 20
        slow_print(f"Salute: {player.health}, Sanità: {player.sanity}")
        if random.random() < 0.5:
            slow_print("Nonostante le difficoltà, scoprite un'antica mappa del Dominio di Upsilon.")
            player.artifacts += 1
    
    slow_print("Dopo un viaggio straziante, raggiungete la base di Monteggrigio, esausti e traumatizzati.")

def greymount_ascent(player):
    slow_print("\nMonteggrigio si erge davanti a voi, una montagna che sfida le leggi della fisica e della sanità.")
    slow_print("Mentre scalate, la realtà stessa sembra piegarsi e contorcersi.")
    slow_print("A metà strada, incontrate un Avatar del Dio dal Doppio Volto. Come reagisci?")
    
    choice = make_choice([
        "Ingaggiare un combattimento all'ultimo sangue",
        "Tentare un rituale di esorcismo",
        "Cercare di ingannare l'Avatar"
    ])
    
    if choice == 1:
        battle_avatar(player)
    elif choice == 2:
        ritual_avatar(player)
    else:
        deceive_avatar(player)
    
    slow_print(f"Salute: {player.health}, Sanità: {player.sanity}, Membri del team: {player.team_members}")
    slow_print("Esausti e sull'orlo della follia, raggiungete la vetta di Monteggrigio.")

def battle_avatar(player):
    slow_print("Inizia una battaglia epica contro l'Avatar del Dio dal Doppio Volto.")
    rounds = 3
    for i in range(rounds):
        slow_print(f"\nRound {i+1} di {rounds}")
        choice = make_choice([
            "Attacco frontale",
            "Manovra evasiva",
            "Usare un artefatto (se disponibile)"
        ])
        
        if choice == 1:
            if random.random() < 0.6:
                slow_print("Il tuo attacco va a segno! L'Avatar barcolla.")
                player.health -= 10
            else:
                slow_print("L'Avatar schiva il tuo attacco e contrattacca!")
                player.health -= 20
        elif choice == 2:
            if random.random() < 0.7:
                slow_print("Riesci a evitare l'attacco dell'Avatar!")
            else:
                slow_print("Nonostante i tuoi sforzi, l'Avatar ti colpisce.")
                player.health -= 15
        elif choice == 3 and player.artifacts > 0:
            slow_print("Usi un artefatto contro l'Avatar. Una luce accecante lo indebolisce!")
            player.artifacts -= 1
            player.health -= 5
        else:
            slow_print("Non hai artefatti. L'Avatar approfitta della tua esitazione!")
            player.health -= 25
        
        slow_print(f"Salute: {player.health}")
    
    if player.health > 30:
        slow_print("Con un ultimo sforzo sovrumano, sconfiggi l'Avatar!")
    else:
        slow_print("Sconfiggi l'Avatar, ma le ferite sono gravi.")
    player.sanity -= 20

def ritual_avatar(player):
    slow_print("Iniziate un rituale antico per esorcizzare l'Avatar.")
    success_chance = 0.5
    for i in range(3):
        slow_print(f"\nFase {i+1} del rituale")
        choice = make_choice([
            "Recitare antiche formule",
            "Offrire un sacrificio di sangue",
            "Canalizzare l'energia del Dominio"
        ])
        
        if choice == 1:
            if random.random() < success_chance:
                slow_print("Le tue parole risuonano con potere. L'Avatar si contorce!")
                success_chance += 0.1
            else:
                slow_print("Le parole sembrano non avere effetto. L'Avatar ride.")
                success_chance -= 0.1
                player.sanity -= 10
        elif choice == 2:
            slow_print("Offri il tuo sangue. Il rituale guadagna potenza, ma a che costo?")
            player.health -= 15
            success_chance += 0.2
        else:
            if random.random() < 0.5:
                slow_print("Riesci a canalizzare l'energia. Il rituale si intensifica!")
                success_chance += 0.15
            else:
                slow_print("L'energia ti sopraffà, causando dolore indicibile.")
                player.health -= 10
                player.sanity -= 15
    
    if random.random() < success_chance:
        slow_print("Il rituale ha successo! L'Avatar viene bandito in un'altra dimensione.")
    else:
        slow_print("Il rituale fallisce. L'Avatar attacca con furia rinnovata!")
        player.health -= 30
        player.sanity -= 20

def deceive_avatar(player):
    slow_print("Inizi un pericoloso gioco di inganni con l'Avatar del Dio dal Doppio Volto.")
    deception_points = 0
    for i in range(3):
        slow_print(f"\nRound {i+1} di inganno")
        choice = make_choice([
            "Mentire spudoratamente",
            "Dire una mezza verità",
            "Usare conoscenze segrete"
        ])
        
        if choice == 1:
            if random.random() < 0.4:
                slow_print("La tua bugia è convincente. L'Avatar sembra crederci.")
                deception_points += 2
            else:
                slow_print("L'Avatar vede attraverso la tua bugia. La sua ira cresce!")
                player.sanity -= 15
        elif choice == 2:
            if random.random() < 0.6:
                slow_print("La mezza verità confonde l'Avatar. Guadagni un vantaggio.")
                deception_points += 1
            else:
                slow_print("L'Avatar coglie la verità nascosta. Ti attacca!")
                player.health -= 10
        else:
            if player.artifacts > 0:
                slow_print("Usi conoscenze segrete ottenute da un artefatto. L'Avatar è impressionato.")
                deception_points += 3
                player.artifacts -= 1
            else:
                slow_print("Non hai conoscenze segrete da usare. L'Avatar si insospettisce.")
                player.sanity -= 10
    
    if deception_points >= 5:
        slow_print("Sei riuscito a ingannare l'Avatar! Si ritira, lasciandovi passare.")
    else:
        slow_print("L'Avatar vede attraverso i tuoi inganni. Attacca con furia sovrannaturale!")
        player.health -= 25
        player.sanity -= 20

def final_confrontation(player):
    slow_print("\nSulla vetta di Monteggrigio, vi trovate di fronte agli orrori cosmici del Signore Pallido e del Dio dal Doppio Volto.")
    slow_print("La loro mera presenza minaccia di annientare la vostra esistenza.")
    slow_print("È giunto il momento dello scontro finale. Come affronterai queste entità al di là della comprensione umana?")
    
    battle_rounds = 5
    for round in range(battle_rounds):
        slow_print(f"\n--- Round {round + 1} di {battle_rounds} ---")
        slow_print(f"Salute: {player.health}, Sanità: {player.sanity}, Membri del team: {player.team_members}")
        
        choice = make_choice([
            "Attacco coordinato",
            "Difesa e contrattacco",
            "Usare un artefatto (se disponibile)",
            "Sacrificio eroico"
        ])
        
        if choice == 1:
            coordinated_attack(player)
        elif choice == 2:
            defend_and_counter(player)
        elif choice == 3:
            use_artifact(player)
        else:
            heroic_sacrifice(player)
        
        if check_game_over(player):
            return False
        
        # Le divinità contrattaccano
        divine_counterattack(player)
        
        if check_game_over(player):
            return False
    
    # Esito finale della battaglia
    if player.health > 30 and player.sanity > 30:
        slow_print("\nCon un ultimo, disperato assalto, riuscite a sconfiggere le divinità corrotte!")
        slow_print("Il Dominio di Upsilon inizia a collassare intorno a voi, ma avete trionfato.")
        return True
    else:
        slow_print("\nNonostante i vostri sforzi eroici, le divinità sono troppo potenti.")
        slow_print("Venite sopraffatti, ma il vostro sacrificio non sarà dimenticato.")
        return False

def coordinated_attack(player):
    slow_print("Lanciate un attacco coordinato contro le divinità.")
    if random.random() < 0.6:
        slow_print("L'attacco ha successo! Infliggete danni significativi.")
        player.health -= 10
    else:
        slow_print("Le divinità prevedono il vostro attacco e contrattaccano con forza devastante.")
        player.health -= 25
        player.sanity -= 15

def defend_and_counter(player):
    slow_print("Adottate una posizione difensiva, cercando il momento giusto per contrattaccare.")
    if random.random() < 0.7:
        slow_print("La vostra strategia funziona! Riuscite a difendervi e a infliggere danni.")
        player.health -= 5
    else:
        slow_print("La potenza delle divinità supera le vostre difese.")
        player.health -= 15
        player.sanity -= 10

def use_artifact(player):
    if player.artifacts > 0:
        slow_print("Utilizzate un potente artefatto contro le divinità.")
        player.artifacts -= 1
        if random.random() < 0.8:
            slow_print("L'artefatto rilascia un'energia immensa, danneggiando gravemente le divinità!")
            player.health -= 5
        else:
            slow_print("L'artefatto si rivela instabile, danneggiando sia voi che le divinità.")
def use_artifact(player):
    if player.artifacts > 0:
        slow_print("Utilizzate un potente artefatto contro le divinità.")
        player.artifacts -= 1
        if random.random() < 0.8:
            slow_print("L'artefatto rilascia un'energia immensa, danneggiando gravemente le divinità!")
            player.health -= 5
        else:
            slow_print("L'artefatto si rivela instabile, danneggiando sia voi che le divinità.")
            player.health -= 20
            player.sanity -= 15
    else:
        slow_print("Non avete più artefatti! Le divinità approfittano della vostra esitazione.")
        player.health -= 30
        player.sanity -= 20

def heroic_sacrifice(player):
    slow_print("Decidete di compiere un sacrificio eroico per danneggiare le divinità.")
    if player.team_members > 1:
        slow_print("Uno dei tuoi compagni si offre volontario per un attacco suicida.")
        player.team_members -= 1
        if random.random() < 0.9:
            slow_print("Il sacrificio infligge danni enormi alle divinità, ma il costo è alto.")
            player.sanity -= 30
        else:
            slow_print("Il sacrificio non ha l'effetto sperato. La perdita sembra vana.")
            player.sanity -= 50
    else:
        slow_print("Sei l'ultimo rimasto. Ti lanci in un attacco disperato.")
        player.health = 1
        if random.random() < 0.7:
            slow_print("Il tuo sacrificio quasi totale ferisce gravemente le divinità!")
        else:
            slow_print("Il tuo sacrificio non è sufficiente. Le divinità ti sopraffanno.")
            player.health = 0

def divine_counterattack(player):
    attack_type = random.choice(["Signore Pallido", "Dio dal Doppio Volto"])
    if attack_type == "Signore Pallido":
        slow_print("Il Signore Pallido scatena un'onda di energia grigia che minaccia di cancellare la vostra esistenza.")
        if random.random() < 0.5:
            slow_print("Riuscite a resistere all'attacco, ma siete gravemente feriti.")
            player.health -= 20
        else:
            slow_print("L'attacco vi colpisce in pieno, causando danni fisici e mentali devastanti.")
            player.health -= 30
            player.sanity -= 25
    else:
        slow_print("Il Dio dal Doppio Volto distorce la realtà intorno a voi, attaccando la vostra sanità mentale.")
        if random.random() < 0.6:
            slow_print("Resistete alla distorsione della realtà, ma la vostra mente è provata.")
            player.sanity -= 20
        else:
            slow_print("La vostra mente vacilla sotto l'assalto cosmico. La follia si avvicina.")
            player.sanity -= 35
            player.health -= 15

def epilogue(victory):
    if victory:
        slow_print("\nAvete sconfitto il Signore Pallido e il Dio dal Doppio Volto!")
        slow_print("Il Dominio di Upsilon inizia a collassare intorno a voi.")
        slow_print("Fuggite attraverso portali dimensionali, inseguiti dai frammenti di una realtà morente.")
        slow_print("Tornati al quartier generale del MEG, siete accolti come eroi leggendari.")
        slow_print("Le vostre gesta saranno cantate per eoni, ma le cicatrici di questa missione vi perseguiteranno per sempre.")
        slow_print("\nFINE DELLA MISSIONE: VITTORIA EPICA")
    else:
        slow_print("\nNonostante i vostri sforzi eroici, la missione è fallita.")
        slow_print("Il Dominio di Upsilon continua a espandersi, minacciando innumerevoli realtà.")
        slow_print("Il vostro sacrificio sarà ricordato, ma l'orrore cosmico continua a crescere.")
        slow_print("Forse un giorno, altri eroi raccoglieranno il testimone della vostra lotta.")
        slow_print("\nFINE DELLA MISSIONE: SCONFITTA EROICA")

def main():
    player = Player()
    intro()
    
    if not check_game_over(player):
        flesh_sea(player)
    
    if not check_game_over(player):
        greymount_ascent(player)
    
    if not check_game_over(player):
        victory = final_confrontation(player)
        epilogue(victory)
    
    slow_print("\nFine della simulazione di memoria. Disconnessione dal database MEG...")
    slow_print("Che gli dei abbiano pietà delle nostre anime.")

if __name__ == "__main__":
    main()