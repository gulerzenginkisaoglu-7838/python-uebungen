try:
    print("Programm zur Berechnung des Einkaufpreises")
    print("Bitte geben Sie folgende Werte ein:")
    anzahl = int(input("Anzahl der Artikel: "))
    preis = float(input("Preis pro Artikel: "))
    rabatt = float(input("Rabatt in Prozent: "))
    normal_preis = anzahl * preis
    gesamt_preis = normal_preis - (normal_preis * rabatt / 100)
    print( "Der Einkaufspreis beträgt: {0:.2f} Euro" .format(gesamt_preis))
except Exception as e:
    print( "Es ist folgender Fehler aufgetreten: \n" + e.args[0])
