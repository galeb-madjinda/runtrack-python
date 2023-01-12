def maximum_minimum(liste):
  maximum = liste[0]
  minimum = liste[0]
  
  for element in liste[1:]:
    if element > maximum:
      maximum = element
      
    if element < minimum:
      minimum = element
  return maximum, minimum

L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]
maximum, minimum = maximum_minimum(L)
print(f"Le maximum de la liste L est {maximum} et le minimum est {minimum}.")
