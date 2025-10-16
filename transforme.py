from time import *
from copy import *
from math import *
from trouve import *
def trensfo (block3,couche3,direction3):
  blockM3=block3
  blockF3={}
  blockDF3=[]
  for i in range(0,block3.index(block3[-1])+1):
    blockM3[i][1]=blockM3[i][1]-160
    blockM3[i][2]=blockM3[i][2]-91
    blockM3[i][1]=blockM3[i][1]//20
    blockM3[i][2]=blockM3[i][2]//-20
  if direction3=="D":
    for i in range(0,blockM3.index(blockM3[-1])+1):
      if blockM3[i][1]>=1 and blockM3[i][2]>=-2 and blockM3[i][2]<=2:
        blockDF3+=[blockM3[i]]
        blockDF3[blockDF3.index(blockDF3[-1])][2]+=1
        blockDF3[blockDF3.index(blockDF3[-1])][1]-=2
        couche3-=1
  if direction3=="G":
    print(blockM3)
    for i in range(0,blockM3.index(blockM3[-1])+1):
      if blockM3[i][1]<=-1 and blockM3[i][2]>=-2 and blockM3[i][2]<=2:
        blockDF3+=[blockM3[i]]
        blockDF3[blockDF3.index(blockDF3[-1])][2]+=1
        blockDF3[blockDF3.index(blockDF3[-1])][1]+=2
        couche3-=1
  if direction3=="H":
    for i in range(0,blockM3.index(blockM3[-1])+1):
      if blockM3[i][1]>=-2 and blockM3[i][1]<=2 and blockM3[i][2]>=1:
        blockDF3+=[blockM3[i]]
        blockDF3[blockDF3.index(blockDF3[-1])][2]-=2
        couche3+=2
  if direction3=="B":
    for i in range(0,blockM3.index(blockM3[-1])+1):
      if blockM3[i][1]>=-2 and blockM3[i][1]<=2 and blockM3[i][2]<=-1:
        blockDF3+=[blockM3[i]]
        blockDF3[blockDF3.index(blockDF3[-1])][2]+=2
        couche3-=2
  for i in range(0,blockDF3.index(blockDF3[-1])):
    temp3=(blockDF3[i][4])
    blockF3["{}".format([blockDF3[i][1],blockDF3[i][2]])]=[temp3,0]
  return [blockF3,couche3]


def detrensfo(blockF3,direction3,n3,couche3):
  blockDF3=[]
  for i in blockF3:
    blockDF3+=[eval(i)]
    blockDF3[-1]+=[blockF3[i]]
  if n3==1:
    if direction3=="D" or direction3=="G":
      for i in range(0,blockDF3.index(blockDF3[-1])+1):
        blockDF3[i][1]-=1
        couche3+=1
    if direction3=="H" or direction3=="B":
      for i in range(0,blockDF3.index(blockDF3[-1])+1):
        blockDF3[i][0]+=1
  elif n3==2:
    if direction3=="D" or direction3=="G":
      for i in range(0,blockDF3.index(blockDF3[-1])+1):
        blockDF3[i][1]-=1
        couche3+=1
    if direction3=="H" or direction3=="B":
      for i in range(0,blockDF3.index(blockDF3[-1])+1):
        blockDF3[i][0]-=2
  else:
    if direction3=="D" or direction3=="G":
      for i in range(0,blockDF3.index(blockDF3[-1])+1):
        blockDF3[i][1]+=1
        couche3-=1
    if direction3=="H":
      for i in range(0,blockDF3.index(blockDF3[-1])+1):
        blockDF3[i][0]+=1
        couche3-=2
    if direction3=="B":
      for i in range(0,blockDF3.index(blockDF3[-1])+1):
        blockDF3[i][0]+=1
        couche3+=2
  blockF3={}
  for i in range(0,blockDF3.index(blockDF3[-1])+1):
    temp3=(blockDF3[i][2])
    blockF3["{}".format([blockDF3[i][0],blockDF3[i][1]])]=temp3
  return [blockF3,couche3]


def detrensfofinal(blockF3,direction3):
  blockDF3=[]
  for i in blockF3:
    blockDF3+=[eval(i)]
    blockDF3[-1]+=blockF3[i]
  if direction3=="D":
    for i in range(0,blockDF3.index(blockDF3[-1])+1):
       blockDF3[i][0]+=2
       blockDF3[i][1]*=(-1)
  if direction3=="G":
    for i in range(0,blockDF3.index(blockDF3[-1])+1):
      blockDF3[i][0]-=2
      blockDF3[i][1]*=(-1)
  if direction3=="H":
    for i in range(0,blockDF3.index(blockDF3[-1])+1):
      blockDF3[i][1]-=2
  if  direction3=="B":
    for i in range(0,blockDF3.index(blockDF3[-1])+1):
      blockDF3[i][1]+=2
  blockM3=[]
  print(range(0,blockDF3.index(blockDF3[-1])))
  for i in range(0,blockDF3.index(blockDF3[-1])+1):
    blockM3+=deep_copy([blockDF3[i]])
    blockM3[i][0]*=20
    blockM3[i][1]*=20
    blockM3[i][0]+=160
    blockM3[i][1]+=91
  return blockM3