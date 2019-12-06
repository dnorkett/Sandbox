#MIT Problem Set 1, Problem 1
annual_salary = float(input('Enter your starting annual salary:'))
portion_saved = float(input('Enter the percent of your salary to save, as a decimal:'))
total_cost = float(input('Enter the cost of your future home:'))
semi_annual_raise = float(input('Enter the semi-annual raise, as a decimal:'))

portion_down_payment = .25 * total_cost
current_savings = 0
r = .04
months = 0

while (current_savings < portion_down_payment):
    current_savings = current_savings + (current_savings * r / 12) + (portion_saved*annual_salary / 12)
    months+=1
    if months%6 == 0:
        annual_salary = annual_salary + annual_salary*semi_annual_raise

print('Number of months:',months)
print(int(months/12), ' years and', months%12, 'months')

