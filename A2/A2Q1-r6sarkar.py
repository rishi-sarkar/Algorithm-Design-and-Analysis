#!/usr/bin/env python3
"""
Assignment 2 Python file
Copy-and-paste your extended_euclid and modexp functions
from assignment 1
"""
import random
import math

################################################################################
# PROGRAMMING QUESTION SUBMISSION INSTRUCTIONS FOR A1Q5
#   1. Write your username and student number in the box below
#   2. Submit your code as A2Q1-<WatIAMusername>.py to the LEARN Dropbox
#      where <WatIAMusername> is replaced by your WatIAM username
#   3. Submit a screencap of the functions you implemented
#      and the comment box containing your username and student
#      number to Crowdmark.
################################################################################

################################################################################
# student info
#
# WatIAM username: r6sarkar
# Student number: 20894095
################################################################################


################################################################################
# helper functions (from A1)
################################################################################
#
def modexp(x, y, N):
    """
    This function compute x^y mod N
    Hint:  modulo in python is  the "%" operator.
    You can check that your code is correct by comparing to pow(x,y,N), which is python's implementation
    """
    if y == 0:
        return 1
    z = modexp(x, math.floor(y/2), N)
    if y % 2 == 0:
        return (z * z) % N
    else:
        return (x * z * z) % N
#
#


def extended_Euclid(a, b):
    """
    This function computes (x,y,d) where d = gcd(a,b) and x and y are integers such that ax + by = d
    """
    if b == 0:
        return 1, 0, a
    (x1, y1, d) = extended_Euclid(b, a % b)

    return y1, x1 - math.floor(a/b) * y1, d
#
################################################################################


def primality(N):
    """
    Test if a number N is prime using Fermat's little Theorem with
    ten random values of a.  If a^(N-1) mod N = 1 for all values,
    then return true.  Otherwise return false.
    Hint:  you can generate a random integer between a and b using
    random.randint(a,b).
    """
    tests = random.sample(range(2, N-1), 10)
    for a in tests:
        if modexp(a, N-1, N) != 1:
            return False
    return True


def prime_generator(N):
    """
    This function generates a prime number <= N
    """
    possible_primes = random.sample(
        range(N % 10, N-1), 100)  # low probability of error with 100 samples
    for prime in possible_primes:
        if primality(prime):
            return prime
    return 0


def main():
    """
    Generate RSA private/public key, then encode and decode a message.
    """
    # A2Q1:  generating primes and RSA
    ##################
    x = 2148321
    e = 5

    p = 0
    q = 0
    phi = 0
    d = 0
    N = 0
    relative_prime = False

    for _ in range(100):  # no infinite loop
        p = prime_generator(10000000)
        q = prime_generator(10000000)
        _, d, gcd = extended_Euclid((p-1)*(q-1), e)
        if (gcd == 1):
            relative_prime = True
            phi = (p-1)*(q-1)
            N = p * q
            break
    if not relative_prime:
        print("No useful primes found. Try Again")
        return 0

    while (d < 0 or d > phi-1):
        d += phi

    # encoding
    print()
    print("Message: ", x)
    print("Public Key: (N): {}, (e): {}".format(N, e))
    encoded = modexp(x, e, N)
    print("Encoded Message: ", encoded)
    print("Secret Key: ", d)
    decoded = modexp(encoded, d, N)
    print("Decoded Message: ", decoded)
    print("Encoder Working?: ", x == decoded)
    print("\n")

    print("part iii:")
    print("p: {}, q: {}".format(p, q))
    print("part iv:")
    print("d: ", d)
    print("part v:")
    print("Encoded message: ", encoded)
    print("part vi:")
    print("Decoded message: ", decoded)


if __name__ == '__main__':
    main()
