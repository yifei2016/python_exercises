class Marriage:
  #constructor __init__(argument,argument)
  def __init__(self,name1,birthdate1, name2, birthdate2,weddingDate):
    # instance variable person1, access person1, use self. in class
    self.person1 = Person(name1,birthdate1)
    self.person2 = Person(name2,birthdate2)

    self.weddingDate = weddingDate
    self.divorced = False
    #method printOutInfo
  def printOutInfo(self):
    divorced_condition = " and they are not divorced"
    #divorced is instance variable, access instance variable, use self. in class
    if self.divorced == True:
      divorced_condition = " and they are divorced"
    print(self.person1.name + ' married on the ' + self.weddingDate + ' with ' + self.person2.name + divorced_condition)
   

class Person:
  def __init__(self, name,birthdate):
    self.name = name
    self.birthdate = birthdate
   

m1 = Marriage("Karl Karlsson", "8010102", "Eva Evasdotter", "8001003", "090101")
m1.printOutInfo()
# access instance variable divorced, use instance of class m1
m1.divorced = True
m1.printOutInfo()