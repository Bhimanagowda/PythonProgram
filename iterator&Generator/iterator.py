class Topten:
  def __init__(self):
    self.num=1
    
  def __iter__(self):
    return self
  def __next__(self):
    if self.num<=10:
      val=self.num
      self.num+=1
      return val
    else:
      raise StopIteration
    
t1=Topten()
for i in t1:
  print(i)
      