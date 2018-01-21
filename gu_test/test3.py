class Marriage:
  #constructor __init__(argument,argument)
  def __init__(self,name1,birthdate1, name2, birthdate2,weddingDate,divorced):
    # instance variable person1, access person1, use self. in class
    self.person1 = Person(name1,birthdate1)
    self.person2 = Person(name2,birthdate2)

    self.weddingDate = weddingDate
    self.divorced = divorced
    #method printOutInfo
  def printOutInfo(self):
    divorced_condition = " and they are still married."
    #divorced is instance variable, access instance variable, use self. in class
    if self.divorced == True:
      divorced_condition = " and they are divorced"
    print(self.person1.name + ' married ' + self.person2.name + ' on the ' + self.weddingDate + divorced_condition)

class Person:
  def __init__(self, name,birthdate):
    self.name = name
    self.birthdate = birthdate

def findMarriage(inputName,register):
  result = None
  for item in register:
    if item.person1.name == inputName or item.person2.name == inputName:
      result = item
      break
  return result

def main():
  m0 = Marriage("Yifei", "8010102", "Chuan", "8001003", "890202", False)
  m1 = Marriage("Pelle Persson", "8010102", "Sara Sturesson", "8001003", "890202", False)
  m2 = Marriage("Stina Student", "8010102", "Sture Student", "8001003", "090101", True)

  register = [m0,m1,m2]

  answer = 'yes'
  print('Welcome to Who is Married to Who')

  while answer == 'yes':
    inputName = input("Input a name: ")
    result = findMarriage(inputName,register)
    if result == None:
      print("The are no " + inputName + " in the register.")
    else:
      result.printOutInfo()
    answer = input("Do you want to continue <yes/no>?")

  print('Welcome back.')

if __name__ == '__main__':
  main()
