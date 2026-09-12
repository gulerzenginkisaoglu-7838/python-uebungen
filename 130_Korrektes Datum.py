
# Korrektes Datum

"""
Die Meyer GmbH benötigt ein Modul,
das ein beliebiges Datum auf Korrektheit prüft.
Ist das zu prüfende Datum korrekt,
so ist die Variable datum_ok auf 1, andernfalls auf 0
zu setzen.

Beispiele:

29.02:1999 - datum_ok: 0
29.02:2000 - datum_ok: 1
13.05.2000 - datum_ok: 1
32.05:2000 - datum_ok: 0
24.13:2000 - datum_ok: 0

Für die Jahre gilt: jahr > 1900 UND jahr < 2100
"""


# Eingabe
tag   = int(input("Tag  (TT): "))
monat = int(input("Monat (MM): "))
jahr  = int(input("Jahr (JJJJ): "))

Datum_ok = 1

# Jahr prüfen
if jahr <= 1900 or jahr >= 2100:
    Datum_ok = 0

# Monat prüfen
if monat < 1 or monat > 12:
    Datum_ok = 0

# Schaltjahr
if   jahr % 400 == 0:
     schaltjahr = True
elif jahr % 100 == 0:
     schaltjahr = False
elif jahr %   4 == 0:
     schaltjahr = True
else:
     schaltjahr = False

# Tage prüfen
if Datum_ok == 1:

# Monate mit 31 Tagen
 if monat in [1, 3, 5, 7, 8, 10, 12]:
    if tag < 1 or tag > 31:
        Datum_ok = 0

# Monate mit 30 Tagen
elif monat in [4, 6, 9, 11]:
    Datum_ok = 0

# Februar Wichtig 28? & 29?
elif monat == 2:
    if schaltjahr:
        if tag < 1 or tag > 29:
            Datum_ok = 0

else:
    if tag < 1 or tag > 28:
        Datum_ok = 0

# Ausgabe
print(f"\n{tag:02}.{monat:02}.{jahr} -> {Datum_ok}")










