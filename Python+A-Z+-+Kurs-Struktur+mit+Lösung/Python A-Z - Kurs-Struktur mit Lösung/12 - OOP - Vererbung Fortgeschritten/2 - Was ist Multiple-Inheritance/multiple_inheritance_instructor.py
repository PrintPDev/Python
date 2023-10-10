"""

In Python ist es auch möglich von mehreren Klassen zu erben. Allerdings gibt es dabei einiges zu beachten:

1. Multiple-Inheritance (auch mehrfache Vererbung) funktioniert ähnlich zu der einfachen Verbung
2. Die Syntax ist sehr ähnlich zu der uns bekannten Vererbung
3. Eigenschaften und Funktionen werde, wie gewohnt, vererbt.

Beispiel: 

Wir haben drei Entitäten: Mitarbeiter, Team-Mitarbeiter und Teamleiter

Wenn wir uns nur den Teamleiter anschauen: Er ist ein Mitarbeiter aber auch ein Team-Mitarbeiter. 

-> Das heißt er erbt von beiden Klassen!

"""

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