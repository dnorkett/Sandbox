answer = int(input("Enter a number: "))

precision = .000000000001
counter = 0
low = 0
high = answer
guess = (low + high) / 2.0

while abs(guess**2 - answer) >= precision:
    if guess**2 > answer:
        high = guess
    if guess**2 < answer:
        low = guess
    guess = (low + high) / 2.0
    counter+= 1

print("The square root of", answer, "is", round(guess,6))
print("It took", counter, "guesses to figure it out.")
