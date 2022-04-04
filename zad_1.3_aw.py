waga = float(input("podaj swoją wagę w kg: "))
wzrost = float(input("podaj swój wzrost w m: "))

bmi = waga/(wzrost*wzrost)

if bmi < 17 :
    print(f'Twóje BMI to {bmi:.2f} powinieneś udać się do najbliższego szpitala, stan zagrożenian życia')
elif bmi < 18:
        print(f'Twóje BMI to {bmi:.2f} powinieneś udać się do ian zacząć odżywiać, jesz zdecydowanie za mało')
elif bmi < 25:
        print(f'Twóje BMI to {bmi:.2f} nie wiem jak to zrobiłeś ale trzymaj tak dalej')
elif bmi < 30:
        print(f'Twóje BMI to {bmi:.2f} powinieneś udać się do najbliższą siłownię')
elif bmi < 35:
        print(f'Twóje BMI to {bmi:.2f} powinieneś udać się do najbliższego deitetyka ')
elif bmi < 17:
        print(f'Twóje BMI to {bmi:.2f} powinieneś przestać jeść')
else:
    print("to juz jest koniec i powinni Ci zabrać dużo tkanki tłuszcozewj")



