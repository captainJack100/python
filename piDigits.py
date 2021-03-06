import math
import time

class piDigits(object):
    """ piDigits: calculates the digits of pi
    using integers.
    """
    denom = 0 
    precision = 0
    slop = 4

    def __init__(self):
        self.num = 0

    @classmethod
    def scaledNumerator(cls, numerator, denominator):
        tmp = cls()
        tmp.num = (cls.denom * numerator) / denominator
        return tmp
    
    @classmethod
    def noScaleNumerator(cls, numerator):
        tmp = cls()
        tmp.num = numerator
        return tmp
    
    @staticmethod
    def setPrecision(prec):
        piDigits.precision = prec
        
        #tmp = 10
        #for x in xrange(piDigits.precision + piDigits.slop):
        #    tmp *= 10
        #piDigits.denom = tmp

        lst = [0 for x in xrange(piDigits.precision + piDigits.slop)]
        lst.insert(0,1)
        piDigits.denom = int("".join(map(str, lst)))

    @staticmethod
    def Atan(denominator):
        result = piDigits.scaledNumerator(1, denominator)
        squared = denominator*denominator
        
        divisor = 1
        term = result
       
        while(not term.IsZero()):
            divisor += 2
            term /= squared
            result -= term / divisor

            divisor += 2
            term /= squared
            result += term / divisor

        return result

    @staticmethod
    def getPi(digits):
        piDigits.setPrecision(digits)
        first = piDigits.Atan(5)*4
        second = piDigits.Atan(239)
        return (first - second)*4

    def IsZero(self):
        return self.num == 0

    def __mul__(left, right):
        if isinstance(right, int):
            return piDigits.noScaleNumerator(left.num * right)
        else:
            return piDigits.noScaleNumerator((left.num * right.num) / piDigits.denom)
    
    def __div__(left, right):
        return piDigits.noScaleNumerator(left.num/right)

    def __add__(left, right):
        return piDigits.noScaleNumerator(left.num + right.num)

    def __sub__(left, right):
        return piDigits.noScaleNumerator(left.num - right.num)

    def __str__(self):
        remain = 0
        quotient = 0
        quotient, remain = map(int, divmod(self.num, piDigits.denom))
        strg = str(quotient) + '.' + str(remain)[:piDigits.precision]
        return strg 

def unit_test():
    start, end = (0,0)
    
    start = time.time()
    print piDigits.getPi(1000)
    end = time.time()

    print "time: ", end - start

if __name__ == "__main__":
    unit_test()
