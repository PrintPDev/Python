# Parent class 1
class Mitarbeiter(object):
   def __init__(self, name, gehalt, jobtitel, dienstwagen): 
      self.name = name
      self.gehalt = gehalt
      self.jobtitel = jobtitel
      self.dienstwagen = dienstwagen

   def daten_ausgeben(self):
      print("Name: {}, Gehalt: {}, Jobtitel: {}".format(self.name, self.gehalt, self.jobtitel))

# Child-Class von Mitarbeiter
class TeamMitarbeiter(Mitarbeiter):
   def __init__(self, name, gehalt, jobtitel, dienstwagen, aufgabe): 
      self.aufgabe = aufgabe
      super().__init__(name, gehalt, jobtitel, dienstwagen)

   def daten_ausgeben(self):
      print("Name: {}, Gehalt: {}, Aufgabe: {}".format(self.name, self.gehalt, self.aufgabe))

# Child-Class von TeamMitarbeiter
class TeamLeiter(TeamMitarbeiter):
   def __init__(self, name, gehalt, jobtitel, dienstwagen, aufgabe, erfahrung): 
      self.erfahrung = erfahrung
      super().__init__(name, gehalt, jobtitel, dienstwagen, aufgabe)

   def daten_ausgeben(self):       
      print("Name: {}, Gehalt: {}, Dienstwagen: {}, Erfahrung: {} Jahre".format(self.name, self.gehalt, self.dienstwagen.hersteller, self.erfahrung))