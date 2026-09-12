import sys
try:
    file = open("568 textdatei_lesen_K563.py","r")
    text = file.read()
    print(text)
    file.close()
except IOError:
    print("Datei kann nicht geöffnet werden")
except: print("Es ist folgender Fehler ausgetreten:",sys.exc_info()[0])
