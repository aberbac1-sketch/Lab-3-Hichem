# Classe Player

class Player:

    # Constructeur
    def __init__(self, name):
        self.name = name
        self.kills = 0
        self.deaths = 0
        self.assists = 0

    # Ajouter un kill
    def add_kill(self):
        self.kills += 1

    # Ajouter une mort
    def add_death(self):
        self.deaths += 1

    # Ajouter une assistance
    def add_assist(self):
        self.assists += 1


# Classe Team

class Team:

    # Constructeur
    def __init__(self, name):
        self.name = name
        self.players = []
        self.score = 0

    # Ajouter un joueur dans l'équipe
    def add_player(self, player):

        # Vérifier le nombre maximum de joueurs
        if len(self.players) < 5:
            self.players.append(player)

        else:
            print("L'équipe est déjà complète.")

    # Ajouter un point à l'équipe
    def win_round(self):
        self.score += 1

    # Calculer le total des kills
    def get_total_kills(self):

        total = 0

        # Parcourir les joueurs
        for player in self.players:
            total += player.kills

        return total

    # Afficher les statistiques de l'équipe
    def get_team_stats(self):

        print("\n----- Statistiques de l'equipe -----")
        print("Nom de l'equipe :", self.name)
        print("Score :", self.score)
        print("Total des kills :", self.get_total_kills())

        print("Liste des joueurs :")

        for player in self.players:

            print(player.name,
                  "- Kills :", player.kills,
                  "- Deaths :", player.deaths,
                  "- Assists :", player.assists)


# Classe Match

class Match:

    # Constructeur
    def __init__(self, team1, team2):

        self.team1 = team1
        self.team2 = team2
        self.round_number = 0

    # Jouer une manche
    def play_round(self, winning_team):

        self.round_number += 1
        winning_team.win_round()

    # Afficher le score
    def show_score(self):

        print("\n----- Score du match -----")
        print("Nombre de manches :", self.round_number)
        print(self.team1.name, ":", self.team1.score)
        print(self.team2.name, ":", self.team2.score)

    # Vérifier si le match est terminé
    def is_match_over(self):

        if self.team1.score >= 5 or self.team2.score >= 5:
            return True

        return False

    # Retourner le gagnant
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

# Création des joueurs JSK
p1 = Player("Gaya")
p2 = Player("Hamidi")
p3 = Player("Aymen")

# Création des joueurs MCA
p4 = Player("Ali")
p5 = Player("Karim")
p6 = Player("Omar")

# Ajouter les joueurs aux équipes
team1.add_player(p1)
team1.add_player(p2)
team1.add_player(p3)

team2.add_player(p4)
team2.add_player(p5)
team2.add_player(p6)

# Actions des joueurs JSK
p1.add_kill()
p1.add_kill()

p2.add_kill()
p2.add_assist()

p3.add_kill()
p3.add_kill()
p3.add_assist()

# Actions des joueurs MCA
p4.add_kill()

p5.add_assist()

p6.add_death()

# Création du match
match = Match(team1, team2)

# JSK gagne 5 manches
for i in range(5):
    match.play_round(team1)

# Afficher le score
match.show_score()

# Afficher les statistiques des équipes
team1.get_team_stats()
team2.get_team_stats()

# Afficher le gagnant
print("\nGagnant du match :", match.get_winner())