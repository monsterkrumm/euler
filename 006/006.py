# Project Euler
# Problem 006
# Marc Watkins
# 2016-06-13

sumOfSquares = 0
for x in range (1,101):
    sumOfSquares = sumOfSquares + x**2

squareOfSums = 5050**2

solution = squareOfSums - sumOfSquares

print(solution)
