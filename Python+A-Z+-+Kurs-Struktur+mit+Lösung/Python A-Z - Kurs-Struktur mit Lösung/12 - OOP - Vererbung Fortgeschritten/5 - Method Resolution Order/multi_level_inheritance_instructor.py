"""

Method Resolution Order (MRO) ist ein Ansatz, den eine Programmiersprache verwendet, 
um die Variablen oder Methoden einer Klasse aufzulösen.

Python hat eine eingebaute Basisklasse, die als Objekt bezeichnet wird. 
Jede andere eingebaute oder benutzerdefinierte Klasse, die Sie definieren, wird also irgendwann von ihr erben.

- Im Anwendungsfall der Mehrfachvererbung wird das Attribut zunächst in der aktuellen Klasse nachgeschlagen. 
Wenn dies fehlschlägt, wird als nächstes in der übergeordneten Klasse nachgeschlagen, und so weiter.
- Wenn es mehrere Elternklassen gibt, dann ist die Präferenzreihenfolge depth-first gefolgt von einem 
Links-Rechts-Pfad, d.h. DLR.
- MRO stellt sicher, dass eine Klasse immer vor ihren Elternklassen steht und bei mehreren Elternklassen 
die Reihenfolge als Tupel der Basisklassen beibehalten wird.

"""

# Parent class 1
class Mitarbeiter(object):
   def __init__(self, name, gehalt, jobtitel): 
      self.name = name
      self.gehalt = gehalt
      self.jobtitel = jobtitel

   def daten_ausgeben(self):
      print('Mitarbeiter wird ausgegeben')

# Child-Class von Mitarbeiter
class TeamMitarbeiter(Mitarbeiter):
   def __init__(self, name, gehalt, jobtitel, aufgabe): 
      self.aufgabe = aufgabe
      super().__init__(name, gehalt, jobtitel)

   def daten_ausgeben(self):
      print('TeamMitarbeiter wird ausgegeben')

# Child-Class von TeamMitarbeiter
class TeamLeiter(TeamMitarbeiter):
   def __init__(self, name, gehalt, jobtitel, aufgabe, erfahrung): 
      self.erfahrung = erfahrung
      super().__init__(name, gehalt, jobtitel, aufgabe)
      print("Name: {}, Gehalt: {}, Erfahrung: {}".format(self.name, self.gehalt, self.erfahrung))

   def daten_ausgeben(self):
      print('TeamLeiter wird ausgegeben')

def main():
    john = TeamLeiter('John', 250000, 'Python Entwickler', 'Deep Learning', 5)
    john.daten_ausgeben()

    # MRO von TeamLeiter in Multilevel-Inheritance
    print(TeamLeiter.mro())

if __name__ == "__main__":
    main()