import biblioteka
import time

print("Labriit! Esi atvēris mūsu 100% vislabāko darbu, ko vien varējām izdarīt. Šeit saņemsiet visu ko jūs norādījāt specifikācijā <3")


class Rekins():
  def __init__(self, klients, veltijums, izmers, materials, laiks):
    self.klients = klients
    self.veltijums = veltijums
    self.izmers = izmers
    self.materials = materials
    self.laiks = laiks
    
  def RadaLaiku(self):
    print("Rēķina ātrums: ", self.laiks)
    
  def izdrukat(self):
    pass

class Klients1(Rekins):
  def __init__(self):
    start = time.time()
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
       self.platums = int(input("Ievadi platumu(veselu skaitli): "))
       self.garmus = int(input("Ievadi garumu(veselu skaitli): "))
       self.augstums = int(input("Ievadi augstumu(veselu skaitli): "))
    except:
       print("Ievadi izmēru izmantojot tikai veselus skaitļus")
    
    try:
       self.materials = int(input("Ievadi izmantojamā kokmateriāla cenu EUR/m^2: "))
    except:
       print("Ievadi kokmateriala cenu ar cipariem<3")
    end = time.time()
    self.laiks = round(end - start, 2)


Klients1 = Klients1() 

Klients1.RadaLaiku()






#Vieta, kur nolikt kursoru:    


