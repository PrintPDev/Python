'''
Lass uns nun auch unsere Mitarbeiter und Fahrzeuge in separate Module auslagern!

'''

from fahrzeuge import SUV, Pickup, PKW
from mitarbeiter import TeamMitarbeiter, TeamLeiter

def main():
    benz_cla = PKW('Mercedes', 'CLA', 120, 'AMG line', sitzplaetze=4, kilometerstand=20000)
    benz_cla.daten_ausgeben()

    saif = TeamLeiter('Saif', 100000, 'ML Engineer', 'Deep Learning', 10)
    saif.daten_ausgeben()

if __name__ == "__main__":
    main()