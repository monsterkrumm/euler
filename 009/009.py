# Project Euler
# Problem 009 # Marc Watkins # 2016-06-18 
# We use the fact that Pythagorean triples are given by
# a = k(m^2-n^2), b = k2mn, c = k(m^2+n^2) for any coprime m and n

from fractions import gcd

#initialising
k,m,n = 1,1,1

#We use a function so to easier return result tuple
def finder(target):
    #looping through n, sort of makes sense to cap but
    #does not really matter since function returns once value is found
    for n in range(1,target // 2):
        for m in range(n,target //2):
            if gcd(m,n) != 1:     # use only coprime m and n
                continue
            #iterate through mulitples (limit for k is a guess)
            for k in range(1,121):
                a = k * (m * m - n * n)
                b = k * 2 * m * n
                c = k * (m * m + n * n)
                if a + b + c == target:
                    return a,b,c

result = finder(1000)
print(result)
print(result[0] * result[1] * result[2])



