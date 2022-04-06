print(' '*6, end=' ')

for liczba_a in range(0,11):
    print(f' {liczba_a:5}', end="  ")
print()
print(

)
for liczba_a in range(0,11):
    print(f'{liczba_a:<5}', end='  ')
    for liczba_b in range(0,11):
        print(f' {liczba_a * liczba_b:5}', end="  ")
    print()
