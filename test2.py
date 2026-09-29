class Test():
  def __init__(self):
    self.test=1
    self.test2=2
    self.a()
  def ad(self,ch):
    self.ch+=1
  def a(self):
    self.ad("test")
    print(self.test)

Test()