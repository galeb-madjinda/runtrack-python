# demande à l'utilisateur de saisir deux nombres
num1 = input("Entrez un premier nombre : ")
num2 = input("Entrez un deuxième nombre : ")

# convertit les nombres saisis en nombres flottants (au lieu de chaînes de caractères)
num1 = float(num1)
num2 = float(num2)

# effectue les opérations
somme = num1 + num2
soustraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2

# affiche les résultats
print(somme)
print(soustraction)
print(multiplication)
print(division)
