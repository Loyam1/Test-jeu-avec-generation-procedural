import random
def chiffrement(key):
  random.seed(key)
  b=random.randint(10,100)
  a=0
  while not a==b:
    a+=1
    c=random.randint(0,1000)
  random.seed(c)
  b = random.randint(10, 100)
  a = 0
  while not a == b:
    a += 1
    c = random.randint(0, 1000)
  random.seed(c)
  b = random.randint(10, 100)
  a = 0
  while not a == b:
    a += 1
    c = random.randint(0, 1000)
  print(c)
chiffrement(2)