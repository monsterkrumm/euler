
# Project Euler
# Problem 003
# Marc Watkins
# 2016-06-12

solution = 3
number = 4498475987938465
i = 3
while i < number:
    if number % i == 0:
        solution = i
        number = number / i
    else:
        i += 2
print(max(solution,number))

