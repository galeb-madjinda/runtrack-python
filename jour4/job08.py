def somme_valeurs_paires(liste):
  somme = 0
  for element in liste:
    if element % 2 == 0:
      somme += element
  return somme

L = [8, 24, 27, 48, 2, 16, 9, 7, 84, 91]
somme = somme_valeurs_paires(L)
print(f"La somme des valeurs paires de la liste L est {somme}.")
