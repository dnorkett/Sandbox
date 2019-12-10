while True:
    try:
        a = int(input("Enter a number: "))
        b = int(input("Enter another number: "))
        print("a/b = ", a/b)
        print("a+b = ", a+b)
    except ValueError:
        raise ValueError('Could not convert to a number')
    except ZeroDivisionError:
        print("Can't divide by zero")
    except:
        print("Something went very wrong")
    else:
        print("Completed with no exceptions")
    finally:
        print("Ended")

def avg(grades):
    assert not len(grades) == 0, 'no grades data'
    return sum(grades / len(grades))
