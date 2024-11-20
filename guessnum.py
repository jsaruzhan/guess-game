import random

num = random.randint(1, 100)
i = 0

while i < 3:
    n = int(input("Guess the number between 1-100: "))
    if n == num:
        print("Congratulations! You have guessed correctly!")
        break
    elif n < num:
        print("You guessed wrong, but here is a hint: your number is smaller than the actual number.")
    elif n > num:
        print("You guessed wrong, but here is a hint: your number is larger than the actual number.")
    i += 1
    print("You have ", 3 - i, "tries left.")

if i == 3 and n != num:
    print("Sorry, you've used all your tries. The correct number was ", num)
