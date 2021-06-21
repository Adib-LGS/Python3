# Guess the right print_exception
def guess_price():
    enter_price = int(input("Choose a price between 1-1000: "))
    play = True 

    if 1000 >= enter_price >= 1:
        while play:
            if enter_price == 333:
                play = False
                print("you win")
                exit()
            elif enter_price <= 350 and enter_price >= 330:
                play
                print('Hot')
                enter_price = int(input("Choose a price between 1-1000: "))
            elif enter_price <= 330 or enter_price >= 350:
                play
                print('Cold')
                enter_price = int(input("Choose a price between 1-1000: "))
            else:
                enter_price = int(input("Choose a price between 1-1000: "))
    elif enter_price < 1:
        print('Only between 1 and 1000')
        enter_price = int(input("Choose a price between 1-1000: "))
guess_price()

