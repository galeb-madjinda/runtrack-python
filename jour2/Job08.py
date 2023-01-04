def list_produce(produce_type, saison):
  if produce_type == "fruits":
    
    if saison == "hiver":
      print("orange, mandarine et kiwi")

    elif saison == "ete":
      print("Poire, fraise, cassis")

  elif produce_type == "legume":
    if saison == "hiver":
      print("carotte, topinambour, endive")

    elif saison == "ete":
      print("artichaut, aubergine,navet")

list_produce("fruits", "hiver")
list_produce("fruits", "ete")
list_produce("legume", "hiver")
list_produce("legume", "ete")

