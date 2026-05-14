# Classe Team

class Team:

    # Constructeur de la classe
    def __init__(self, name):
        self.name = name
        self.score = 0

    # Ajouter un point à l'équipe
    def win_round(self):
        self.score += 1


# Classe Match

class Match:

    # Constructeur de la classe
    def __init__(self, team1, team2):
        self.team1 = team1
        self.team2 = team2
        self.round_number = 0
        self.max_rounds = 30

    # Jouer une manche
    def play_round(self, winning_team):

        # Ajouter une manche jouée
        self.round_number += 1

        # Ajouter un point à l'équipe gagnante
        winning_team.win_round()

    # Afficher le score du match
    def show_score(self):

        print("----- Score du match -----")
        print(self.team1.name, ":", self.team1.score)
        print(self.team2.name, ":", self.team2.score)

    # Vérifier si le match est terminé
    def is_match_over(self):

        if self.team1.score >= 5 or self.team2.score >= 5:
            return True

        return False

    # Retourner le gagnant du match
    def get_winner(self):

        if self.team1.score > self.team2.score:
            return self.team1.name

        elif self.team2.score > self.team1.score:
            return self.team2.name

        else:
            return "Égalité"


# Création des équipes
team1 = Team("JSK")
team2 = Team("MCA")

# Création du match
match1 = Match(team1, team2)

# JSK gagne 5 manches
for i in range(5):
    match1.play_round(team1)

# Affichage du score
match1.show_score()

# Vérifier si le match est terminé
print("Match termine :", match1.is_match_over())

# Afficher le gagnant
print("Gagnant du match :", match1.get_winner())