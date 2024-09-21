import random
import time
import sys

class Giocatore:
    def __init__(self):
        self.salute = 100
        self.sanita_mentale = 100
        self.inventario = []
        self.posizione = "Periferia"
        self.incontrato_entita_100 = False
        self.stabilita_core2 = 100
        self.conoscenza_meg = 0
        self.fiducia_meg = 50
        self.frammenti_mappa = 0
        self.chiave_uscita = False

class Luogo:
    def __init__(self, nome, descrizione, pericolo, opportunita):
        self.nome = nome
        self.descrizione = descrizione
        self.pericolo = pericolo
        self.opportunita = opportunita

class Entita:
    def __init__(self, nome, ostilita):
        self.nome = nome
        self.ostilita = ostilita

def stampa_lento(testo):
    for carattere in testo:
        sys.stdout.write(carattere)
        sys.stdout.flush()
        time.sleep(0.03)
    print()

def introduzione():
    stampa_lento("Benvenuto al Livello -998 delle Backrooms.")
    stampa_lento("Ti trovi in una realtà alterata, creata dall'Entità 100.")
    stampa_lento("L'ambiente è tossico e quasi impossibile da sopravvivere per gli umani.")
    stampa_lento("La tua missione: Esplorare, sopravvivere e trovare una via d'uscita.")
    stampa_lento("Dovrai viaggiare attraverso città abbandonate e villaggi misteriosi.")
    stampa_lento("Raccogli frammenti di mappa e cerca la chiave per l'uscita.")
    stampa_lento("Il M.E.G. (Major Explorer Group) ha una presenza significativa qui.")
    stampa_lento("Collabora con loro e con altre entità per aumentare le tue possibilità di sopravvivenza.")

def crea_mappa():
    return {
        "Città di Ruggine": Luogo("Città di Ruggine", "Una metropoli abbandonata con edifici arrugginiti e strade deserte.", "Interferenze elettroniche dannose", "Possibili risorse nascoste"),
        "Villaggio Sussurrante": Luogo("Villaggio Sussurrante", "Un piccolo insediamento dove i sussurri sembrano provenire dalle pareti.", "Attacchi psichici dei Sussurri", "Conoscenza arcana"),
        "Foresta di Cristallo": Luogo("Foresta di Cristallo", "Una foresta di alberi cristallizzati che riflettono una luce inesistente.", "Schegge di cristallo taglienti", "Cristalli curativi rari"),
        "Complesso Industriale Omega": Luogo("Complesso Industriale Omega", "Un vasto complesso industriale con macchinari ancora in funzione.", "Gas tossici", "Componenti per stabilizzare Core 2"),
        "Lago di Mercurio": Luogo("Lago di Mercurio", "Un lago di metallo liquido che riflette realtà distorte.", "Vapori tossici", "Metallo raro per equipaggiamento"),
        "Necropoli delle Cripte": Luogo("Necropoli delle Cripte", "Una città sotterranea abitata dalle misteriose Cripte.", "Trappole antiche", "Conoscenza segreta"),
        "Osservatorio dell'Entità 100": Luogo("Osservatorio dell'Entità 100", "Una struttura aliena da cui l'Entità 100 osserva il livello.", "Alterazioni della realtà", "Rivelazioni cosmiche"),
        "Base Principale M.E.G.": Luogo("Base Principale M.E.G.", "Il quartier generale del M.E.G. in questo livello.", "Esperimenti pericolosi", "Tecnologia avanzata e informazioni"),
        "Void Junction": Luogo("Void Junction", "Un nodo dove la realtà sembra assottigliarsi.", "Buchi nella realtà", "Possibile punto di uscita")
    }

def mostra_stato(giocatore):
    print(f"\nPosizione: {giocatore.posizione}")
    print(f"Salute: {giocatore.salute}%")
    print(f"Sanità Mentale: {giocatore.sanita_mentale}%")
    print(f"Stabilità Core 2: {giocatore.stabilita_core2}%")
    print(f"Conoscenza M.E.G.: {giocatore.conoscenza_meg}%")
    print(f"Fiducia M.E.G.: {giocatore.fiducia_meg}%")
    print(f"Frammenti di Mappa: {giocatore.frammenti_mappa}/5")
    print(f"Chiave Uscita: {'Sì' if giocatore.chiave_uscita else 'No'}")

def scegli_azione():
    print("\nCosa vuoi fare?")
    print("1. Esplorare la zona")
    print("2. Cercare risorse")
    print("3. Controllare l'inventario")
    print("4. Interagire con l'ambiente")
    print("5. Tentare di comunicare con le entità")
    print("6. Stabilizzare Core 2")
    print("7. Interagire con il M.E.G.")
    print("8. Viaggiare verso un'altra località")
    print("9. Tentare di uscire")
    return input("Scegli un'azione (1-9): ")

def esplora(giocatore, mappa):
    luogo_attuale = mappa[giocatore.posizione]
    stampa_lento(f"Stai esplorando: {luogo_attuale.nome}")
    stampa_lento(luogo_attuale.descrizione)
    
    if random.random() < 0.4:
        stampa_lento(f"Attenzione! {luogo_attuale.pericolo}!")
        danno = random.randint(5, 15)
        giocatore.salute -= danno
        giocatore.sanita_mentale -= danno // 2
        stampa_lento(f"Hai subito {danno} danni alla salute e {danno // 2} alla sanità mentale.")
    
    if random.random() < 0.3:
        stampa_lento(f"Hai trovato: {luogo_attuale.opportunita}!")
        if random.random() < 0.5:
            giocatore.inventario.append("Oggetto misterioso")
            stampa_lento("Hai ottenuto un oggetto misterioso.")
        else:
            recupero = random.randint(10, 20)
            giocatore.sanita_mentale += recupero
            stampa_lento(f"La tua sanità mentale è aumentata di {recupero}.")
    
    if random.random() < 0.2:
        giocatore.frammenti_mappa += 1
        stampa_lento("Hai trovato un frammento di mappa!")

def cerca_risorse(giocatore):
    risorse = ["Acqua Purificata", "Bende Mediche", "Batteria di Emergenza", "Razione M.E.G.", "Cristallo Energetico", "Componente di Core 2"]
    risorsa_trovata = random.choice(risorse)
    stampa_lento(f"Hai trovato: {risorsa_trovata}")
    giocatore.inventario.append(risorsa_trovata)
    
    if risorsa_trovata == "Acqua Purificata" or risorsa_trovata == "Razione M.E.G.":
        recupero = random.randint(5, 15)
        giocatore.salute += recupero
        stampa_lento(f"Hai recuperato {recupero} punti salute.")
    elif risorsa_trovata == "Cristallo Energetico":
        recupero = random.randint(10, 20)
        giocatore.sanita_mentale += recupero
        stampa_lento(f"La tua sanità mentale è aumentata di {recupero}.")
    elif risorsa_trovata == "Componente di Core 2":
        giocatore.stabilita_core2 += 10
        stampa_lento("La stabilità di Core 2 è aumentata del 10%.")

def controlla_inventario(giocatore):
    if giocatore.inventario:
        stampa_lento("Nel tuo inventario:")
        for oggetto in giocatore.inventario:
            stampa_lento(f"- {oggetto}")
    else:
        stampa_lento("Il tuo inventario è vuoto.")

def interagisci_ambiente(giocatore, mappa):
    luogo_attuale = mappa[giocatore.posizione]
    stampa_lento(f"Stai interagendo con l'ambiente di {luogo_attuale.nome}.")
    
    if luogo_attuale.nome == "Foresta di Cristallo":
        stampa_lento("Tocchi uno degli alberi cristallizzati. Senti una strana energia fluire attraverso di te.")
        giocatore.sanita_mentale += random.randint(5, 15)
        giocatore.salute -= random.randint(1, 5)
    elif luogo_attuale.nome == "Lago di Mercurio":
        stampa_lento("Ti avvicini al lago di mercurio. Le tue riflessioni mostrano versioni alternative di te stesso.")
        giocatore.sanita_mentale -= random.randint(5, 10)
        giocatore.conoscenza_meg += random.randint(1, 5)
    elif luogo_attuale.nome == "Complesso Industriale Omega":
        stampa_lento("Esamini i macchinari ancora in funzione. Scopri informazioni utili sul funzionamento di Core 2.")
        giocatore.stabilita_core2 += random.randint(5, 10)
    else:
        stampa_lento("Non trovi nulla di particolarmente interessante.")

def comunica_entita(giocatore):
    entita = [
        Entita("I Sussurri", 0.5),
        Entita("Le Cripte", 0.3),
        Entita("Entità 100", 0.1)
    ]
    entita_scelta = random.choice(entita)
    stampa_lento(f"Tenti di comunicare con {entita_scelta.nome}.")
    
    if random.random() < entita_scelta.ostilita:
        stampa_lento("L'entità reagisce in modo ostile!")
        giocatore.salute -= 20
        giocatore.sanita_mentale -= 15
    else:
        stampa_lento("L'entità sembra disposta a comunicare.")
        if entita_scelta.nome == "Entità 100":
            dialogo_entita_100(giocatore)
        elif entita_scelta.nome == "Le Cripte":
            dialogo_cripte(giocatore)
        else:
            stampa_lento("I Sussurri ti trasmettono visioni frammentarie del livello.")
            giocatore.sanita_mentale -= 10
            giocatore.conoscenza_meg += 5

def dialogo_entita_100(giocatore):
    giocatore.incontrato_entita_100 = True
    stampa_lento("L'Entità 100 si manifesta davanti a te, una presenza che sfida la comprensione.")
    stampa_lento("'Benvenuto, esploratore. Sei giunto in un luogo oltre la realtà che conosci.'")
    stampa_lento("'Questo livello è un esperimento, un crocevia tra dimensioni.'")
    stampa_lento("'Le leggi della fisica qui sono malleabili, il tempo è un concetto fluido.'")
    stampa_lento("'Core 2 è il cuore pulsante di questo luogo, mantienilo stabile o tutto collasserà.'")
    stampa_lento("'Cerca i frammenti di mappa, ti guideranno verso la verità e, forse, verso la libertà.'")
    stampa_lento("'Ma ricorda, la conoscenza ha un prezzo. Ogni rivelazione ti avvicinerà alla follia o all'illuminazione.'")
    giocatore.sanita_mentale -= 20
    giocatore.conoscenza_meg += 30

def dialogo_cripte(giocatore):
    stampa_lento("Le Cripte emergono dall'ombra, entità enigmatiche e antiche.")
    stampa_lento("'Viaggiatore, sei giunto nella terra tra i mondi.'")
    stampa_lento("'Noi siamo i custodi dei segreti di questo livello.'")
    stampa_lento("'Le città che vedi sono echi di realtà collassate, intrappolate in un limbo eterno.'")
    stampa_lento("'Core 2 è la chiave e la prigione. Stabilizzalo e potresti trovare la via d'uscita.'")
    stampa_lento("'Ma attento, poiché ogni passo verso la verità è un passo lontano dalla tua realtà.'")
    
    if "Oggetto misterioso" in giocatore.inventario:
        stampa_lento("Le Cripte notano l'oggetto misterioso nel tuo inventario.")
        stampa_lento("'Possiedi un artefatto di grande potere. Desideri scambiarlo per conoscenza?'")
        scelta = input("Accetti lo scambio? (si/no): ").lower()
        if scelta == "si":
            giocatore.inventario.remove("Oggetto misterioso")
            giocatore.conoscenza_meg += 20
            giocatore.sanita_mentale -= 10
            stampa_lento("Hai ottenuto conoscenza preziosa, ma a un costo per la tua sanità mentale.")
        else:
            stampa_lento("Le Cripte rispettano la tua decisione.")

def stabilizza_core2(giocatore):
    if giocatore.posizione != "Complesso Industriale Omega":
        stampa_lento("Devi essere nel Complesso Industriale Omega per stabilizzare Core 2.")
        return
    
    stampa_lento("Inizi il processo di stabilizzazione di Core 2.")
    if "Componente di Core 2" in giocatore.inventario:
        stampa_lento("Usi il Componente di Core 2 per migliorare il processo di stabilizzazione.")
        giocatore.inventario.remove("Componente di Core 2")
        aumento_stabilita = random.randint(15, 25)
    else:
        aumento_stabilita = random.randint(5, 15)
    
    giocatore.stabilita_core2 = min(100, giocatore.stabilita_core2 + aumento_stabilita)
    giocatore.salute -= random.randint(5, 10)
    stampa_lento(f"La stabilità di Core 2 è aumentata del {aumento_stabilita}%.")
    stampa_lento("Lo sforzo ha avuto un impatto sulla tua salute.")

def interagisci_meg(giocatore):
    if giocatore.posizione != "Base Principale M.E.G.":
        stampa_lento("Devi essere nella Base Principale M.E.G. per interagire direttamente con loro.")
        return

    print("\nCome vuoi interagire con il M.E.G.?")
    print("1. Richiedi informazioni")
    print("2. Offri assistenza")
    print("3. Richiedi supporto medico")
    print("4. Scambia risorse")
    scelta = input("Scegli un'opzione (1-4): ")

    if scelta == "1":
        stampa_lento("Richiedi informazioni al M.E.G. sulla situazione attuale.")
        giocatore.conoscenza_meg += 15
        stampa_lento("Hai appreso nuove informazioni cruciali sul livello -998.")
        stampa_lento("Il M.E.G. ti informa che l'uscita dal livello si trova probabilmente a Void Junction.")
        stampa_lento("Tuttavia, per accedervi, avrai bisogno di tutti i frammenti di mappa e della chiave d'uscita.")
    elif scelta == "2":
        stampa_lento("Offri il tuo aiuto al M.E.G. per le loro operazioni.")
        giocatore.fiducia_meg += 10
        giocatore.salute -= 10
        stampa_lento("Il M.E.G. apprezza il tuo aiuto, ma lo sforzo ti ha affaticato.")
        if giocatore.fiducia_meg >= 80 and not giocatore.chiave_uscita:
            stampa_lento("Come segno di fiducia, il M.E.G. ti consegna la chiave d'uscita!")
            giocatore.chiave_uscita = True
    elif scelta == "3":
        stampa_lento("Richiedi assistenza medica al M.E.G.")
        if giocatore.fiducia_meg >= 70:
            recupero = random.randint(20, 40)
            giocatore.salute = min(100, giocatore.salute + recupero)
            stampa_lento(f"Il M.E.G. ti fornisce cure avanzate. Recuperi {recupero}% di salute.")
        else:
            stampa_lento("Il M.E.G. ti offre cure di base. Recuperi 10% di salute.")
            giocatore.salute = min(100, giocatore.salute + 10)
    elif scelta == "4":
        if len(giocatore.inventario) > 0:
            oggetto = random.choice(giocatore.inventario)
            giocatore.inventario.remove(oggetto)
            stampa_lento(f"Hai scambiato {oggetto} con il M.E.G.")
            giocatore.conoscenza_meg += 10
            giocatore.fiducia_meg += 5
            stampa_lento("In cambio, hai ottenuto informazioni preziose e aumentato la fiducia del M.E.G.")
        else:
            stampa_lento("Non hai oggetti da scambiare.")

def viaggia(giocatore, mappa):
    print("\nDove vuoi viaggiare?")
    destinazioni = list(mappa.keys())
    for i, dest in enumerate(destinazioni, 1):
        print(f"{i}. {dest}")
    
    scelta = int(input("Scegli una destinazione: ")) - 1
    if 0 <= scelta < len(destinazioni):
        nuova_posizione = destinazioni[scelta]
        stampa_lento(f"Stai viaggiando verso {nuova_posizione}...")
        giocatore.posizione = nuova_posizione
        giocatore.salute -= random.randint(5, 15)
        giocatore.sanita_mentale -= random.randint(5, 10)
        stampa_lento("Il viaggio è stato faticoso e ha influito sulla tua salute e sanità mentale.")
    else:
        stampa_lento("Destinazione non valida.")

def tenta_uscita(giocatore):
    if giocatore.posizione != "Void Junction":
        stampa_lento("Devi essere a Void Junction per tentare l'uscita.")
        return False
    
    if giocatore.frammenti_mappa < 5:
        stampa_lento("Non hai raccolto tutti i frammenti di mappa necessari.")
        return False
    
    if not giocatore.chiave_uscita:
        stampa_lento("Non possiedi la chiave d'uscita.")
        return False
    
    stampa_lento("Hai tutti i requisiti per tentare l'uscita!")
    stampa_lento("Ti avvicini al punto in cui la realtà sembra più sottile...")
    stampa_lento("Usi i frammenti di mappa per orientarti e la chiave per aprire un varco...")
    
    if random.random() < 0.8:  # 80% di possibilità di successo
        return True
    else:
        stampa_lento("Qualcosa è andato storto. Il tentativo è fallito, ma almeno sei sopravvissuto.")
        giocatore.salute -= 20
        giocatore.sanita_mentale -= 20
        return False

def main():
    giocatore = Giocatore()
    mappa = crea_mappa()
    introduzione()
    
    while giocatore.salute > 0 and giocatore.sanita_mentale > 0:
        mostra_stato(giocatore)
        azione = scegli_azione()
        
        if azione == "1":
            esplora(giocatore, mappa)
        elif azione == "2":
            cerca_risorse(giocatore)
        elif azione == "3":
            controlla_inventario(giocatore)
        elif azione == "4":
            interagisci_ambiente(giocatore, mappa)
        elif azione == "5":
            comunica_entita(giocatore)
        elif azione == "6":
            stabilizza_core2(giocatore)
        elif azione == "7":
            interagisci_meg(giocatore)
        elif azione == "8":
            viaggia(giocatore, mappa)
        elif azione == "9":
            if tenta_uscita(giocatore):
                stampa_lento("Congratulazioni! Sei riuscito a fuggire dal Livello -998!")
                break
        else:
            stampa_lento("Azione non valida. Riprova.")
        
        if giocatore.stabilita_core2 <= 0:
            stampa_lento("Core 2 è diventato completamente instabile ed è esploso. Il livello sta collassando!")
            break
        
        # Limita i valori tra 0 e 100
        giocatore.salute = max(0, min(giocatore.salute, 100))
        giocatore.sanita_mentale = max(0, min(giocatore.sanita_mentale, 100))
        giocatore.stabilita_core2 = max(0, min(giocatore.stabilita_core2, 100))
        
    if giocatore.salute <= 0:
        stampa_lento("La tua salute è scesa a 0. Sei soccombuto agli pericoli del Livello -998.")
    elif giocatore.sanita_mentale <= 0:
        stampa_lento("La tua sanità mentale è crollata. Ti sei perso per sempre nelle distorsioni del Livello -998.")

if __name__ == "__main__":
    main()