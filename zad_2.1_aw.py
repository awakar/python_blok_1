import random

licz_a = random.randint(1, 99)
licz_b = random.randint(1, 99)

print(f'podaj sumę liczy {licz_a} a liczby {licz_b}')
while True:
    liczba = int(input('Podaj sumę podanych liczb: '))
    if liczba == licz_a + licz_b:
        print('podałeś prawidłową sumę')
        break
