import random

licz_a = random.randint(1, 99)
licz_b = random.randint(1, 99)

print(f'wylosowano liczby {licz_a} i {licz_b}')
while True:
    suma = int(input('Podaj sumę podanych liczb: '))
    if suma == licz_a + licz_b:
        print('podałeś prawidłową sumę')
        break
