
#this function accepts the amount of hamburgers requested by the user and
#gives them those hamburgers 

def getHamburgers(amount):
    print(f'Here are {amount} hamburgers')
    print('Thank you for stopping by')

#first, getting the user's answer for what they want. We hope
#that it's hamburgers. At least I do. 

want = input("What do you want?: ")

#if the user wants hamburgers, we ask them how many
#and then give them the hamburgers they asked for. If not,
#we ridicule them.

if want == "hamburgers":
    amount = int(input('How many?: '))
    getHamburgers(amount)
else:
    print("We don't have those.")
    print("You are an idiot.")