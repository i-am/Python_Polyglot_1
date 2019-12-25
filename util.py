def digits(n):
    if (n==0):
        return 1
    
    count = 0
    while(n != 0):
        count = count + 1
        n = n//10
    return count

def removeLeftDigit(n):
    order = 10**(digits(n)-1)
    multiple = n // order
    return n - order*multiple

def isPrime(n):
    if(n < 2):
        return False
    if(n < 4):
        return True
    
    if(n%2 == 0 or n%3 == 0):
        return False
    
    i=5
    while(i*i < n):
        if(n%i == 0 or n%(i+2) == 0):
            return False
        i=i+6
    return True

def isRightPrime(n):
    if(digits(n) == 1):
        return isPrime(n)
    return isPrime(n) and isRightPrime(n//10)

def isLeftPrime(n):
    if(digits(n) == 1):
        return isPrime(n)
    return isPrime(n) and isLeftPrime(removeLeftDigit(n))

def isTwoSidedPrime(n):
    if(digits(n) == 1):
        return isPrime(n)
    else:
        return isRightPrime(n) and isLeftPrime(n)   