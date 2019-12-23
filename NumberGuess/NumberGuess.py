#Use bisection search to determine a users guessed number
answer = int(input("Enter a number to guess from 1 to 100: "))
low = 1
high = 100
counter = 0
guess = 0

while guess != answer:
    guess = int((low + high) / 2)
    print("Guess #", counter+1, ": ", guess)
    higherOrLower = input("Is your number higher (h), lower (l), or correct(c)?")
    if higherOrLower == 'h':
        low = guess
    if higherOrLower == 'l':
        high = guess
    if higherOrLower == 'c':
        print("Woohoo! Got it!")
    counter += 1

print("It took ", counter, " guesses to find your number!")
