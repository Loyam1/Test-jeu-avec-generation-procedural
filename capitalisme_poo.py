from time import *
from save_op import *
from op import *
from copy import *
import pickle
import pygame
pseudo="Loyam"
file = "sauvegard_" + pseudo + ".pkl"
class Joueur ():
  def __init__(self,save):
    self.carburantT=save["carburantT"]
    self.argent = save["argent"]
    self.Ncarburant=save["Ncarburant"]
    self.amorti=save["amorti"]
    self.Namorti=save["Namorti"]




save=load(file)
joueur=Joueur(save)
print(joueur.argent)
to_save(file,joueur.carburantT,joueur.argent,joueur.Ncarburant,joueur.amorti,joueur.Namorti)