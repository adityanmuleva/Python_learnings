# name = input("please enter your name : ")
# age = int(input("hello " + name + " Pleas enter your age : "))
#
# if age > 18:
#     print("you are ready to vote")
# else:
#     print("please come back after %d years" % (18-age))

guess = int(input("please guess a number between 1 to 10 : "))
if guess < 5:
    print ("please guess higher")
    guess = int(input("please guess again : "))
    if guess == 5:
        print("well done you guessed it correctly")
    else:
        print("sorry you failed to guess")
elif guess > 5:
    print("please guess lesser")
    guess = int(input("please guess again : "))
    if guess == 5:
        print("congrats you made it")
    else:
        print("you cant guess")
else:
    print("you made it in first time")
