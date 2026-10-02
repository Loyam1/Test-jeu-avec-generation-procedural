from Chargement_sauvegarde import *
class Joueur (Chargement_sauvegarde):
  def __init__(self):
    super().__init__()
    self.pseudo=self.save["pseudo"]
    self.carburantT=self.save["carburantT"]
    self.argent = self.save["argent"]
    self.Ncarburant=self.save["Ncarburant"]
    self.amorti=self.save["amorti"]
    self.Namorti=self.save["Namorti"]
    self.Pcarburant = 16 / 3
    self.Pamorti = 30 / 7
    for i in range(0, self.Ncarburant):
      self.Pcarburant = round(self.Pcarburant * 1.5, 1)
    for i in range(0, self.Namorti):
      self.Pamorti = round(self.Pamorti * 1.4, 1)