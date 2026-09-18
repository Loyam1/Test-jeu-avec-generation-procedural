import random
def chiffrement(key):
  random.seed(key)
  b=random.randint(10,100)
  a=0
  while not a==b:
    a+=1
    c=random.randint(0,1000000)
  random.seed(c)
  b = random.randint(10, 100)
  a = 0
  while not a == b:
    a += 1
    c = random.randint(0, 1000000)
  random.seed(c)
  b = random.randint(10, 100)
  a = 0
  while not a == b:
    a += 1
    c = random.randint(0, 10000000)
  print(c)
def chiffrement_mot_de_passe(mot_de_passe):
  convertion=""
  for i in mot_de_passe:
    convertion+=str(ord(i))
  convertion=int(convertion)
  chiffrement(convertion)
chiffrement_mot_de_passe("Mayol")
