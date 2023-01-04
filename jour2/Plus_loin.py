def classify_triangle(a, b, c):
  if a + b > c and a + c > b and b + c > a:
    if a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or a**2 + c**2 == b**2:
      print("Le triangle est rectangle.")
    elif a == b and b == c:
      print("Le triangle est équilatéral.")
    elif a == b or b == c or a == c:
      print("Le triangle est isocèle.")
    else:
      print("Le triangle est quelconque.")
  else:
    print("Il n'est pas possible de construire un triangle avec ces longueurs.")

classify_triangle(3, 4, 5)
classify_triangle(5, 5, 5)
classify_triangle(2, 2, 3)
classify_triangle(5, 5, 7)
classify_triangle(1, 2, 3)
