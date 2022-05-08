def user_input():
    possible_answears = ['too big', 'too small', 'you won']
    while True:
        user_answear = input().lower()
        if user_answear in possible_answears:
            break
        print("Podaj prawidlowa wartosc")

    return user_answear


def guess_the_number():
    print("Pomysl liczbe od 0 do 1000, a ja ja zgadne w max. 10 probach")
    user_answear = ''
    number_min = 0
    number_max = 1000

    while user_answear != "you won":
        guess = (number_max - number_min) // 2 + number_min
        print(f"Your number is {guess}")
        user_answear = user_input()
        if user_answear == "too big":
            number_max = guess
        elif user_answear == "too small":
            number_min = guess
    print('I won!')


guess_the_number()