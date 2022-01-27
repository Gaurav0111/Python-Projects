import random


print("Here is a Stone paper scissor game ")
print("Its between you and computer")
def mygame(comp,user):
    if (comp==user):
        return None


    elif(comp == 'stone'):
        if(user == 'papper'):
            return True
        elif(user == 'scissor'):
            return False


    elif(comp == 'papper'):
        if(user == 'stone'):
            return False
        elif(user == 'scissor'):
            return True


    elif(comp == 'scissor'):
        if(user == 'papper'):
            return False
        elif(user == 'stone'):
            return True



Name = input("Enter your name buddy : ")
print("")
print(' Hey! {0} Welcome '.format(Name) )
print("")
print('This is a game beetween you and computer ' )
print("")
print("The rules of the game are as follows :" )
print(" You and computer have to make a choise " )
print(" Both of you will have have three options " )
print(" Remember !" )
print(" For choosing Stone press (s)" )
print(" For choosing Paper press (p)" )
print(" For choosing Scissor press (sc)" )
print("")
print(" And here you go " )
print("")
print('All the best {0}'.format(Name) )
print("")
print("Computer has made its descession ")
rand_no = random.randint(1,3)
if(rand_no==1):
    comp = 'stone'
elif(rand_no==2):
    comp = 'papper'
elif(rand_no==3):
    comp = 'scissor'

print("")
user = input("Enter your choise buddy: Stone(s) , Paper(p) , Scissor(sc) ? \n")
if(user=="s"):
    user = 'stone'
elif(user=="p"):
    user = 'papper'
elif(user=="sc"):
    user = 'scissor'
else:
    print("Enter a valid input")


result = mygame(comp,user)
print("")
print(f"Computer choose : {comp}")
print(f"You  choose : {user}")


if(result == None):
    print("You and computer choose same input")
    print("it was a tie")

elif (result == True):
    print(f'Hey {Name} you win !')

else:
    print(f'Sorry {Name} you loose !')






feed = input("")