
cena_ban = float(input("podaj cenę banów w zł za kg: "))
ban_ile = float(input("podaj ile chcesz zakupić bananów w kg: "))
cena_ziem = float(input("podaj cenę ziemniaków w zł za kg: "))
ziem_ile = float(input("podaj ile chcesz zakupić ziemniaków w kg: "))

zapl_ban = cena_ban * ban_ile
zapl_ziemn = cena_ziem + ziem_ile

print(f'do zapłaty  {zapl_ban+zapl_ziemn} zł')


if zapl_ban > zapl_ziemn:
    print('banany były droższe')
elif zapl_ban < zapl_ziemn:
    print("ziemniaki były droższe")
else:
    print("placisz tyle samo za oba produkty")
