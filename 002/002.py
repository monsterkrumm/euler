
# Project Euler
# Problem 002
# Marc Watkins
# 2016-06-12

solution = 0
f = 2
f1 = 1
f2 = 1
ftmp = 0 # like to initialise

while f < 4000000:
    if f % 2 == 0:
        solution += f
    f = f + f2
    ftmp = f2
    f2 = f2 + f1
    f1 = ftmp

print(solution)
