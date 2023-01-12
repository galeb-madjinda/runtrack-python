L = [1, 2, 3, 4, 5]
print(L[1])

def remplacer_element(lst, index):
  lst[index] = lst[index-1] + lst[index+1]
  
remplacer_element(L,3)
print(L)

print(L[-1])

