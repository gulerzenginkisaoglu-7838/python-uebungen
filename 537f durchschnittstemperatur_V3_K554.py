try:
    print("Programm zur Berechnung einer Durchschnittstemperatur \n")
    print("Geben Sie bitte drei Temperaturwerte in °C ein!")
    temperatur1 = float(input("1. Wert: "))
    temperatur2 = float(input("2. Wert: "))
    temperatur3 = float(input("3. Wert: "))
    durchschnitt = (temperatur1 + temperatur2 + temperatur3) / 3
    print( "Sie haben folgende Temperaturen eingeben: {0} °C, {1} °C, {2} °C" .format(temperatur1,temperatur2,temperatur3))
    print( "Die Durchschnittstemperatur beträgt: {0:.2f} °C" .format(durchschnitt))
except Exception as e:
    print("Es ist folgender Fehler aufgetreten: \n" + e.args[0])