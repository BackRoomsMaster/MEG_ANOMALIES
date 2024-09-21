from game_classes import Player, npcs
from enemies import enemies, final_boss
import random
import time

class Game:
    def __init__(self):
        self.player = None
        self.days_survived = 0
        self.hospital_integrity = 100
        self.npcs = npcs
        self.enemies = enemies
        self.final_boss = final_boss
        self.events = [
            self.entity_attack,
            self.find_supplies,
            self.repair_hospital,
            self.quiet_day,
            self.strange_noise,
            self.npc_conflict,
            self.memory_lapse,
            self.reality_shift
        ]

    def start_game(self):
        print("Benvenuto nelle Backrooms - Livello 14: L'Ospedale Militare")
        player_name = input("Inserisci il tuo nome: ")
        self.player = Player(player_name)
        self.main_loop()

    def main_loop(self):
        while True:
            self.days_survived += 1
            self.display_status()
            action = self.choose_action()
            self.perform_action(action)
            if self.check_game_over():
                break
            if self.days_survived % 10 == 0:
                self.boss_encounter()

    def display_status(self):
        print(f"\n{'=' * 40}")
        print(f"Giorno: {self.days_survived}")
        print(f"Salute: {self.player.health} | Sanità mentale: {self.player.sanity}")
        print(f"Munizioni: {self.player.ammo} | Forniture mediche: {self.player.medical_supplies}")
        print(f"Integrità dell'ospedale: {self.hospital_integrity}")
        print(f"{'=' * 40}")

    def choose_action(self):
        print("\nCosa vuoi fare?")
        print("1. Esplorare l'ospedale")
        print("2. Parlare con qualcuno")
        print("3. Usare forniture mediche")
        print("4. Riposare")
        print("5. Controllare l'inventario")
        print("6. Migliorare le abilità")
        return input("Scelta: ")

    def perform_action(self, action):
        if action == '1':
            self.explore()
        elif action == '2':
            self.talk()
        elif action == '3':
            self.use_medical_supplies()
        elif action == '4':
            self.rest()
        elif action == '5':
            self.check_inventory()
        elif action == '6':
            self.improve_skills()

    def check_game_over(self):
        if self.player.health <= 0:
            print("Sei morto. Game Over.")
            return True
        if self.hospital_integrity <= 0:
            print("L'ospedale è stato distrutto. Game Over.")
            return True
        return False

    def boss_encounter(self):
        print("\nATTENZIONE! Il Guardiano dell'Ospedale è apparso!")
        print(self.final_boss.description)
        while self.final_boss.health > 0 and self.player.health > 0:
            print("\n1. Attacca")
            print("2. Difendi")
            print("3. Usa oggetto")
            choice = input("Cosa vuoi fare? ")
            if choice == '1':
                damage = self.player.skills["combat"] * random.randint(10, 20)
                self.final_boss.health -= damage
                print(f"Hai inflitto {damage} danni al boss!")
            elif choice == '2':
                print("Ti prepari a difenderti.")
            elif choice == '3':
                self.use_item()
            else:
                print("Azione non valida.")
            
            if random.random() < 0.3:
                damage = self.final_boss.use_special_attack()
                print(f"Il boss usa il suo attacco speciale! Subisci {damage} danni!")
            else:
                damage = self.final_boss.attack()
                print(f"Il boss attacca! Subisci {damage} danni!")
            self.player.health -= damage

        if self.player.health <= 0:
            print("Sei stato sconfitto dal Guardiano dell'Ospedale. Game Over.")
        else:
            print("Hai sconfitto il Guardiano dell'Ospedale! Hai vinto!")

    def explore(self):
        print("\nTi avventuri nei corridoi bui e umidi dell'ospedale...")
        time.sleep(1)
        event = random.choice(self.events)
        event()

    def talk(self):
        print("\nCon chi vuoi parlare?")
        for i, npc in enumerate(self.npcs, 1):
            if npc.alive:
                print(f"{i}. {npc.name} ({npc.role})")
        choice = int(input("Scelta: ")) - 1
        if 0 <= choice < len(self.npcs) and self.npcs[choice].alive:
            self.dialogue(self.npcs[choice])
        else:
            print("Scelta non valida.")

    def dialogue(self, npc):
        print(f"\n{npc.name}: '{npc.get_dialogue()}'")
        print("1. Chiedi del suo passato")
        print("2. Chiedi consigli per sopravvivere")
        print("3. Offri il tuo aiuto")
        choice = input("Come vuoi rispondere? ")
        
        if choice == '1':
            print(f"\n{npc.name}: '{npc.backstory}'")
            self.player.sanity += 5
        elif choice == '2':
            if npc.role == "Medico":
                print(f"\n{npc.name}: 'Mantieni alta la tua sanità mentale. La mente è il nostro bene più prezioso qui.'")
            elif npc.role == "Soldato":
                print(f"\n{npc.name}: 'Tieni sempre d'occhio le tue munizioni e non abbassare mai la guardia.'")
            elif npc.role == "Tecnico":
                print(f"\n{npc.name}: 'Cerca di capire come funziona questo posto. Ogni informazione può essere vitale.'")
            else:
                print(f"\n{npc.name}: 'Restiamo uniti. La solitudine è il nostro peggior nemico qui.'")
            self.player.sanity += 10
        elif choice == '3':
            print(f"\n{npc.name}: 'Grazie, apprezzo il tuo aiuto. Siamo tutti sulla stessa barca qui.'")
            npc.trust += 15
            self.player.sanity += 5
        
        npc.trust += random.randint(1, 10)
        print(f"Il livello di fiducia di {npc.name} è aumentato.")

    def use_medical_supplies(self):
        if self.player.medical_supplies > 0:
            self.player.medical_supplies -= 1
            heal_amount = random.randint(20, 40)
            self.player.health = min(100, self.player.health + heal_amount)
        else:
            print("Non hai forniture mediche!")

    def rest(self):
        print("\nDecidi di riposare per un po'...")
        self.player.health = min(100, self.player.health + 10)
        self.player.sanity = min(100, self.player.sanity + 5)
        if random.random() < 0.3:
            self.nightmare()

    def nightmare(self):
        print("\nMentre dormi, hai un terribile incubo...")
        print("Ti ritrovi in un corridoio infinito, inseguito da ombre deformi...")
        print("Le pareti sembrano respirare e sussurrare il tuo nome...")
        print("Ti svegli di soprassalto, sudato e tremante.")
        self.player.sanity -= random.randint(5, 15)

    def check_inventory(self):
        if not self.player.inventory:
            print("\nIl tuo inventario è vuoto.")
        else:
            print("\nNel tuo inventario:")
            for item in self.player.inventory:
                print(f"- {item}")

    def improve_skills(self):
        print("\nQuale abilità vuoi migliorare?")
        print("1. Combattimento")
        print("2. Medicina")
        print("3. Tecnica")
        choice = input("Scelta: ")
        
        if choice == '1':
            self.player.skills["combat"] += 1
            print("Hai migliorato le tue abilità di combattimento!")
        elif choice == '2':
            self.player.skills["medical"] += 1
            print("Hai migliorato le tue abilità mediche!")
        elif choice == '3':
            self.player.skills["technical"] += 1
            print("Hai migliorato le tue abilità tecniche!")
        else:
            print("Scelta non valida.")

    def entity_attack(self):
        enemy = random.choice(self.enemies)
        print(f"\nATTENZIONE! Un {enemy.name} sta attaccando!")
        print(enemy.description)
        
        while enemy.health > 0 and self.player.health > 0:
            print("\n1. Combatti")
            print("2. Fuggi")
            choice = input("Cosa vuoi fare? ")
            
            if choice == '1':
                if self.player.ammo > 0:
                    damage = self.player.skills["combat"] * random.randint(5, 15)
                    self.player.ammo -= 1
                    enemy.health -= damage
                    print(f"Hai inflitto {damage} danni al {enemy.name}!")
                else:
                    print("Sei a corto di munizioni! Combatti corpo a corpo.")
                    damage = self.player.skills["combat"] * random.randint(1, 5)
                    enemy.health -= damage
                    print(f"Hai inflitto {damage} danni al {enemy.name}!")
                
                if enemy.health <= 0:
                    print(f"Hai sconfitto il {enemy.name}!")
                    self.player.sanity += 10
                    break
                
                enemy_damage = enemy.attack()
                self.player.health -= enemy_damage
                print(f"Il {enemy.name} ti ha inflitto {enemy_damage} danni!")
            
            elif choice == '2':
                if random.random() < 0.5:
                    print("Sei riuscito a fuggire!")
                    self.player.sanity -= 5
                    break
                else:
                    print("Non sei riuscito a fuggire!")
                    enemy_damage = enemy.attack()
                    self.player.health -= enemy_damage
                    print(f"Il {enemy.name} ti ha inflitto {enemy_damage} danni!")
            
            else:
                print("Scelta non valida.")

    def find_supplies(self):
        print("\nEsplorando una stanza abbandonata, trovi un nascondiglio segreto!")
        items = ["Munizioni", "Kit medico", "Cibo in scatola", "Batterie", "Diario misterioso"]
        found = random.sample(items, k=random.randint(1, 3))
        for item in found:
            if item == "Munizioni":
                amount = random.randint(10, 30)
                self.player.ammo += amount
                print(f"Hai trovato {amount} munizioni.")
            elif item == "Kit medico":
                self.player.medical_supplies += 1
                print("Hai trovato un kit medico.")
            else:
                self.player.inventory.append(item)
                print(f"Hai trovato: {item}")
        self.player.sanity += 5

    def repair_hospital(self):
        print("\nTrovi alcuni strumenti e materiali per riparare l'ospedale.")
        success = random.random() < 0.7 + (0.1 * self.player.skills["technical"])
        if success:
            repair_amount = random.randint(5, 15) + (5 * self.player.skills["technical"])
            self.hospital_integrity = min(100, self.hospital_integrity + repair_amount)
            print(f"Le tue riparazioni hanno avuto successo! L'integrità dell'ospedale è aumentata di {repair_amount}.")
            self.player.sanity += 10
        else:
            print("Purtroppo, le tue riparazioni non hanno avuto successo. Almeno non hai peggiorato la situazione.")
            self.player.sanity -= 5

    def quiet_day(self):
        print("\nOggi sembra essere una giornata tranquilla, per quanto possa esserlo qui...")
        print("L'incessante allarme continua a suonare in sottofondo, un promemoria costante della vostra situazione.")
        choice = input("Vuoi approfittarne per (R)iposare o (E)splorare con calma? ").lower()
        
        if choice == 'r':
            print("Decidi di concederti un po' di riposo. Ti senti leggermente rinvigorito.")
            self.player.health = min(100, self.player.health + 15)
            self.player.sanity = min(100, self.player.sanity + 10)
        elif choice == 'e':
            print("Esplori con calma i corridoi dell'ospedale, cercando di mappare meglio la zona.")
            if random.random() > 0.7:
                print("Hai scoperto un nuovo passaggio! Potrebbe essere utile in futuro.")
                self.player.sanity += 15
            else:
                print("Non trovi nulla di nuovo, ma almeno hai passato il tempo.")
                self.player.sanity += 5

    def strange_noise(self):
        print("\nAll'improvviso, senti un rumore inquietante provenire da una stanza vicina...")
        choice = input("Vuoi (I)ndagare o (I)gnorarlo? ").lower()
        
        if choice == 'i':
            print("Ti avvicini cautamente alla fonte del rumore...")
            if random.random() > 0.5:
                print("Trovi una strana entità che sta manipolando la struttura dell'ospedale!")
                combat_choice = input("Vuoi (A)ttaccare o (O)sservare? ").lower()
                if combat_choice == 'a':
                    if self.player.ammo >= 10:
                        self.player.ammo -= 10
                        print("Riesci a scacciare l'entità! L'ospedale sembra più stabile.")
                        self.hospital_integrity = min(100, self.hospital_integrity + random.randint(5, 15))
                        self.player.sanity += 10
                    else:
                        print("Non hai abbastanza munizioni! L'entità scompare, lasciandoti scosso.")
                        self.player.sanity -= 15
                else:
                    print("Osservi l'entità manipolare la realtà. È affascinante e terrificante allo stesso tempo.")
                    self.player.sanity -= random.randint(5, 20)
            else:
                print("Non trovi nulla di insolito. Forse la tua mente ti sta giocando brutti scherzi.")
                self.player.sanity -= 5
        else:
            print("Decidi di ignorare il rumore. Meglio non rischiare, ma l'incertezza ti tormenta.")
            self.player.sanity -= random.randint(5, 10)

    def npc_conflict(self):
        npc1, npc2 = random.sample(self.npcs, 2)
        print(f"\nScoppia un acceso litigio tra {npc1.name} e {npc2.name}!")
        print(f"{npc1.name}: 'Non possiamo continuare così! Le tue decisioni ci metteranno tutti in pericolo!'")
        print(f"{npc2.name}: 'E cosa proponi di fare? Le tue idee sono ancora peggiori!'")
        
        choice = input("Vuoi (I)ntervenire o (L)asciarli risolvere da soli? ").lower()
        
        if choice == 'i':
            print(f"{self.player.name}: 'Calmiamoci tutti. Dobbiamo restare uniti per sopravvivere.'")
            if random.random() > 0.6:
                print("Riesci a calmare gli animi. Il gruppo sembra più unito dopo questa prova.")
                self.player.sanity += 10
                npc1.trust += 5
                npc2.trust += 5
            else:
                print("Il tuo intervento sembra solo peggiorare le cose. Il litigio si intensifica.")
                self.player.sanity -= 10
                npc1.trust -= 5
                npc2.trust -= 5
        else:
            print("Decidi di non intervenire. Il litigio continua, creando tensione nel gruppo.")
            self.player.sanity -= 5

    def memory_lapse(self):
        print("\nAll'improvviso, ti rendi conto di non ricordare come sei arrivato qui...")
        print("I tuoi ricordi sembrano sfocati e confusi.")
        choice = input("Vuoi (C)ercare di ricordare o (D)istrarti con qualcos'altro? ").lower()
        
        if choice == 'c':
            if random.random() > 0.7:
                print("Riesci a recuperare alcuni ricordi. Ti senti più ancorato alla realtà.")
                self.player.sanity += 15
            else:
                print("Più ci provi, più i ricordi sembrano sfuggire. Ti senti disorientato.")
                self.player.sanity -= 10
        else:
            print("Decidi di concentrarti sul presente. Forse è meglio così.")
            self.player.sanity += 5

    def reality_shift(self):
        print("\nIl mondo intorno a te sembra... cambiare. Le pareti si muovono, i colori cambiano.")
        print("Per un momento, non sei sicuro di dove ti trovi o chi sei.")
        choice = input("Vuoi (A)ggrappati alla realtà o (L)asciarti andare? ").lower()
        
        if choice == 'a':
            if random.random() > 0.5:
                print("Con uno sforzo immane, riesci a mantenere la presa sulla realtà. Il mondo si stabilizza.")
                self.player.sanity += 20
            else:
                print("Nonostante i tuoi sforzi, la realtà continua a scivolare. Ti senti perso.")
                self.player.sanity -= 15
        else:
            if random.random() > 0.7:
                print("Ti lasci andare e... improvvisamente tutto ha un senso. Hai una nuova comprensione del luogo.")
                self.player.sanity += 30
                self.player.skills[random.choice(list(self.player.skills.keys()))] += 1
            else:
                print("Ti perdi nel flusso della realtà distorta. Quando torni in te, ti senti profondamente scosso.")
                self.player.sanity -= 25

    def use_item(self):
        if not self.player.inventory:
            print("Non hai oggetti da usare!")
            return
        
        print("Quale oggetto vuoi usare?")
        for i, item in enumerate(self.player.inventory, 1):
            print(f"{i}. {item}")
        
        choice = int(input("Scelta: ")) - 1
        if 0 <= choice < len(self.player.inventory):
            item = self.player.inventory.pop(choice)
            if item == "Cibo in scatola":
                self.player.health = min(100, self.player.health + 20)
                print("Hai mangiato il cibo. Ti senti meglio!")
            elif item == "Batterie":
                print("Hai usato le batterie per alimentare... qualcosa. Non sei sicuro di cosa, ma sembra importante.")
                self.player.sanity += 10
            elif item == "Diario misterioso":
                print("Leggi il diario. Contiene informazioni inquietanti sulle Backrooms, ma anche indizi utili.")
                self.player.sanity -= 5
                self.player.skills[random.choice(list(self.player.skills.keys()))] += 1
            else:
                print(f"Hai usato {item}, ma non sembra avere alcun effetto.")
        else:
            print("Scelta non valida.")

if __name__ == "__main__":
    game = Game()
    game.start_game()