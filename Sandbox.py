# """Find the largest odd integer"""
# iterations = 10
# max = 0
#
# while iterations > 0:
#     userInput = int(input('Enter a whole number: '))
#     if userInput % 2 != 0 and userInput > max:
#         max = userInput
#     iterations -= 1
#
# print(max)
#
# x = 25
# epsilon = .00001
# step = epsilon**2
# numGuesses = 0
# ans = 0.0
#
# while abs(ans**2 - x) >= epsilon and ans*ans <= x:
#     ans += step
#     numGuesses += 1
#
# print("numGuesses:", numGuesses)
#
# if abs(ans**2 - x) >= epsilon:
#     print("Failed on square root of ", x)
# else:
#     print(ans, "is close to square root of", x)
#
# x = 25
# epsilon = .01
# numGuesses = 0
# low = 0.0
# high = max(1.0,x)
# ans = (low + high)/2.0
#
# while abs(ans**3 - x) >= epsilon:
#     print("low=",low,"high=",high,"ans=",ans)
#     numGuesses+=1
#     if ans**3 < x:
#         low=ans
#     else:
#         high = ans
#     ans = (low + high)/2.0
#
# print("numGuesses = ",numGuesses)
# print(ans, "is the cube root of",x)
#
# x = 0.0
# for i in range(10):
#     print(x)
#     x = x + 0.1
# if x == 1.0:
#     print(x,"= 1.0")
# else:
#     print(x,"is not 1.0")
#
# def disemvowel(string):
#     vowels = ('a', 'e','i','o','u')
#     new_str = ''
#     for i in string:
#         if i.lower() not in vowels:
#             new_str += i
#     return new_str
#
# print(disemvowel("This website is for losers LOL!"))

#
# import string
# def toJadenCase(userinput):
#     return string.capwords(userinput)
#
# print(toJadenCase('q w e r'))

def digital_root(n):
    running_sum=0
    for i in str(n):
        running_sum+= int(i)
    if len(str(running_sum)) > 1:
        return digital_root(running_sum)
    else:
        return running_sum


print(digital_root(444))
