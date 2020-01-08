def digital_root(n):
    """Given n, take the sum of the digits of n.
    If that value has more than one digit, continue reducing in this way
    until a single-digit number is produced. """
    running_sum=0
    for i in str(n):
        running_sum+= int(i)
    if len(str(running_sum)) > 1:
        return digital_root(running_sum)
    else:
        return running_sum