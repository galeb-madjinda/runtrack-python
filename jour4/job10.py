def produit_intervalle(liste, debut, fin):
  produit = 1

  for element in liste:
    if debut <= element <= fin:
      produit *= element
  return produit

L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]
produit = produit_intervalle(L, 25, 90)
print(f"Le produit des valeurs de la liste L comprises entre 25 et 90 est {produit}.")
