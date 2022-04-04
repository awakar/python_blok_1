import random

licz_a = random.randint(1, 99)
licznik = 0
while True:
    liczba_zgad = int(input('Podaj liczbę: '))
    licznik +=1
    if liczba_zgad != licz_a:
        if liczba_zgad < licz_a:
            print('podana liczba jest mniejsza od wylosowanej liczby')
        elif liczba_zgad > licz_a:
            print('podana liczba jest większa od wylosowanej liczby')
    else:
        print('podałeś prawidłową liczbę')
        print(f'liczba prób do zgadnięcia to {licznik}')
        break