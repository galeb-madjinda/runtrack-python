def augmente_liste(liste):
  # Parcours tous les éléments de la liste
  for i, element in enumerate(liste):
    # Augmente la valeur de l'élément de 1
    liste[i] = element + 1

# Exemple d'utilisation
L = [7, 11, 42, 39, 2]
augmente_liste(L)
print(L)
