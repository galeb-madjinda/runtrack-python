for i in range(2, 1001):
  nb_premiers = True
  for j in range(2, i):
    if i % j == 0:
      nb_premiers = False
      break
  if nb_premiers:
    print(i)
