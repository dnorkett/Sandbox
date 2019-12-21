#Calculate the number of months needed to save for a down payment based on two raises a year
annual_salary = float(input('Enter your starting annual salary:'))
portion_saved = float(input('Enter the percent of your salary to save, as a decimal:'))
total_cost = float(input('Enter the cost of your future home:'))
semi_annual_raise = float(input('Enter the semi-annual raise, as a decimal:'))

def calc_downpayment_months(annual_salary, portion_saved, total_cost, semi_annual_raise):
    """
    :param annual_salary: annual salary amount
    :param portion_saved: percent of the annual salary that will be saved
    :param total_cost: cost of the home that will be purchased
    :param semi_annual_raise: percentage annual salary increased every 6 months, as a decimal
    :return: returns the number of months needed to save a down payment
    """
    portion_down_payment = .25 * total_cost
    r = .04
    current_savings = 0
    months = 0
    while (current_savings < portion_down_payment):
        current_savings = current_savings + (current_savings * r / 12) + (portion_saved*annual_salary / 12)
        months+=1
        if months%6 == 0:
            annual_salary = annual_salary + annual_salary*semi_annual_raise
    return months

print('Number of months:', calc_downpayment_months(annual_salary, portion_saved, total_cost, semi_annual_raise))