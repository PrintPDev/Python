class Fahrzeug():
    hersteller = None
    modell = None
    kilometerstand = 0
    ps = 0

    def __init__(self, hersteller, modell, ps, kilometerstand = 0):
        self.hersteller = hersteller
        self.modell = modell
        self.ps = ps
        self.kilometerstand = kilometerstand

    @property
    def hersteller(self):
        return self.__hersteller

    @hersteller.setter
    def hersteller(self, hersteller):
        if hersteller is None:
            raise ValueError('Hersteller muss gesetzt werden')
        self.__hersteller = hersteller

    @property
    def modell(self):
        return self.__modell

    @modell.setter
    def modell(self, modell):
        if modell is None:
            raise ValueError('Modell muss gesetzt werden')
        self.__modell = modell

    @property
    def ps(self):
        return self.__ps

    @ps.setter
    def ps(self, ps):
        if ps < 0:
            raise ValueError('PS darf nicht kleiner als 0 sein')
        self.__ps = ps
    
    @property
    def kilometerstand(self):
        return self.__kilometerstand

    @ps.setter
    def kilometerstand(self, kilometerstand):
        if kilometerstand < 0:
            raise ValueError('kilometerstand darf nicht kleiner als 0 sein')
        self.__kilometerstand = kilometerstand

    def daten_ausgeben(self):
        print('Fahrzeugdaten: ')
        print('Hersteller: ', self.hersteller)
        print('Modell: ', self.__modell)
        print('PS: ', self.__ps)
        print('Kilometerstand: ', self.__kilometerstand)

def main():
    benz_cla = Fahrzeug('Mercedes', 'CLA45', 385) # kilometerstand muss nicht angegeben werden, da neuwagen
    benz_cla.daten_ausgeben()



if __name__ == "__main__":
    main()