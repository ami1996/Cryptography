from random import randrange, getrandbits
from math import sqrt

def is_prime(n, k=128):
    """ Test if a number is prime
        Args:
            n -- int -- the number to test
            k -- int -- the number of tests to do
        return True if n is prime
    """
    # Test if n is not even.
    # But care, 2 is prime !
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False
    # find r and s
    s = 0
    r = n - 1
    while r & 1 == 0:
        s += 1
        r //= 2
    # do k tests
    for _ in range(k):
        a = randrange(2, n - 1)
        x = pow(a, r, n)
        if x != 1 and x != n - 1:
            j = 1
            while j < s and x != n - 1:
                x = pow(x, 2, n)
                if x == 1:
                    return False
                j += 1
            if x != n - 1:
                return False
    return True

"""
# Returns True if n is prime
def is_prime( n):

    # Corner cases
    if (n <= 1):
        return False
    if (n <= 3):
        return True

    # This is checked so that we can skip
    # middle five numbers in below loop
    if (n % 2 == 0 or n % 3 == 0):
        return False
    i = 5
    while(i * i <= n):
        if (n % i == 0 or n % (i + 2) == 0) :
            return False
        i = i + 6

    return True
"""

""" Iterative Function to calculate (x^n)%p
    in O(logy) */"""

def power( x, y, p):
    res = 1 # Initialize result
    x = x % p # Update x if it is more
              # than or equal to p
    while (y > 0):

        # If y is odd, multiply x with result
        if (y & 1):
            res = (res * x) % p

        # y must be even now
        y = y >> 1 # y = y/2
        x = (x * x) % p

    return res

# Utility function to store prime
# factors of a number
def findPrimefactors(s, n) :

    # Print the number of 2s that divide n
    while (n % 2 == 0) :
        s.add(2)
        n = n // 2

    # n must be odd at this po. So we can
    # skip one element (Note i = i +2)
    for i in range(3, int(sqrt(n)), 2):

        # While i divides n, print i and divide n
        while (n % i == 0) :

            s.add(i)
            n = n // i

    # This condition is to handle the case
    # when n is a prime number greater than 2
    if (n > 2) :
        s.add(n)

# Function to find smallest primitive
# root of n
def findPrimitive( n) :
    s = set()

    # Check if n is prime or not
    if (is_prime(n) == False):
        return -1

    # Find value of Euler Totient function
    # of n. Since n is a prime number, the
    # value of Euler Totient function is n-1
    # as there are n-1 relatively prime numbers.
    phi = n - 1

    # Find prime factors of phi and store in a set
    findPrimefactors(s, phi)

    # Check for every number from 2 to phi
    for r in range(2, phi + 1):

        # Iterate through all prime factors of phi.
        # and check if we found a power with value 1
        flag = False
        for it in s:

            # Check if r^((phi)/primefactors)
            # mod n is 1 or not
            if (power(r, phi // it, n) == 1):

                flag = True
                break

        # If there was no power with value 1.
        if (flag == False):
            return r

    # If no primitive root found
    return -1

def extended(r1,r2):
    if r1 == 0:
        return (r2, 0, 1)
    else:
        gcd, x, y = extended(r2 % r1, r1)
        return (gcd, y - (r2//r1) * x, x)


def generate_prime_candidate(length):
    # generate random bits
    p = getrandbits(length)
    # apply a mask to set MSB and LSB to 1
    p |= (1 << length - 1) | 1
    return p

def generate_prime_number(length=128):
    # keep generating while the primality test fail
    p = 4
    while not is_prime(p, 128):
        p = generate_prime_candidate(length)
    return p
