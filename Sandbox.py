"""Find the largest odd integer"""
iterations = 10
max = 0

while iterations > 0:
    userInput = int(input('Enter a whole number: '))
    if userInput % 2 != 0 and userInput > max:
        max = userInput
    iterations -= 1

print(max)