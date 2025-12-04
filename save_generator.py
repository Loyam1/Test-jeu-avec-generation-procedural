import pickle
def new_save():
  save={"carburantT":10,"argent":0,"Ncarburant":1,"amorti":1,"Namorti":1}
  with open('sauvegard.pkl', 'wb') as f:
    pickle.dump(save, f)