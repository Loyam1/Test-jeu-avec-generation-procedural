import pickle
def new_save(file,carburantT=10,argent=0,Ncarburant=1,amorti=1,Namorti=1):
  save={"carburantT":carburantT,"argent":0,"Ncarburant":Ncarburant,"amorti":amorti,"Namorti":Namorti}
  with open(file, 'wb') as f:
    pickle.dump(save, f)
def load(file):
  try:
    f = open(file, "rb")
  except FileNotFoundError:
    new_save(file)
    f = open(file, "rb")
  save = pickle.load(f)
  f.close()
  return save
def save(file):
  save = {"carburantT": round(carburantT), "argent": round(argent, 1), "Ncarburant": round(Ncarburant),"amorti": round(amorti), "Namorti": round(Namorti)}
  with open('sauvegard.pkl', 'wb') as f:  # open a text file
    pickle.dump(save, f)
