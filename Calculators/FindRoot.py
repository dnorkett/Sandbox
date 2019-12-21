def findRoot(x, power, epsilon):
    #Negative numbers do not have even roots
    if x < 0 and power%2 == 0:
        return None
    low = min(-1.0, x)
    high = max(1.0, x)
    ans = (low + high) / 2.0

    while (abs(ans**power - x) >= epsilon ):
        if ans**power > x:
            high = ans
        else:
            low = ans
        ans = (low + high) / 2.0

    return ans

def testFindRoot():
    epsilon = 0.00001
    for x in [-0.25, .25, -2, 2, -8, 8, -27, 27]:
        for power in range(1,4):
            print("Testing x=", x, "power=", power, "epsilon=", epsilon)
            print(findRoot(x, power, epsilon))

testFindRoot()