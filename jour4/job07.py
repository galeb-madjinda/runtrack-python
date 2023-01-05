def compte_multiples_de_3(liste):
  # Initialise le compteur à 0
  compteur = 0

  # Parcours tous les éléments de la liste
  for element in liste:
    # Si l'élément est un multiple de 3, +1 au compteur
    if element % 3 == 0:
      compteur += 1

  # Renvoie le compteur
  return compteur

# Exemple d'utilisation
L = [8, 24, 48, 2, 16]
nombre_multiples_de_3 = compte_multiples_de_3(L)
print(f"Le nombre de multiples de 3 dans la liste L est {nombre_multiples_de_3}.")
