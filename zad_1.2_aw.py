dzien = int(input("podaj dzień kiedy oddałeś buty: "))
dlug_napr = int(input("podaj ile dni potrwa nawprawa: "))

if (dzien + dlug_napr) <= 7:
    dzien_oddania = dzien + dlug_napr
else:
    dzien_oddania = (dzien + dlug_napr) - ((dzien + dlug_napr)//7)*7

print(f"Dzień oddania butów to: {dzien_oddania}")
