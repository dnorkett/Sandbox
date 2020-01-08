def calcSimpleInterest(rate,days, principle):
    """
    calculates simple interest based on a yearly rate, the principal amount, and the number of days

    rate - the yearly rate, specified as a decimal
    days - the number of days to calculate interest
    principle - the principle amount used to calculate interest

    returns interest amount
    """
    interest = principle * rate * days / 365

    return interest