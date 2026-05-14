# Classe Player (joueur)

class Player:

    # Constructeur
    def __init__(self, name):
        self.name = name
        self.kills = 0
        self.deaths = 0
        self.assists = 0
        self.money = 0

    # Ajouter un kill
    def add_kill(self):
        self.kills += 1

    # Ajouter une mort
    def add_death(self):
        self.deaths += 1

    # Ajouter une assistance
    def add_assist(self):
        self.assists += 1

    # Ajouter de l'argent
    def earn_money(self, amount):
        self.money += amount

    # Dépenser de l'argent
    def spend_money(self, amount):
        if amount <= self.money:
            self.money -= amount
        else:
            print("Pas assez d'argent")

    # Calculer le ratio K/D
    def get_kd_ratio(self):
        if self.deaths == 0:
            return self.kills
        else:
            return self.kills / self.deaths


# Créer un joueur
player1 = Player("Hichem")

# Actions du joueur
player1.add_kill()
player1.add_kill()
player1.add_death()
player1.add_assist()

# Gestion de l'argent
player1.earn_money(1000)
player1.spend_money(400)

# Affichage des résultats
print("----- Statistiques du joueur -----")
print("Nom :", player1.name)
print("Kills :", player1.kills)
print("Deaths :", player1.deaths)
print("Assists :", player1.assists)
print("Argent en euros:", player1.money)
print("Ratio K/D :", player1.get_kd_ratio())