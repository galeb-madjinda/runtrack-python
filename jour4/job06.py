def echange_premiere_derniere(liste):
  # Vérifie que la liste contient au moins deux éléments
  if len(liste) < 2:
    return

  # Échange les valeurs de la première et de la dernière case
  liste[0], liste[-1] = liste[-1], liste[0]

# Exemple d'utilisation
ma_liste = [1, 2, 3, 4, 5]
echange_premiere_derniere(ma_liste)
print(ma_liste)
