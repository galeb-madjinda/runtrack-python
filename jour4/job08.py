def somme_valeurs_paires(liste):
  # Initialise la somme à 0
  somme = 0

  # Parcours tous les éléments de la liste
  for element in liste:
    # Si l'élément est pair, ajoute sa valeur à la somme
    if element % 2 == 0:
      somme += element

  # Renvoie la somme
  return somme

# Exemple d'utilisation
L = [8, 24, 27, 48, 2, 16, 9, 7, 84, 91]
somme = somme_valeurs_paires(L)
print(f"La somme des valeurs paires de la liste L est {somme}.")
