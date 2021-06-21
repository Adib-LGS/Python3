from builtins import slice
from os.path import split
from random import shuffle

# When user is online / offline -- Add/RM pseudo in List  
list_pseudo = ['A', 'B', 'C', 'D']
new_pseudo = input('Choose your pseudo MDF: ')


print(list_pseudo[-1])

# insert manualy pseudo in list 
list_pseudo.insert(1, 'BBBB')

#eddit existing pseudo in list
list_pseudo[0] = 'AA'

# Add pseudo between 2 and 3 psoition in list
list_pseudo[2:3] = ['Add1', 'Add2'] 

# Add Pseudo input in list exentisible
list_pseudo.extend([new_pseudo])

for i in list_pseudo:
    print(i)

off = input('Do you want to quit [yes/no]? ')
if off == "yes":
    list_pseudo.remove(new_pseudo)
    for i in list_pseudo:
        print(i)
if off == "no":
    for i in list_pseudo:
        print(i) 

#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------



# When user is online / offline -- Add/RM pseudo in List  
def offLine_palayer():
    list_pseudo = ['Player1', 'Player2']
    new_pseudo = input('Choose your pseudo MDF: ')
    connected = True


    list_pseudo.extend([new_pseudo])
    for i in list_pseudo:
        print(i + "is now connected")
    while connected:
        question = input("Do you wanna quite Now?: [Yes/NO] ")
        if question == "yes":
            connected = False
            list_pseudo.remove(new_pseudo)
            print("Bye, bye, buddy")
            for i in list_pseudo:
                print(i + " still online")
        elif question == "no":
            for i in list_pseudo:
                print(i) 
offLine_palayer()
#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------

#Ask to enter somes words and show different elements depending of the length of the list
def random_words():
    str = input("Enter random words (word1/word2/word3/word4/word5) ").split("/")
    print(str)
    shuffle(str)
    print(str)
    if len(str) < 10:
        print(str[0:2])
    elif len(str) >= 10:
        print(str[-4: -1])
random_words()