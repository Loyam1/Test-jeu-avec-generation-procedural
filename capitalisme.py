from kandinsky import *
from ion import *
from time import *
import kandinsky
from save_op import *
from op import *
from copy import *
import pickle
fill_rect(0,0,320,222,'black')
#texture
#set_pixel(10,10,kandinsky.color(255,255,0))
def visible (b):
  if b[1] <= -20 or b[1] >= 320 or b[2] <= -20 or b[2] >= 222:
    return False
  else:
    return  True
def joueur (cT,cR):
  fill_rect(150,101,20,20,'gray')
  fill_rect(151,102,18,18,kandinsky.color(107, 109, 109))
  fill_rect(152,103,16,16,'gray')
  if cR/cT*100>50:
    fill_rect(153,118,14,round(-(cR/cT*14)),'green')
  elif cR/cT*100>25:
    fill_rect(153,118,14,round(-(cR/cT*14)),'yellow')
  elif cR/cT*100>10:
    fill_rect(153,118,14,round(-(cR/cT*14)),'orange')
  else:
    fill_rect(153,118,14,round(-(cR/cT*14)),'red')

def Tbois (x,y):
  fill_rect(x-10,y+10,20,20,'brown')
  fill_rect(x-9,y+11,18,18,'orange')
  fill_rect(x-8,y+11,16,18,'brown')
  fill_rect(x-7,y+11,14,18,'orange')
  fill_rect(x-6,y+11,12,18,'brown')
  fill_rect(x-5,y+11,10,18,'orange')
  fill_rect(x-4,y+11,8,18,'brown')
  fill_rect(x-3,y+11,6,18,'orange')
  fill_rect(x-2,y+11,4,18,'brown')
  fill_rect(x-1,y+11,2,18,'orange')
def Bbois (x,y):
  block.append([1,x,y,1,Tbois,0.1])
def Tfeuille(x,y):
  fill_rect(x-10,y+10,20,20,'green')
  fill_rect(x-9,y+11,18,18,'white')
  for comt in range(0,325):
    if randint(0,2)<2:
      set_pixel(x-9+(round((comt/18-comt//18)*18)),y+11+comt//18,'green')
def Bfeuille(x,y):
  block.append([1,x,y,0.5,Tfeuille,choice([0,choice([0,0,0,0,2])])])
def Tair(x,y):
  fill_rect(x-10,y+10,20,20,'white')
def Bair(x,y):
  block.append([1,x,y,0,Tair,0])
def Techelle(x,y):
  fill_rect(x-10,y+10,20,20,kandinsky.color(85, 85, 129))
  fill_rect(x-8,y+12,16,3,'white')
  fill_rect(x-8,y+17,16,3,'white')
  fill_rect(x-8,y+22,16,3,'white')
  fill_rect(x-8,y+27,16,3,'white')
def Bechelle (x,y) :
  block.append([1,x,y,1,Techelle,0])
def Tterre(x,y):
  fill_rect(x-10,y+10,20,20,'black')
  fill_rect(x-9,y+11,18,18,'brown')
def Bterre(x,y):
  block.append ([1,x,y,1,Tterre,0])
def Menu(y,x):
  fill_rect(0,0,320-round(x*26/15),222,'black')
  fill_rect(0,105,320-round(x*26/15),30,'red')
  draw_string("{}@".format (argent),250-((2+len("{}".format(argent)))*5)-(x*2),10)
  draw_string("jouer",130-round(x*26/15),111+y)
  draw_string("stop",130-round(x*26/15),81+y)
  draw_string("magasin",130-round(x*26/15),141+y)
def magasin (y,x):
  fill_rect(300-x,0,170,222,'black')
  fill_rect(300-x,105,170,30,'red')
  draw_string("carburant {}@".format (Pcarburant),315-x,111+y)
  draw_string("amortie {}@".format (Pamorti),315-x,81+y)
  draw_string("rm",315-x,141+y)
#fin texture
def dico(block):
  blockM=[]
  ref={
  Tair:"Tair",
  Tbois:"Tbois",
  Techelle:"Techelle",
  Tfeuille:"Techelle",
  Tterre:"Tterre",
  "<function>":"tos"
  }
  for b in range(0,block.index(block[-1])):
    blockM+=deep_copy([block[b]])
    blockM[b][4]=ref.get(block[b][4],"no")
  return blockM
try:
  f=open("sauvegard.pkl", "rb")
except FileNotFoundError :
  save_game("sauvegard.pkl")
  f=open("sauvegard.pkl", "rb")
save = pickle.load(f)
f.close()
carburantT=save["carburantT"]
argent=save["argent"]
Ncarburant=save["Ncarburant"]
amorti=save["amorti"]
Namorti=save["Namorti"]
carburantR=carburantT
fin=1

parametre2=0
#Prix amelioration
Pcarburant=16/3
Pamorti=30/7
for i in range(0,Ncarburant):
  Pcarburant=round(Pcarburant*1.5,1)
for i in range(0,Namorti):
  Pamorti=round(Pamorti*1.4,1)
while fin!=2:
  if carburantR<=0:
    fin=1
  if fin==1:
    parametre=0
    Menu(0,0)
    while fin!=2:
      sleep(0.25)
      if keydown(KEY_UP):
        parametre+=1
        Menu(parametre*30,0)
      if keydown(KEY_DOWN):
        parametre-=1
        Menu(parametre*30,0)
      if keydown(KEY_RIGHT):
        if parametre==1:
          save={"carburantT":round(carburantT),"argent":round(argent,1),"Ncarburant":round(Ncarburant),"amorti":round(amorti),"Namorti":round(Namorti)}
          with open('sauvegard.pkl', 'wb') as f:  # open a text file
            pickle.dump(save, f)  # serialize the list
          exit(kandinsky)
        if parametre==0:
          fin=2
        if parametre==-1:
          for i in range(0,75):
            Menu(parametre*30,i)
            magasin(parametre2*30,i*2)
            sleep(0.06)
          while not keydown(KEY_LEFT):
            sleep(0.2)
            if keydown(KEY_DOWN):
              parametre2-=1
              magasin(parametre2*30,75*2)
            if keydown(KEY_UP):
              parametre2+=1
              magasin(parametre2*30,75*2)
            if keydown(KEY_RIGHT):
              if parametre2==0 and argent>=Pcarburant:
                Ncarburant+=1
                carburantT=carburantT*1.5
                argent-=Pcarburant
                Pcarburant=round(Pcarburant*1.5,1)
                magasin(parametre2*30,75*2)
              if parametre2==1 and argent>=Pamorti:
                Namorti+=1
                amorti+=1
                argent-=Pamorti
                Pamorti=round(round(Pamorti*1.4,1),1)
                magasin(parametre2*30,75*2)
              Menu(parametre*30,75)
              magasin(parametre2*30,75*2)
          for i in range(-75,0):
            Menu(parametre*30,i*-1)
            sleep(0.06)
    carburantR=carburantT
    block = [
    #[1,2,3,4,t5,6], 1=visible ou non, 2=x, 3=y, 4=durete, Tterre=texture, 6=argent, 7=famille
    [1,140,111,1,Tterre,0],
    [1,160,111,1,Tterre,0],
    [1,180,111,1,Tterre,0],
    [1,140,91,0,Tair,0],
    [1,140,71,0,Tair,0],
    [1,160,91,0,Tair,0],
    [1,160,71,0,Tair,0],
    [1,180,91,0,Tair,0],
    [1,180,71,0,Tair,0]
    ]
    fin=0
    couche=1
    fill_rect(0,0,320,222,'black')
    for b in block:
      if b[0]==1:
        b[4](b[1],b[2])
    joueur(carburantT,carburantR)
    sleep(0.5)
  if keydown(KEY_UP):
    carburantR-=1
    couche+=1
    block=[b for b in block if (b[1]!=160 or b[2]!=91)]
    Bechelle(160,91)
    argent+=[b for b in block if (b[1]==160 and b[2]==71)][0][5]
    block.remove([b for b in block if (b[1]==160 and b[2]==71)][0])
    Bair(160,71)
    tempo=opstart(dico(block),couche,"H")
    for i in tempo:
      eval(i)
    fill_rect(0,0,320,222,'black')
    for b in block:
      b[2]+=20
      tempo=visible(b)
      if tempo:
        b[4](b[1],b[2])
    joueur(carburantT,carburantR)
    sleep(0.2)
  if keydown(KEY_DOWN):
    carburantR-=1
    couche-=1
    argent+=[b for b in block if (b[1]==160 and b[2]==111)][0][5]
    block.remove([b for b in block if (b[1]==160 and b[2]==111)][0])
    Bair(160,111)
    tempo=opstart(dico(block),couche,"B")
    for i in tempo:
      eval(i)
    fill_rect(0,0,320,222,'black')
    for b in block:
      b[2]-=20
      tempo = visible(b)
      if tempo:
        b[4](b[1],b[2])
    joueur(carburantT,carburantR)
    sleep(0.2)
    chute=0
    while [b for b in block if (b[1]==160 and b[2]==111)][0][3]<1:
      chute+=1
      couche-=1
      tempo=opstart(dico(block),couche,"B")
      for i in tempo:
        eval(i)
      fill_rect(0,0,320,222,'black')
      for b in block:
        b[2]-=20
        tempo = visible(b)
        if tempo:
          b[4](b[1],b[2])
      joueur(carburantT,carburantR)
      sleep(0.2)
    if chute>amorti:
      fin=1
  if keydown(KEY_LEFT):
    carburantR-=1
    argent+=[b for b in block if (b[1]==140 and b[2]==91)][0][5]
    block.remove([b for b in block if (b[1]==140 and b[2]==91)][0])
    Bair(140,91)
    tempo=opstart(dico(block),couche,"G")
    for i in tempo:
      eval(i)
    fill_rect(0,0,320,222,'black')
    for b in block:
      b[1]+=20
      tempo = visible(b)
      if tempo:
        b[4](b[1],b[2])
    joueur(carburantT,carburantR)
    sleep(0.2)
    chute=0
    while [b for b in block if (b[1]==160 and b[2]==111)][0][3] <1:
      chute+=1
      couche-=1
      tempo=opstart(dico(block),couche,"B")
      for i in tempo:
        eval(i)
      fill_rect(0,0,320,222,'black')
      for b in block:
        b[2]-=20
        tempo = visible(b)
        if tempo:
          b[4](b[1],b[2])
      joueur(carburantT,carburantR)
      sleep(0.2)
    if chute>amorti:
      fin=1
  if keydown(KEY_RIGHT):
    carburantR-=1
    argent+=[b for b in block if (b[1]==180 and b[2]==91)][0][5]
    block.remove([b for b in block if (b[1]==180 and b[2]==91)][0])
    Bair(180,91)
    tempo=opstart(dico(block),couche,"D")
    for i in tempo:
      eval(i)
    print(block)
    fill_rect(0,0,320,222,'black')
    for b in block:
      b[1]-=20
      tempo = visible(b)
      if tempo:
        b[4](b[1],b[2])
    joueur(carburantT,carburantR)
    sleep(0.2)
    chute=0
    blocktempo=[b for b in block if (b[1]==160 and b[2]==111)][0]
    while blocktempo[3] <1:
      chute+=1
      couche-=1
      argent+=[b for b in block if (b[1]==180 and b[2]==91)][0][5]
      block.remove([b for b in block if (b[1]==180 and b[2]==91)][0])
      Bair(180,91)
      tempo=opstart(dico(block),couche,"B")
      for i in tempo:
        print(i)
        eval(i)
      print(block)
      fill_rect(0,0,320,222,'black')
      for b in block:
        b[2]-=20
        tempo = visible(b)
        if tempo:
          b[4](b[1],b[2])
      blocktempo=[b for b in block if (b[1]==160 and b[2]==111)][0]
      joueur(carburantT,carburantR)
    if chute>amorti:
      fin=1