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
    print("Ievadi savu vardu???: ")
    self.klients = str(input())
    print("Ievadi veltījumu: ")
    self.veltijums = str(input())
    print("Ievadi izmēru(veselu skaitli):")
    self.izmers = int(input())
    print("Izmantojamais materiāls:")
    self.materials = str(input())


#Vieta, kur nolikt kursoru:       