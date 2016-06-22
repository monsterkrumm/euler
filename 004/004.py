# Project Euler
# Problem 004
# Marc Watkins
# 2016-06-13


def isPalindrome(number):
    strnumber = str(number)
    strlen  = len(strnumber)
    isPalindrome = True
    for i in range(strlen):
        if strnumber[i] != strnumber[strlen - 1 - i]: 
            isPalindrome = False
            break
    return isPalindrome

solution = 0
for i in range(100,1000):
    for j in range(i,1000):
        product = i * j
        if product > solution:
            if isPalindrome(product):
                solution = product
print(solution)


'''
EXAMPLES

example1 = 2332
example2 = 3456543
example3 = 3422342
example4 = 34567543

print(isPalindrome(example1))
print(isPalindrome(example2))
print(isPalindrome(example3))
print(isPalindrome(example4))

'''
