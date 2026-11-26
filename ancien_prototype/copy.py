def deep_copy(sublist):
 #Fonction pour copier profondément une liste (et ses sous-listes).
    new_sublist = []
    for item in sublist:
        if isinstance(item, list):
            # Si l'élément est une liste, on copie aussi ses sous-éléments
            new_sublist.append(deep_copy(item))
        else:
            # Sinon, on copie simplement l'élément
            new_sublist.append(item)
    return new_sublist