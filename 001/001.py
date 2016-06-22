
# Project Euler
# Problem 001
# Marc Watkins
# 2016-06-12

# I realise this is probably no the most
# elegant solution, but here goes

solution = 0
i = 1
while i < 1000:
    if i%3 == 0:
        solution += i
    elif i%5 == 0:
        solution += i
    i += 1

print(solution)
    
