def compte_multiples_de_3(liste):
  compteur = 0
  for element in liste:
    if element % 3 == 0:
      compteur += 1
  return compteur

L = [8, 24, 48, 2, 16]
nombre_multiples_de_3 = compte_multiples_de_3(L)
print(f"Le nombre de multiples de 3 dans la liste L est {nombre_multiples_de_3}.")
