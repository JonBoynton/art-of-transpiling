#
# Numbers to Words:
# Provides a code example that will convert a long string of numbers into text. 
#
# https:#en.wikipedia.org/wiki/Names_of_large_numbers - Standard dictionary 
# to:vigintillion 
#
# Note: This is sample source code. It does work but is not optimized or
#       otherwise intended for use in production.
#
# @author: Jon L. Boynton
#
from math import ceil, floor
SMALL_NUMBERS = [
    "",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
    "ten",
    "eleven",
    "twelve",
    "thirteen",
    "fourteen",
    "fifteen",
    "sixteen",
    "seventeen",
    "eighteen",
    "nineteen",
    "twenty",
    "thirty",
    "forty",
    "fifty",
    "sixty",
    "seventy",
    "eighty",
    "ninety"]
    
LARGE_NUMBERS = [
    "",
    "hundred",
    "thousand",
    "million",
    "billion",
    "trillion",
    "quadrillion",
    "quintillion",
    "sextillion",
    "septillion",
    "octillion",
    "nonillion",
    "decillion",
    "undecillion",
    "duodecillion",
    "tredecillion",
    "quattuordecillion",
    "quindecillion",
    "sexdecillion",
    "septendecillion",
    "octodecillion",
    "novemdecillion",
    "vigintillion"]
    
ZERO = "zero"
    
        
def isDecimal(charCode):
    return charCode > 47 and charCode < 58 # between 0 - 9    


  
class NumberString():
    
    def __init__(self, spec, offset=0):
        self.spec = spec
        self.offset = offset
        
        while offset < len(spec) and not isDecimal(ord(spec[offset])):
            offset += 1
        
        end = offset
        
        while end < len(spec):
            c = ord(spec[end])
    
            # check for  0-9 and ","    
            if not isDecimal(c) and c != 44:
                break
            
            end += 1        
        
        
        self.rawLength = end - offset
        self.isNegative = bool(self.rawLength and ord(spec[offset-1]) == 45)
        
        s = spec[offset: end]
        self.value = s.replace(",", "")
        
        if len(self.value) > 66:
            raise TypeError("number >= '1000 vigintillion'")
            
    
    
    
    def getTokens(self):
        ta = []
        
        if not self.value:
            return ta
        
        pos = 0
        Len = ceil(len(self.value)/3)
        rem = len(self.value) % 3 or 3
        
        while True:
            ta.append(int(self.value[pos: pos + rem]))
            pos += rem
            rem = 3
            Len -= 1
            if not Len > 0:
                break
        
        return ta        
    
    
    def formatSmallNumber(self, numbr):
        n = ""
        numbr %= 1000
        
        if numbr > 99:
            n = SMALL_NUMBERS[floor(numbr/100)] + " " + LARGE_NUMBERS[1]
            numbr %= 100
            
            if numbr:
                n += " and "
            
                
        
        if numbr > 20:
            n += SMALL_NUMBERS[18 + floor(numbr/10)]
            numbr %= 10
            
            if numbr:
                n += "-"+SMALL_NUMBERS[numbr]
            
                            
        elif numbr:
            n += SMALL_NUMBERS[numbr]            
                    
        return n        
    
    
    def toString(self):
        ta = self.getTokens()
        
        if len(ta) == 1 and not ta[0]:
            return ZERO
        
        
        buf = ""
        
        for i in range(0, len(ta)):
            n = self.formatSmallNumber(ta[i])
            
            if n:
                if buf:
                    buf += ", "
                elif self.isNegative:
                    buf = "minus "
                
                if i < len(ta) - 1:
                    n += " " + LARGE_NUMBERS[len(ta) - i]
                                    
                buf += n
                        
        
        return buf        
        


n = NumberString("my big number is 431,541,056,545,003,000,102")

print(n.toString())
