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


class PKW(Fahrzeug):
    variante = None
    sitzplaetze = 1

    def __init__(self, hersteller, modell, ps, variante, sitzplaetze = 1, kilometerstand = 0):
        super().__init__(hersteller, modell, ps, kilometerstand=kilometerstand)
        self.variante = variante # braucht keine property, weil nicht jedes Auto eine Variante hat.
        self.sitzplaetze = sitzplaetze
    
    @property
    def sitzplaetze(self):
        return self.__sitzplaetze

    @sitzplaetze.setter
    def sitzplaetze(self, sitzplaetze):
        if sitzplaetze < 1:
            raise ValueError('Es gibt keine Autos mit 0 Sitzplätze')
        self.__sitzplaetze = sitzplaetze

    def daten_ausgeben(self):
        super().daten_ausgeben()
        print('Variante: ', self.variante)
        print('Sitzplätze: ', self.__sitzplaetze)

class SUV(PKW):
    offroad_faehigkeit = False
    zuglast = 0

    def __init__(self, hersteller, modell, ps, variante, zuglast, offroad_faehigkeit = False, sitzplaetze=1, kilometerstand=0):
        super().__init__(hersteller, modell, ps, variante, sitzplaetze=sitzplaetze, kilometerstand=kilometerstand)

        if type(offroad_faehigkeit) != bool:
            raise ValueError('offroad_faehigkeit muss ein Bool sein')
        self.offroad_faehigkeit = offroad_faehigkeit

        if zuglast < 0:
            raise ValueError('Zuglast darf nicht < 0 sein')
        self.zuglast = zuglast

    def daten_ausgeben(self):
        super().daten_ausgeben()
        print('Offroad fähig ? ', self.offroad_faehigkeit)
        print('Zuglast: ', self.zuglast)



def main():
    benz_cla = Fahrzeug('Mercedes', 'CLA45', 385) # kilometerstand muss nicht angegeben werden, da neuwagen
    benz_cla.daten_ausgeben()
    print()
    fiat_500 = PKW('Fiat', '500', 75, '2-Türer', sitzplaetze=2, kilometerstand=25000)
    fiat_500.daten_ausgeben()
    print()
    audi_q8 = SUV('Audi', 'Q8', 290, 'Sline', 1000, offroad_faehigkeit=False, sitzplaetze=4)
    audi_q8.daten_ausgeben()


if __name__ == "__main__":
    main()