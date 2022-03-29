import math

bok_a= float(input("podaj długość boku a: "))
bok_b= float(input("podaj długość boku b: "))
bok_c= float(input("podaj długość boku c: "))

if ((bok_a +bok_b) > bok_c and (bok_a +bok_c) > bok_b and (bok_c +bok_b) > bok_a):
    pol_obw = (bok_a +bok_b +bok_c)/2
    pole = math.sqrt(pol_obw * (pol_obw - bok_a) + pol_obw * (pol_obw - bok_b) + pol_obw * (pol_obw - bok_c))
    print(f'pole trójkąta to: {pole:.2}')
else:
    print('nie jesteśmy na chwilę obecną zbudować żądany trókąt')