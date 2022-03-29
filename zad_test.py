for liczba in range(0,101):
    if liczba % 3 == 0 and liczba % 5 == 0:
        print("FuzzBuzz")
    elif liczba % 5 == 0:
        print('Buzz')
    elif liczba % 3 == 0:
        print('Buzz')
    else: print(liczba)
