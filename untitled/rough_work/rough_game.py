import random
initial = int(input("please enter your first number :"))
final = int(input("please enter your second number :"))
a = random.randint(initial, final)
guess = 0
b = " "
while guess != a:
    guess = int(input("please guess a number : " ))
    if guess > a:
        print ("please select a lower number")
    elif guess < a:
        print ("please select a greater number")
    else:
        print("congrats you made it")




"""
    if guess > a:
        print ("please select smaller")
    elif guess < a:
        print ("please select a greater number")
    else:
        print("congratulations you made it!!")
"""