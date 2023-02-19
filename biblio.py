class Employé:

    def __init__(self, nom, âge, salaire, poste):
        self.nom = nom
        self.âge = âge
        self.salaire = salaire
        self.poste = poste

    def info_emp(self):
        return ("Name: ", self.nom, "âge: ", self.âge, "salaire: ", self.salaire, "poste: ", self.poste)

    def salaire_plus(self, montant):
        self.salaire += montant
        return f"Le nouveau salaire de {self.nom} est de {self.salaire}"

    def salaire_print(self):
        return "Votre salaire actuelle est de: ", self.salaire

    def change_post(self, new_post):
        del self.poste
        self.poste = new_post
        return "Votre nouveau poste est: ", self.poste