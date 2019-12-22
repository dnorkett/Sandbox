# # """Find the largest odd integer"""
# # iterations = 10
# # max = 0
# #
# # while iterations > 0:
# #     userInput = int(input('Enter a whole number: '))
# #     if userInput % 2 != 0 and userInput > max:
# #         max = userInput
# #     iterations -= 1
# #
# # print(max)
# #
# # x = 25
# # epsilon = .00001
# # step = epsilon**2
# # numGuesses = 0
# # ans = 0.0
# #
# # while abs(ans**2 - x) >= epsilon and ans*ans <= x:
# #     ans += step
# #     numGuesses += 1
# #
# # print("numGuesses:", numGuesses)
# #
# # if abs(ans**2 - x) >= epsilon:
# #     print("Failed on square root of ", x)
# # else:
# #     print(ans, "is close to square root of", x)
# #
# # x = 25
# # epsilon = .01
# # numGuesses = 0
# # low = 0.0
# # high = max(1.0,x)
# # ans = (low + high)/2.0
# #
# # while abs(ans**3 - x) >= epsilon:
# #     print("low=",low,"high=",high,"ans=",ans)
# #     numGuesses+=1
# #     if ans**3 < x:
# #         low=ans
# #     else:
# #         high = ans
# #     ans = (low + high)/2.0
# #
# # print("numGuesses = ",numGuesses)
# # print(ans, "is the cube root of",x)
# #
# # x = 0.0
# # for i in range(10):
# #     print(x)
# #     x = x + 0.1
# # if x == 1.0:
# #     print(x,"= 1.0")
# # else:
# #     print(x,"is not 1.0")
# #
# # def disemvowel(string):
# #     vowels = ('a', 'e','i','o','u')
# #     new_str = ''
# #     for i in string:
# #         if i.lower() not in vowels:
# #             new_str += i
# #     return new_str
# #
# # print(disemvowel("This website is for losers LOL!"))
#
# #
# # import string
# # def toJadenCase(userinput):
# #     return string.capwords(userinput)
# #
# # print(toJadenCase('q w e r'))
# #
# # def digital_root(n):
# #     running_sum=0
# #     for i in str(n):
# #         running_sum+= int(i)
# #     if len(str(running_sum)) > 1:
# #         return digital_root(running_sum)
# #     else:
# #         return running_sum
# #
# # print(digital_root(444))
#
# #
# # def add_binary(a,b):
# #     return format(a+b, "b")
# #
# # print(add_binary(1,1))
#
#
# #
# # def persistence(n, counter=0):
# #     if len(str(n)) == 1:
# #         return counter
# #     product = 1
# #     counter+=1
# #     for i in str(n):
# #         product *= int(i)
# #     return persistence(product, counter)
# #
# #
# #
# # print(persistence(39))
#
# # def isPalindrome(input):
# #     input = input.replace(" ", "")
# #     input = input.lower()
# #     if len(input) <= 1:
# #         return True
# #     elif input[0] == input[-1]:
# #         return isPalindrome(input[1:-1])
# #     else:
# #         return False
# #
# # print(isPalindrome('soaoos'))
# #
#
# def get_permutations(sequence):
#     '''
#     Enumerate all permutations of a given string
#     sequence (string): an arbitrary string to permute. Assume that it is a
#     non-empty string.
#     You MUST use recursion for this part. Non-recursive solutions will not be
#     accepted.
#     Returns: a list of all permutations of sequence
#     Example:
#     >>> get_permutations('abc')
#     ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
#     Note: depending on your implementation, you may return the permutations in
#     a different order than what is listed here.
#     '''
#
#     if len(sequence) <= 1:
#         return [sequence]
#     else:
#         permutations = []
#         first_char = sequence[0]
#         next_chars = sequence[1:]
#         permutations_of_subsequence = get_permutations(next_chars)
#         for seq in permutations_of_subsequence:
#             for index in range(len(seq) + 1):
#                 new_seq = seq[0:index] + first_char + seq[index:len(seq) + 1]
#                 permutations.append(new_seq)
#
#         # print(permutations)
#         return permutations
#
#
# print(get_permutations('abc'))
#

def build_shift_dict(shift):
    '''
    Creates a dictionary that can be used to apply a cipher to a letter.
    The dictionary maps every uppercase and lowercase letter to a
    character shifted down the alphabet by the input shift. The dictionary
    should have 52 keys of all the uppercase letters and all the lowercase
    letters only.

    shift (integer): the amount by which to shift every letter of the
    alphabet. 0 <= shift < 26

    Returns: a dictionary mapping a letter (string) to
             another letter (string).
    '''
    lower_letters = 'abcdefghijklmnopqrstuvwxyz'
    upper_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    shifted_lower = lower_letters[shift:] + lower_letters[:shift]
    shifted_upper = upper_letters[shift:] + upper_letters[:shift]
    shift_dict={}
    for i in range(26):
        lower_char = lower_letters[i]
        upper_char = upper_letters[i]
        shift_dict[lower_char] = shifted_lower[i]
        shift_dict[upper_char] = shifted_upper[i]
    return shift_dict



def apply_shift(message_text, shift):
    shift_dict = build_shift_dict(shift)
    shifted_message_text = ''
    for char in message_text:
        shifted_message_text += shift_dict[char]

    return shifted_message_text

print(apply_shift('bob', 1))