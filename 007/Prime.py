# Primem Class File
# Marc Watkins
# 2016-06-14


class Primelist:

    import math

    def __init__(self, upto=0):
        self.primelist = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47] 
        while upto > self.primelist[-1]:
            self.nextNewPrime()

    def __len__(self):
        return len(primelist)







#HELPERS
    def nextNewPrime(self):
        newNum = self.primelist[-1]+2
        while True:
            for factor in self.primelist:
                if factor**2 > newNum:
                    self.primelist.append(newNum)
                    return newNum
                if newNum % factor == 0:
                    newNum += 2
                    break
