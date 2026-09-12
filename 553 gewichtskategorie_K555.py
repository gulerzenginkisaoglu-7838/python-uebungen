def ermittle_gewichtskategorie():
    try:
        bmi = float(input("Bitte geben Sie den BMI ein: "))
        if bmi < 18.5:
            print("Gewichtskategorie: Untergewicht")
        if bmi >= 18.5 and bmi < 25:
            print("Gewichtskategorie: Normalgewicht")
        if bmi >= 25 and bmi < 30:
            print("Gewichtskategorie: Übergewicht")
        if bmi >= 30:
            print("Gewichtskategorie: Adipositas")
    except Exception as e:
        print("Es ist folgender Fehler aufgetreten: \n" + e.args[0])

ermittle_gewichtskategorie()
