wiek = int(input("Podaj swój wiek: "))
il_bilet = int(input("Podaj ile biletów chcesz zakupić: "))

if wiek < 7:
    cena_biletu = 0
elif wiek < 18:
    cena_biletu = 2.28
elif wiek < 65:
    cena_blietu = 3.8
else:
    cena_biletu = 1.9

cena = il_bilet * cena_biletu
print(f'cnea zakupu {il_bilet} biletów to {cena:.2f} zł.')
