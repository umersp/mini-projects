import random
print("max limit = 10, means you have to guess between 0 to 10")
max_limit = input("Enter max limit number: ")

if max_limit.isdigit():
    max_limit = int(max_limit)

    if max_limit <= 0:
        print('Please type a number larger than 0 in next try.')
        quit()
else:
    print('Please type a number in next try.')
    quit()

random_no = random.randint(0, max_limit)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Please type a number next time.')
        continue

    if user_guess == random_no:
        print("You got it correct!")
        break
    elif user_guess > random_no:
        print("Try lower number")
    else:
        print("Try greater number")

print("You took", guesses, "guesses")