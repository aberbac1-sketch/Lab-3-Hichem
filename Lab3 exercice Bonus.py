
# Classe Player

class Player:

    def __init__(self, name):
        self.name = name
        self.kills = 0
        self.deaths = 0
        self.assists = 0
        self.money = 0

    def add_kill(self):
        self.kills += 1

    def add_death(self):
        self.deaths += 1

    def add_assist(self):
        self.assists += 1

    def earn_money(self, amount):
        self.money += amount

    def spend_money(self, amount):

        # Vérifier si le joueur possède assez d'argent
        if amount <= self.money:
            self.money -= amount

        else:
            print(self.name, "ne peut pas depenser en euros", amount,
                  ": argent insuffisant")

    # Calcul du ratio K/D
    def get_kd_ratio(self):

        # Éviter la division par zéro
        if self.deaths == 0:
            return self.kills

        else:
            return self.kills / self.deaths


# Classe Team

class Team:

    def __init__(self, name):
        self.name = name
        self.players = []
        self.score = 0

    # Ajouter un joueur
    def add_player(self, player):

        # Vérifier le nombre maximum de joueurs
        if len(self.players) < 5:
            self.players.append(player)

        else:
            print("L'équipe est déjà complète.")

    # Ajouter un point à l'équipe
    def win_round(self):
        self.score += 1

    # Calcul du total des éliminations
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
        print("Total des eliminations :", self.get_total_kills())

        print("\nListe des joueurs :")

        for player in self.players:

            print(player.name,
                  "- Eliminations :", player.kills,
                  "- Morts :", player.deaths,
                  "- Assistances :", player.assists,
                  "- Argent en euros:", player.money,
                  "- Ratio K/D :", player.get_kd_ratio())


# Classe Match

class Match:

    def __init__(self, team1, team2):

        self.team1 = team1
        self.team2 = team2
        self.round_number = 0

    # Jouer une manche
    def play_round(self, winning_team):

        self.round_number += 1
        winning_team.win_round()

    # Afficher le score du match
    def show_score(self):

        print("\n----- Score du match -----")
        print("Nombre de manches :", self.round_number)

        print(self.team1.name, ":", self.team1.score)
        print(self.team2.name, ":", self.team2.score)

    # Retourner le gagnant
    def get_winner(self):

        if self.team1.score > self.team2.score:
            return self.team1.name

        elif self.team2.score > self.team1.score:
            return self.team2.name

        else:
            return "Égalité"

    # Résumé complet du match
    def print_match_summary(self):

        print("\n========== RESUME COMPLET DU MATCH ==========")

        self.show_score()

        print("Gagnant :", self.get_winner())

        self.team1.get_team_stats()
        self.team2.get_team_stats()


# Création des équipes
team1 = Team("JSK")
team2 = Team("MCA")

# Création des joueurs JSK
p1 = Player("Gaya")
p2 = Player("Hamidi")
p3 = Player("Bada")
p4 = Player("Aymen")
p5 = Player("Sarr")

# Création des joueurs MCA
p6 = Player("Ali")
p7 = Player("Karim")
p8 = Player("Omar")
p9 = Player("Yacine")
p10 = Player("Mehdi")

# Ajouter les joueurs dans les équipes
team1.add_player(p1)
team1.add_player(p2)
team1.add_player(p3)
team1.add_player(p4)
team1.add_player(p5)

team2.add_player(p6)
team2.add_player(p7)
team2.add_player(p8)
team2.add_player(p9)
team2.add_player(p10)

# Statistiques des joueurs JSK
p1.add_kill()
p1.add_kill()

p2.add_kill()
p2.add_assist()

p3.add_kill()
p3.add_assist()

p4.add_kill()
p4.add_kill()
p4.add_kill()

p5.add_assist()

# Statistiques des joueurs MCA
p6.add_kill()
p6.add_death()

p7.add_kill()

p8.add_assist()

p9.add_kill()

# Gestion de l'argent
p1.earn_money(1000)
p1.spend_money(400)

p6.earn_money(300)
p6.spend_money(500)

# Création du match
match = Match(team1, team2)

# JSK gagne 5 manches
for i in range(5):
    match.play_round(team1)

# Affichage du résumé complet
match.print_match_summary()