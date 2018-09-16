import random
def guess():
    counter = 0
    print("I am thinking of a number between 1 and 20.")
    num = random.randint(1, 20)
    while True:
        n = int(input("Take a guess "))
        if n < num:
            print("Your guess to low")
            counter += 1
        elif n > num:
            print("Your guess to high")
            counter += 1
        else:
            print("Good job. You guessed my number in", counter, "guesses")
            return
guess()
