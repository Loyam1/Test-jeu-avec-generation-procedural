def plus():
  if not hasattr(plus,"a"):
    plus.a=1
  plus.a+=1
  return plus.a
print(plus())
print(plus())
print(plus())
print(plus())
print(plus())