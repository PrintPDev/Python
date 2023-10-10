
# Parent class 2
class Mitarbeiter():                 
   def __init__(self, name, gehalt, jobtitel): 
      self.name = name
      self.gehalt = gehalt
      self.jobtitel = jobtitel

# Parent class 1
class TeamMitarbeiter():
   def __init__(self, aufgabe): 
      self.aufgabe = aufgabe
  
# Child-Class von TeamMitarbeiter
class TeamLeiter(TeamMitarbeiter, Mitarbeiter):         
   def __init__(self, name, gehalt, jobtitel, aufgabe, erfahrung): 
      self.erfahrung = erfahrung
      TeamMitarbeiter.__init__(self, aufgabe) 
      Mitarbeiter.__init__(self, name, gehalt, jobtitel)
      print("Name: {}, Gehalt: {}, Erfahrung: {}".format(self.name, self.gehalt, self.erfahrung))

def main():
    john = TeamLeiter('John', 250000, 'Python Entwickler', 'Deep Learning', 5)

if __name__ == "__main__":
    main()