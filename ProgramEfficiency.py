#1. Measure with a timer
#2. Count the operations
#3. *PREFERRED* Abstract notion of order of growth (BIG O NOTATION)

#Option 1, timing a program / algorithm
#Varies between implementations, varies between computers. Not predictable based on small inputs
#Timing varies for different inputs, but cant really express relationship between time and inputs
import time
def c_to_f(c):
    return c*9/5 + 32

t0=time.clock()
c_to_f(100000)
t1=time.clock()

timeDiff=t1 - t0
print(timeDiff)


#Option 2, count the operations
#Assume that steps take constant time
#Mathmatical operations, comparisons, assignments, accessing objects in memory
#Then count the number of operations executed as funtion of size of input
#Depends on algorithm (good) and not on computers (good)
#Depends on implementation (bad) and no clear definition of which operations to count
def c_to_f(c):
    return c*9/5 + 32       #3 ops

def mysum(x):
    total=0                 #1 ops
    for i in range(x+1):    #1 ops
        total += i          #2 ops
    return total            #times number of loops, +1 operation for return


