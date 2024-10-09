def getHamburgers(amount):
    print(f'Here are {amount} hamburgers')
    print('Thank you for stopping by')

want = input("What do you want?: ")

if want == "hamburgers":
    amount = int(input('How many?: '))
    getHamburgers(amount)
else:
    print("We don't have those.")
    print("You are an idiot.")