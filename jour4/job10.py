def produit_intervalle(liste, debut, fin):
  # Initialise le produit à 1
  produit = 1

  # Parcours tous les éléments de la liste
  for element in liste:
    # Si l'élément est dans l'intervalle, multiplie le produit par sa valeur
    if debut <= element <= fin:
      produit *= element

  # Renvoie le produit
  return produit

# Exemple d'utilisation
L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]
produit = produit_intervalle(L, 25, 90)
print(f"Le produit des valeurs de la liste L comprises entre 25 et 90 est {produit}.")
