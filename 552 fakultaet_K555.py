def fakultaet(n):
    if n < 1:
        return 1
    return fakultaet (n-1)*n # hier ruft sich die Funktion selbst auf

print(fakultaet(4))
