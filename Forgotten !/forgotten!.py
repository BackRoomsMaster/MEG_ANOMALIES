import time
import sys

def slow_print(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def make_choice(options):
    while True:
        choice = input("Cosa fai? ").lower()
        if choice in options:
            return choice
        print("Non capisco. Prova di nuovo.")

def dialogue(speaker, text):
    slow_print(f"{speaker}: ", delay=0.02)
    slow_print(text, delay=0.03)
    time.sleep(0.5)  # Pausa breve tra le battute di dialogo

def game():
    slow_print("\nTi trovi davanti a una porta con un punto esclamativo sbiadito...")
    time.sleep(1)
    
    dialogue("Tu", "Allora, spiegami di nuovo perché siamo nel 109?")
    dialogue("Amico", "Okay, okay, ricordi quella leggenda horror sui forum? Quella stupida sul corridoio?")
    dialogue("Tu", "Sì, ne stavamo ridendo la settimana scorsa... perché?")
    dialogue("Amico", "Beh, questo suonerà folle, ma... penso di averlo trovato. Qui.")
    dialogue("Tu", "... Cosa?")
    dialogue("Amico", "Sono serio! Dai, vieni a trovare questa porta con me.")
    
    choice = make_choice(["segui", "rifiuta"])
    if choice == "rifiuta":
        slow_print("Decidi di non seguire il tuo amico. Forse alcune leggende dovrebbero rimanere tali.")
        return

    slow_print("\nSegui il tuo amico fino alla porta con il simbolo sbiadito...")
    dialogue("Tu", "È solo una porta.")
    dialogue("Amico", "Sì, ma non vedi quel segno sbiadito?")
    dialogue("Tu", "Chiunque potrebbe averlo messo lì...")
    dialogue("Amico", "Dai, potremmo fare la storia qui! Una leggenda, scoperta essere vera!")
    dialogue("Tu", "O potremmo finire morti prima che la notizia si diffonda.")
    dialogue("Amico", "Per favore? Daremo solo un'occhiata dentro e basta, okay?")
    
    choice = make_choice(["entra", "rifiuta"])
    if choice == "rifiuta":
        slow_print("Decidi di non entrare. Il rischio è troppo alto.")
        return

    slow_print("\nEntri nella prima stanza. Le pareti metalliche riflettono una tenue luce rossa.")
    dialogue("Tu", "Beh, questo sembra...")
    dialogue("Amico", "Silenzioso da morire senza motivo? Sì.")
    
    while True:
        slow_print("\nVedi due porte: una sembra essere stata forzata, l'altra conduce al corridoio.")
        choice = make_choice(["porta forzata", "corridoio", "rifletti"])
        
        if choice == "porta forzata":
            slow_print("\nApri la porta forzata. L'odore di decomposizione ti assale.")
            dialogue("Tu", "Gesù, guarda lo stato di questo posto.")
            dialogue("Amico", "Non so nemmeno che tipo di entità abbiano le ossa che sto iniziando a vedere.")
            dialogue("Tu", "Pensi che una di queste sia uno smiler?")
            dialogue("Amico", "Non c'è modo che lo siano, sono solo facce fluttuanti... giusto?")
        
        elif choice == "corridoio":
            slow_print("\nTi avventuri nel lungo corridoio. Le pareti sono graffiate, segni di disperazione.")
            dialogue("Tu", "Quindi... questo è. La porta del corridoio.")
            dialogue("Amico", "Pensi che sia davvero lungo dieci chilometri come dice?")
            dialogue("Tu", "Hah, cazzo no. Non mi interessa quanto sia atletica una persona, nessuno potrebbe sopravvivere a quella merda.")
            
            slow_print("\nCamminate per un po' nel corridoio...")
            dialogue("Amico", "Ehi... riguardo a quella tua teoria.")
            dialogue("Tu", "È ancora nella tua mente?")
            dialogue("Amico", "Beh, sì. Diventa più pesante più ci pensi.")
            dialogue("Tu", "Oh dio, dove l'hai portata?")
            dialogue("Amico", "Se, diciamo, la tua teoria regge... può applicarsi a qualsiasi cosa?")
            
            choice = make_choice(["conforta", "esplora"])
            if choice == "conforta":
                dialogue("Tu", "Ehi, ascoltami. La mia teoria è solo una teoria, okay? Non la rende reale, o niente del tutto.")
                dialogue("Tu", "E se è giusta? Se le persone possono essere dimenticate come questo livello? Allora saremo dimenticati insieme.")
                dialogue("Amico", "Heh... è davvero dolce, in realtà... grazie. Ecco a noi, all'essere dimenticati.")
            else:
                slow_print("\nContinuate ad esplorare il corridoio...")
        
        elif choice == "rifletti":
            slow_print("\nTi fermi un momento a riflettere.")
            dialogue("Tu", "Sai, stavo pensando alla tua teoria.")
            dialogue("Amico", "Cosa ne pensi?")
            dialogue("Tu", "Pensi che... a volte potrebbe essere per il meglio?")
            dialogue("Amico", "In che senso?")
            dialogue("Tu", "Come una fenice! Potrebbero morire, ma rinascono di nuovo, forse anche meglio di prima!")
            dialogue("Amico", "Huh. Questo è... incredibilmente ottimista da parte tua! Posso essere d'accordo con questo sentimento.")

        slow_print("\nVedi una luce in lontananza. Sembra essere l'uscita del corridoio.")
        choice = make_choice(["esci", "torna indietro"])
        if choice == "esci":
            dialogue("Tu", "Quindi cosa pensi ci sia oltre l'uscita qui?")
            dialogue("Amico", "Chi lo sa? Non ci sto pensando troppo. Inoltre... qualunque cosa accada, l'affronteremo.")
            dialogue("Tu", "Insieme?")
            dialogue("Amico", "Sì. Insieme.")
            slow_print("\nAttraversate la luce insieme, verso l'ignoto...")
            slow_print("Fine del gioco.")
            return

if __name__ == "__main__":
    slow_print("Benvenuto nel livello dimenticato delle Backrooms.")
    slow_print("Un luogo di leggende dimenticate e storie distorte.")
    game()