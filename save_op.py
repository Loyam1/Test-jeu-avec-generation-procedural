import pickle
def save_game(file, carburantT=10, argent=0, Ncarburant=1, amorti=1, Namorti=1,hauteur_ecran=600,longueur_ecran=1200):
  save={"carburantT":carburantT,"argent":argent,"Ncarburant":Ncarburant,"amorti":amorti,"Namorti":Namorti,"hauteur_ecran":hauteur_ecran,"longueur_ecran":longueur_ecran}
  with open(file, 'wb') as f:
    pickle.dump(save, f)
def load(file):
  try:
    f = open(file, "rb")
  except FileNotFoundError:
    save_game(file)
    f = open(file, "rb")
  save = pickle.load(f)
  f.close()
  return save
def utilisateur(nom,mot_de_passe_chiffré):
  try:
    f = open("utilisateur.pkl", "rb")
  except FileNotFoundError:
    with open("utilisateur.pkl", 'wb') as f:
      pickle.dump({}, f)
    return [False,False]
  liste_utilisateur = pickle.load(f)
  if not liste_utilisateur.get(nom,"cet uttilisateur n'existe pas")=="cet uttilisateur n'existe pas":
    if liste_utilisateur[nom]==mot_de_passe_chiffré:
      return [True,True]
    else:
      return [True,False]
  else:
    return [False,False]
  f.close
def add_utilisateur(nom,mot_de_passe_chiffré):
  f = open("utilisateur.pkl", "rb")
  liste_utilisateur = pickle.load(f)
  f.close
  liste_utilisateur[nom] = mot_de_passe_chiffré
  with open("utilisateur.pkl", 'wb') as f:
    pickle.dump(liste_utilisateur, f)
