wiek = int(input("Podaj swój wiek: "))
il_nocy = int(input("Podaj ile nocy chcesz zostać w hotelu: "))

if wiek < 18:
    cena_nocy = 100
else:
    if il_nocy == 1:
        cena_nocy = 200
    elif il_nocy < 5:
        cena_nocy = 180
    else:
        cena_nocy = 150

if wiek >= 65:
    cena_nocy *= 0.9
cena_pobytu = il_nocy * cena_nocy
print(f'cnea noclegu za {il_nocy} nocy to będzie: {cena_pobytu} zł.')
