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
    self.klients = str(input("Ievadi savu vardu: "))
    self.veltijums = str(input("Ievadi veltijumu: "))
    self.izmers = int(input("Ievadi izmeru(veselu skaitli): "))
    self.materials = str(input("Ievadi izmantojamo materialu: "))

Klients1 = Klients1()

#Vieta, kur nolikt kursoru:       