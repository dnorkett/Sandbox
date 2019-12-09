#Calculate what percentage of income to save to afford a home down payment in 3 years
annual_salary = float(input('Enter your starting annual salary:'))
total_cost = 1000000
portion_down_payment = .25 * total_cost

low_guess = 1
high_guess = 10000
portion_saved_guess = ((low_guess + high_guess) / 2)
counter = 0


def calculateTotal(salary_savings_rate, annual_salary):
    salary_savings_rate = salary_savings_rate / 10000
    annual_salary = annual_salary
    semi_annual_raise = .07
    current_savings = 0
    investment_rate = .04
    for i in range(1,37):
        current_savings = current_savings + (current_savings * investment_rate / 12) + (salary_savings_rate*annual_salary / 12)
        if i % 6 == 0:
            annual_salary += annual_salary*semi_annual_raise
    return current_savings


if calculateTotal(10000,annual_salary) >= portion_down_payment:
    total_saved = calculateTotal(portion_saved_guess, annual_salary)
    while abs(total_saved - portion_down_payment) > 100:
        counter += 1
        if total_saved < portion_down_payment:
            low_guess = portion_saved_guess
        else:
            high_guess = portion_saved_guess
        portion_saved_guess = ((low_guess + high_guess) / 2)
        total_saved = calculateTotal(portion_saved_guess, annual_salary)
    print(round(portion_saved_guess/10000,4))
    print(counter)
else:
    print("It is not possible to pay the down payment in three years.")

