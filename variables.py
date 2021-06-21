""" nom = 'Nom'
age = 27
print(nom + str(age))

def phrase(nom, age):
    print('Salut '  + nom  + " Tu as: " + str(age))

phrase(input('Entrez votre nom: '), input('Entrez votre age: '))"""

#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------

""" def monneyWallet(initial_value,amount):
    total = initial_value - amount
    spend_again = True

    if initial_value > amount:
        spend_again
        while spend_again:
            total -1
            print("Now you've got " + str(total) + "$")
            question = input("Another purchase  [yes/no]? ")
            
            if question == "yes":
                amount = int(input("How much do you wanna spend? "))
                if total >= amount:
                    total -= amount
                    print("New Purchase of " + str(amount) + "$," +  str(total) + "$ in your balance ")
                else:
                    print("Sorry you can't do this transaction, please fill your account")
                    exit()
            elif question == "no":
                print("See you Soon Consumer hahahaha")
                exit()

        if total < amount:
            spend_again = False
            print("You've reach your Spending Limit")
            exit()

    elif initial_value == amount:
        print('Done !, But you must drop some money in your account')
        exit()
    else:
        print('Hey Buddy you need a Black AMEX for that')
        exit()

monneyWallet(int(input("How much do you have in your wallet ? ")),int(input("How much do you wanna spend? ")))"""

#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------

""" def cinema_price(age = int, price_place = int, price_place2 = int):
    popcorn = 5
    
    if age < 5 or age > 100:
        print("NO your age doesn't permiss you to buy a ticket")
    elif age < 18:
        question = input('Do you want some pop-corn for 5$? [Yes/No] ')
        if question == "yes":
            price_place += popcorn
            print("You have to pay " + str(price_place) + "$")
        elif question == "no":
            price_place
            print("You have to pay " + str(price_place) + "$")
    elif age >= 18:
        price_place2
        question = input('Do you want some pop-corn for 5$? [Yes/No] ')
        if question == "yes":
            price_place2 += popcorn
            print("You have to pay " + str(price_place2) + "$")
        elif question == "no":
            price_place2
            print("You have to pay " + str(price_place2) + "$")
    else:
        print("No NO NO")
cinema_price(int(input('How old are you? ')), 7, 12)"""

#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------

