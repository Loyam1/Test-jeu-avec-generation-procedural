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
