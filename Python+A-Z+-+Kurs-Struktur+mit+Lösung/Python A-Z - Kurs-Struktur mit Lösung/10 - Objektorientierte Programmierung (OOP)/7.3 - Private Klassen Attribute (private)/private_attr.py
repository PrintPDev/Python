'''

Mithilfe von Modifikations-Richtlinien kann versichert werden, dass Attribute 
kontrolliert und restriktiert werden können. 

Es gibt drei Modifikatoren: public, protected und private

Private: Private-Attribute können nur innerhalb der Klasse ereicht werden.

'''

class Person:
    __name = None
    __alter = None

    def __init__(self, name, alter):
        self.__name = name
        self.__alter = alter

    def daten_ausgeben(self):
        print('Mein Name ist: ', self.__name)
        print('Mein Alter ist: ', self.__alter)

    def daten_aendern(self, name, alter):
        self.__name = name
        self.__alter = alter


def main():
    p1 = Person('Saif', 27)
    p1.__name = 'Saif'
    p1.__alter = 27
    p1.daten_ausgeben()
    p1.daten_aendern('Jan', 25)
    p1.daten_ausgeben()


if __name__ == "__main__":
    main()
