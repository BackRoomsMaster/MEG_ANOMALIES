import random

class Puzzle:
    def __init__(self, name, description, difficulty):
        self.name = name
        self.description = description
        self.difficulty = difficulty

    def solve(self, player):
        print(f"Ti trovi di fronte a {self.name}.")
        print(self.description)
        solution = input("Qual è la tua risposta? ")
        if self.check_solution(solution):
            self.success(player)
        else:
            self.failure(player)

    def check_solution(self, solution):
        # Implementazione specifica per ogni puzzle
        pass

    def success(self, player):
        reward = self.difficulty * 5
        player.sanity += reward
        player.knowledge += self.difficulty
        print(f"Hai risolto il puzzle! Guadagni {reward} sanità e {self.difficulty} conoscenza.")

    def failure(self, player):
        penalty = self.difficulty * 3
        player.sanity -= penalty
        player.corruption += self.difficulty
        print(f"Non sei riuscito a risolvere il puzzle. Perdi {penalty} sanità e guadagni {self.difficulty} corruzione.")

class RiddleOfVoid(Puzzle):
    def check_solution(self, solution):
        return solution.lower() == "il void" or solution.lower() == "void"

class SymbolSequence(Puzzle):
    def __init__(self):
        super().__init__("Sequenza di Simboli", "Una serie di simboli alieni appare davanti a te. Devi completare la sequenza.", 2)
        self.sequence = [random.choice(["△", "◯", "□", "✧"]) for _ in range(4)]
        self.answer = random.choice(["△", "◯", "□", "✧"])
        self.description += f"\nSequenza: {' '.join(self.sequence)} ?"

    def check_solution(self, solution):
        return solution == self.answer

class MirrorPuzzle(Puzzle):
    def __init__(self):
        super().__init__("Enigma dello Specchio", "Uno specchio mostra il tuo riflesso, ma qualcosa non va...", 3)
        self.anomaly = random.choice(["occhi", "mani", "bocca", "orecchie"])
        self.description += f"\nCosa c'è di strano nel tuo riflesso?"

    def check_solution(self, solution):
        return self.anomaly in solution.lower()

puzzles = {
    "Enigma del Void": RiddleOfVoid("Enigma del Void", "Sono ovunque e in nessun luogo, tutto e niente. Cosa sono?", 1),
    "Sequenza di Simboli": SymbolSequence(),
    "Enigma dello Specchio": MirrorPuzzle()
}