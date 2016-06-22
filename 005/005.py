# Project Euler
# Problem 005
# Marc Watkins
# 2016-06-13

# Note, this problem is not easier to solve by programming
# but will solve by programming anyway, for the fun

# Too tedious to sieve for primes up to 20, so just posit them:
primes = [2,3,5,7,11,13,17,19]
solution = 1
target = 20

for p in primes:
    factor = p
    while factor <= target:
        if factor * p < target:
            factor = factor * p
        else:
            break
    solution = solution * factor

print(solution)
