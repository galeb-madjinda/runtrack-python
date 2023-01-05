def maximum_minimum(liste):
  # Initialise le maximum et le minimum à la première valeur de la liste
  maximum = liste[0]
  minimum = liste[0]

  # Parcours tous les éléments de la liste à partir du second élément
  for element in liste[1:]:
    # Si l'élément est supérieur au maximum actuel, met à jour le maximum
    if element > maximum:
      maximum = element

    # Si l'élément est inférieur au minimum actuel, met à jour le minimum
    if element < minimum:
      minimum = element

  # Renvoie le maximum et le minimum
  return maximum, minimum

# Exemple d'utilisation
L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]
maximum, minimum = maximum_minimum(L)
print(f"Le maximum de la liste L est {maximum} et le minimum est {minimum}.")
