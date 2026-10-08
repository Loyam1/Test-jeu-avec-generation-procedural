from Loging import *
class Chargement_sauvegarde(Loging):
  def __init__(self):
    super().__init__()
    self.file=f".sauvegarde/sauvegarde_{self.identifiant}.pkl"
    self.save=load(self.file)
    self.save["file"]=self.file
    self.save["pseudo"]=self.identifiant