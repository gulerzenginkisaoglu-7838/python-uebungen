# ---------------------------------------------------------------
# Funktion zum Temperaturvergleich mit der langjährigen Mittel
# ---------------------------------------------------------------
def vergleiche_temperatur(temperatur):
    langjähriges_mittel = 18.23
    if temperatur >= langjähriges_mittel:
        if temperatur > langjähriges_mittel:
            return "Die Temperatur liegt über dem langjährigen Mittel"
        else:
            return "Die Temperatur entspricht dem langjährigen Mittel"
    else:
        return "Die Temperatur liegt unter dem langjährigen Mittel"

# ---------------------------------------------------------------
# Hauptfunktion des Programms
# ---------------------------------------------------------------
def main():
    try:
        print("Programm zur Berechnung einer Durchschnittstemperatur \n")
        print("Geben Sie bitte drei Temperaturwerte in °C ein!")
        temperatur1 = float(input("1. Wert: "))
        temperatur2 = float(input("2. Wert: "))
        temperatur3 = float(input("3. Wert: "))
        durchschnitt = (temperatur1 + temperatur2 + temperatur3) / 3
        print( "Sie haben folgende Temperaturen eingeben: {0} °C, {1} °C, {2} °C" .format(temperatur1,temperatur2,temperatur3))
        print( "Die Durchschnittstemperatur beträgt: {0:.2f} °C" .format(durchschnitt))
        text = vergleiche_temperatur(durchschnitt) # Funktionsaufruf
        print(text)
    except Exception as e:
        print("Es ist folgender Fehler aufgetreten: \n" + e.args[0])

main() # Aufruf der Hauptfunktion