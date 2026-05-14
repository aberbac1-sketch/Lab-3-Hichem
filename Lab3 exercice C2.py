# Classe Team

class Team:

    # Constructeur de la classe
    def __init__(self, name):
        self.name = name
        self.players = []
        self.score = 0

    # Ajouter un joueur dans l'équipe
    def add_player(self, player):

        # Vérifier si l'équipe contient moins de 5 joueurs
        if len(self.players) < 5:
            self.players.append(player)

        else:
            print("L'équipe est déjà complète.")

    # Ajouter un point au score de l'équipe
    def win_round(self):
        self.score += 1

    # Calculer le nombre total de kills
    def get_total_kills(self):

        total = 0

        # Parcourir tous les joueurs de l'équipe
        for player in self.players:
            total += player.kills

        return total

    # Afficher les statistiques de l'équipe
    def get_team_stats(self):

        print("----- Statistiques de l'équipe -----")
        print("Nom de l'equipe :", self.name)
        print("Score :", self.score)
        print("Total des kills :", self.get_total_kills())

        print("\nListe des joueurs :")

        # Afficher les informations de chaque joueur
        for player in self.players:

            print(player.name,
                  "- Kills :", player.kills,
                  "- Deaths :", player.deaths,
                  "- Assists :", player.assists)


# Classe Player

class Player:

    # Constructeur de la classe
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


# Création des joueurs
player1 = Player("Gaya")
player2 = Player("Hamidi")
player3 = Player("Bada")
player4 = Player("Aymen")
player5 = Player("sarr")

# Actions des joueurs
player1.add_kill()
player1.add_kill()

player2.add_kill()
player2.add_assist()

player3.add_kill()
player3.add_assist()
player3.add_assist()

player4.add_kill()
player4.add_kill()
player4.add_kill()
player4.add_kill()
player4.add_assist()
player4.add_assist()

player5.add_assist()
player5.add_assist()



# Création de l'équipe
team1 = Team("JSK")

# Ajouter les joueurs dans l'équipe
team1.add_player(player1)
team1.add_player(player2)
team1.add_player(player3)
team1.add_player(player4)
team1.add_player(player5)
# L'équipe gagne une manche
team1.win_round()

# Affichage des statistiques de l'équipe
team1.get_team_stats()
