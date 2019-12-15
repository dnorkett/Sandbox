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


#Option 3, ORDERS OF GROWTH
#Best, Average, Worst Cases
#Suppose you are given a list L of some length len(L)
#Best case, minimum running time over all possible inputs
    #constant for search_for_element
    #first element in any list
#Average case
    #average running time, practical measure
    # linear in length of list for search_for_elmt
#Worst cast, maximum running time over all possible inputs
    #linear in length of list for search_for_elmt
    #must search entire list and not find it

def search_for_element(L,e):
    for i in L:
        if i == e:
            return True
    return False

#Focused on orders of growth. IE if I double the amount of data, what effect does this have
#Linear - 2x data 2x time, Quadratic - 2x data 4x time etc.
#Look at largest factors in runtime
#Upper bound on growth as a function of the size of the input in the worst case
#BIG O NOTATION!!!!!!

def fact_iter(n):
    """assumes n an int >= 0"""
    answer=1                #1 op
    while n>1:              #1 op
        answer *= n         #2 ops
        n-=1                #2 ops
    return answer

#Count steps - (1+5n+1)
#In this case, grows linearly. 2x data = 2x time.  O(n)
#Ignore additive and multiplicative constants, only focus on growth for large numbers

#n² + 2n + 2 = O(n²). n² dominant term over large numbers
#n² + 100000n + 3000000 = O(n²). n² still the dominant term over large numbers
#log(n) + n + 4 = O(n). n grows faster than log(n)
#0.0001*n*log(n) + 300n = O(n log n)
#2n^30 + 3^n = O(3^n). 3^n dominant over large numbers

