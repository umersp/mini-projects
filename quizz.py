print("---------")
print("---------")

print("Hello Player!")
score = 0

x = input("press S to start the quiz: ").lower()

if x == "s":
    que_one = input("Who is known as the FATHER of the nation? ")
    if que_one.lower() == "mahatma gandhi":
        print("Correct")
        score += 1
    else:
        print("Wrong")
        print("correct answer : Mahatma Gandhi ")
# -------------------
    que_two =input("What is the national ANIMAL of India? ")
    if que_two.lower()=="tiger":
        print("Correct!")
        score += 1
    else:
        print("Wrong")
        print("correct answer : Tiger")
# -------------------
    que_three =input("What is the national BIRD of India? ")
    if que_two.lower()=="peacock":
        print("Correct!")
        score += 1
    else:
        print("Wrong")
        print("correct answer : Peacock")
# -------------------
    que_four =input("What is the national GAME of India? ")
    if que_four.lower()=="hockey":
        print("Correct!")
        score += 1
    else:
        print("Wrong")
        print("correct answer : Hockey")
# -------------------
    que_five =input("What is the national TREE of India? ")
    if que_five.lower()=="fig":
        print("Correct!")
        score += 1
    else:
        print("Wrong")
        print("correct answer : Fig")
# -------------------
print("Your score is", score)