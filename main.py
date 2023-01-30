import biblioteka

print("random suds ja")


class Rekins:
  def __init__(self, klients, veltijums, izmers, materials):
    self.klients = klients
    self.veltijums = veltijums
    self.izmers = izmers
    self.materials = materials

  def laiks(self):
    pass

  def izdrukat(self):
    pass

class Klients1(Rekins):
  def __init__(self):
    while True:
       self.klients = input("Ievadi savu vardu: ")
       if all(x.isalpha() or x.isspace() for x in self.klients):
           break
       else:
           print("Ievadu savu VARDU ar BURTIEM >:(")
    
    while True:
       self.veltijums = input("Ievadi veltijumu: ")
       if all(x.isalpha() or x.isspace() for x in self.veltijums):
           break
       else:
           print("Ievadi veltijumu ar VARDIEM:)<3")    
    try:
       self.izmers = int(input("Ievadi izmeru(veselu skaitli): "))
    except:
       print("Ievadi izmēru izmantojot tikai ciparus")
    
    while True:
       self.materials = input("Ievadi izmantojamo materialu: ")
       if all(x.isalpha() or x.isspace() for x in self.materials):
           break
       else:
           print("Ievadi ar burtiem nevis skaitliem <3") 

Klients1 = Klients1()

#Vieta, kur nolikt kursoru:       