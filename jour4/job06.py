def echange_premiere_derniere(liste):
  if len(liste) < 2:
    return

  liste[0], liste[-1] = liste[-1], liste[0]

ma_liste = [1, 2, 3, 4, 5]
echange_premiere_derniere(ma_liste)
print(ma_liste)
