def augmente_liste(liste):
  for i, element in enumerate(liste):
    liste[i] = element + 1

L = [7, 11, 42, 39, 2]
augmente_liste(L)
print(L)
