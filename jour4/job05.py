# Création de la liste L
L = [1, 2, 3, 4, 5]

# Affiche la valeur de L[1]
print(L[1])

# Fonction qui remplace L[3] par la somme des cases voisines L[2] & L[4]
def remplacer_element(lst, index):
  lst[index] = lst[index-1] + lst[index+1]
  
# Exemple d'utilisation
remplacer_element(L,3)
print(L)


# Affiche la valeur du dernier terme de la liste
print(L[-1])

