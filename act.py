from biblio import Employé

person_1 = Employé("h4cK3rM4n°4", 16, 100000, "Hackeur")

print(person_1.info_emp())
print(person_1.salaire_plus(100))
print(person_1.change_post("Directeur R&D"))
print(person_1.salaire_print())