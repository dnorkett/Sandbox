#Use bisection search to determine square root
def square_calculator(user_input):
    """
    accepts input from a user to determine the square root
    returns the square root of the user input
    """
    precision = .000000000001
    counter = 0
    low = 0
    high = user_input
    guess = (low + high) / 2.0

    while abs(guess**2 - user_input) >= precision:
        if guess**2 > user_input:
            high = guess
        if guess**2 < user_input:
            low = guess
        guess = (low + high) / 2.0
        counter+= 1

    return(guess, counter)


while True:
    user_input = int(input("Enter a number: "))
    answer, counter = square_calculator(user_input)

    print("The square root of", user_input, "is", round(answer,6))
    print("It took", counter, "guesses to figure it out.")