import sys
try:
    text = input("Geben Sie bitte einen Text ein: \n")
    file = open("Beispiel.txt","w")
    file.write(text)
    file.close()
    print("Der Text wurde erfolgreich gespeichert")
except IOError:
    print("Datei kann nicht geöffnet werden")
except: print("Es ist folgender Fehler ausgetreten:",sys.exc_info()[0])