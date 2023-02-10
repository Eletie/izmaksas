import biblioteka
from datetime import datetime


print("Labriit! Esi atvēris 100% vislabāko darbu, ko vien varējām izdarīt. Šeit saņemsiet visu ko jūs norādījāt specifikācijā <3")


class Rekins():
  def __init__(self, klients, veltijums, izmers, materials, laiks, aprekins):
    self.klients = klients
    self.veltijums = veltijums
    self.izmers = izmers
    self.materials = materials
    self.laiks = laiks
    self.aprekins = aprekins
    
  def RadaLaiku(self):
    currentDateAndTime = datetime.now()
    print("The current date and time is", currentDateAndTime)

    currentTime = currentDateAndTime.strftime("%H:%M:%S")
    print("The current time is", currentTime)
    
  def izdrukat(self):
    print("Rēķina info:\n","Vārds:", self.klients)
    print(" Veltījums:", self.veltijums)
    print(" Platums:", self.platums)
    print(" Garums:", self.garums)
    print(" Augstums:", self.augstums)
    print(" Materiāla cena:", self.materials)
    print(" Produkta cena:", self.aprekins)
    
    #un tā turpinat talak ez es gulet.

  def aprekins(self):
    darba_samaksa = 15
    PVN = 21
    teksta_garums = len(self.veltijums)
    #print("produkta cena: ", teksta_garums)
    p = int(self.platums)
    g = int(self.garums)
    a = int(self.augstums)
    m = int(self.materials)

    produkta_cena = int(teksta_garums) * 1.2 + (p/100 * g/100 * 
    a/100)/ 3 * m

    #print("produkta cena: ", produkta_cena)

    PVN_summa = int((produkta_cena + darba_samaksa)*PVN/100)

    rekina_summa = int((produkta_cena + darba_samaksa) + PVN_summa)

    self.aprekins = rekina_summa
    #print("produkta cena: ", round(produkta_cena, 2))
    #print("pvnsumma: ", PVN_summa)
    #print("Rēķina summa: ", rekina_summa)

    
  def saglabat(self):
    pass#saglaba visu csv, kas atrodas šaja class...


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
       if all(x.isalpha() or x.isspace() or x.isnumeric() for x in self.veltijums):
           break
       else:
           print("Ievadi veltijumu ar VARDIEM:)<3")  

    while True:
      self.garums = input("Ievadi garumu(veselu skaitli): ")  
      if all(x.isnumeric() for x in self.garums):
        break 
      else:
        print("Ievadi izmēru izmantojot tikai veselus skaitļus")

    while True:
      self.platums = input("Ievadi platumu(veselu skaitli): ")    
      if all(x.isnumeric() for x in self.platums):
        break 
      else:
        print("Ievadi izmēru izmantojot tikai veselus skaitļus")

    while True:
      self.augstums = input("Ievadi augstumu(veselu skaitli): ")    
      if all(x.isnumeric() for x in self.augstums):
        break 
      else:
        print("Ievadi izmēru izmantojot tikai veselus skaitļus")

        
    while True:
      self.materials = (input("Ievadi izmantojamā kokmateriāla cenu EUR/m^2: ")) 
      if all(x.isnumeric() for x in self.materials):
        break 
      else:
        print("Ievadi kokmateriala cenu ar cipariem<3")    

    
    

     #šeit ir problēmas, mana problema ka laiku jāciklē, jo jā un tagad ievadīšanā problēma.jo kad ievadu nepareizi platumu viss man prasa uzreiz materialus, nav labi.


  
  

Klients1 = Klients1() 

Klients1.RadaLaiku()

Klients1.aprekins()

Klients1.izdrukat()




#Vieta, kur nolikt kursoru:    


#es nezino ko darīt, sorry :(   #depresija #dead_inside #dumb_men