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

#Combine complexity classes
    #analyze statements inside functions
#Law of Multiplication for O():
    #Used with nested statements/loops

#Is O(n) * O(n) = O(n^2) because outer loop goes n times and inner loop goes n times for every outer loop tier
#Nested loops typically have O(n^2)
for i in range(n):
    for j in range(n):
        print('a')

#Complexity cases
#O(1) = constant, very rare
#O(log n) = logarithmic running time
#O(n) = linear running time
#O(n log n) log-linear running time
#O(n^c) polynomial running time (c is constant)
#O(c^n) exponential running time (c is a constant being raised to a power based on the size of the input)

#Linear search on unsorted list
#Must look through all elementa to decide it's not there
def linear_search(L,e):
    found=false
    for i in range(len(L)):     #Not using while=false reduces avg runtime (order of complexity), but does NOT change order of growth
        if e==L[i]:
            found = True
    return found

#Quadratic growth
#Outer loop executed len(L1) times, inner loop executed len(L2) times.
#n*n = n^2
def isSubset(L1, L2):
    for e1 in L1:
        matched=False
        for e2 in L2:
            if e1 == e2:
                matched=True
                break
            if not matched:
                return False
    return True

#Still quadratic growth. N^2 + N, look at highest O
def intersect(L1,L2):
    tmp = []
    for e1 in L1:
        for e2 in L2:
            if e1 == e2:
                tmp.append(e1)
    res = []
    for e in tmp:
        if not(e in res):
            res.append(e)
    return res


#How does a choice in design affect efficiency of algorithm
#Recognize standard patterns in algorithm design

#Bisection search - RECAP
#Pick an index, divide list in half. Ask if L[i] == e, if not ask smaller or larger
#Depending on results, search left or right half of L for e
#Break into smaller version of problem (smaller list) plus some simple operations
#Answer to smaller version is answer to original problem
# (n)/(2^i). Complexity is O(log n)


#implementation 1
#O(log n) bisection search calls
    #on each recursive call, size of range to be searched cut in half
    #if original size n, worst cast down to size 1 when n/(2^k) = k; or k = log n
#O(n) for each bisection search call to copy list
    #This is the cost to set up each call, so do this for each level of recursion
#O(log n) * O(n) -> O(n log n)
    #if we are careful, note that length of list to be copies is also halved
    #turns out total cost to copy is O(n) and this dominates the log n cost due to recursive calls


def bisect_search1(L,e):
    if L== []:
        return False
    elif len(L) == 1:
        return L[0] == e
    else:
        half = len(L)//2
        if L[half] > e:
            return bisect_search1(L[:half], e)
        else:
            return bisect_search1(L[half:], e)


