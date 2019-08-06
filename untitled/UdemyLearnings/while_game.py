import random
initial = int(input("please enter initial number : "))
highest = int(input("please select highest number : "))
answer = random.randint(initial, highest)
print ("please guess a number between {} and {} : " .format(initial, highest))
guess = 0
while guess != answer:
    guess = int(input())
    if guess > answer:
        print("please select lower number : ")
    elif guess < answer:
        print("please select higher number : ")
    else:
        print("congratulations you guessed it")
