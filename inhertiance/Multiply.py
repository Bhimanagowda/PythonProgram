class A:
  def feature1(self):
    print("Feature 1")
  def feature2(self):
    print("Feature 2")
    
class B:    #A extended to B
  def feature3(self):
    print("Feature 3")
  def feature4(self):
    print("Feature 4")
    
class C(A,B):    #B extended to C
  def feature5(self):
    print("Feature 5")
  def feature6(self):
    print("Feature 6")
    
a1=A()
a2=A()
b1=B()
b2=B()
c1=C()
c2=C()

print(c1.feature1())
print(c1.feature2())
print(c1.feature1())
print(c1.feature2())
print(c1.feature3())  #here B class extend A class features
print(c2.feature1())  #here B class extend A class features