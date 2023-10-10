
# Parent class 1
class Mitarbeiter():
   def __init__(self, name, gehalt, jobtitel): 
      self.name = name
      self.gehalt = gehalt
      self.jobtitel = jobtitel 

# Child-Class von Mitarbeiter
class TeamMitarbeiter(Mitarbeiter):
   def __init__(self, name, gehalt, jobtitel, aufgabe): 
      self.aufgabe = aufgabe
      super().__init__(name, gehalt, jobtitel)
  
# Child-Class von TeamMitarbeiter
class TeamLeiter(TeamMitarbeiter):
   def __init__(self, name, gehalt, jobtitel, aufgabe, erfahrung): 
      self.erfahrung = erfahrung
      super().__init__(name, gehalt, jobtitel, aufgabe)
      print("Name: {}, Gehalt: {}, Erfahrung: {}".format(self.name, self.gehalt, self.erfahrung))

def main():
    john = TeamLeiter('John', 250000, 'Python Entwickler', 'Deep Learning', 5)

if __name__ == "__main__":
    main()