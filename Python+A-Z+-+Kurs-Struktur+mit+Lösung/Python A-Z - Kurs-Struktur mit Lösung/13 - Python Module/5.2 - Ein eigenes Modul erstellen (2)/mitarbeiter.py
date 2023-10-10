# Parent class 1
class Mitarbeiter(object):
   def __init__(self, name, gehalt, jobtitel): 
      self.name = name
      self.gehalt = gehalt
      self.jobtitel = jobtitel

   def daten_ausgeben(self):
      print("Name: {}, Gehalt: {}, Jobtitel: {}".format(self.name, self.gehalt, self.jobtitel))

# Child-Class von Mitarbeiter
class TeamMitarbeiter(Mitarbeiter):
   def __init__(self, name, gehalt, jobtitel, aufgabe): 
      self.aufgabe = aufgabe
      super().__init__(name, gehalt, jobtitel)

   def daten_ausgeben(self):
      print("Name: {}, Gehalt: {}, Aufgabe: {}".format(self.name, self.gehalt, self.aufgabe))

# Child-Class von TeamMitarbeiter
class TeamLeiter(TeamMitarbeiter):
   def __init__(self, name, gehalt, jobtitel, aufgabe, erfahrung): 
      self.erfahrung = erfahrung
      super().__init__(name, gehalt, jobtitel, aufgabe)

   def daten_ausgeben(self):
       
      print("Name: {}, Gehalt: {}, Erfahrung: {} Jahre".format(self.name, self.gehalt, self.erfahrung))