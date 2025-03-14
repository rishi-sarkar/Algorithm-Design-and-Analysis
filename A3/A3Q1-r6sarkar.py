#!/usr/bin/env python3
"""
ECE 406:  File for Exercise 1 of Assignment #3
"""
import numpy as np
from numpy.fft import fft, ifft

################################################################################
# PROGRAMMING QUESTION SUBMISSION INSTRUCTIONS FOR A3Q1
#   1. Write your username and student number in the box below
#   2. Submit your code as A3Q1-<WatIAMusername>.py to the LEARN Dropbox
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
def get_bitstring(x_int, n):
    """Format a non-negative integer x as a length-n string.
    Each character in the bit-string output represents a bit from x."""
    x_bitstring = format(x_int, f'0{n}b')
    return x_bitstring
#


def get_coeffs(x_int, n):
    """Get coeffs c_0, c_1, ..., c_{n-1} for polynomial representation of x"""
    # NOTE: these coeffs are formatted as a list, where the smallest-power component goes first
    x_bitstring = get_bitstring(x_int, n)
    x_coeff = [int(x_) for x_ in reversed(x_bitstring)]
    return x_coeff
#


def cleanup_coeffs(Qcoeff):
    """Convert coeffs of degree-n polynomial Q(x) to coefficients of a new polynomial Q'(x).

    Coefficients of Q'(x) are all binary, and are chosen so Q'(x=2) = Q(x=2).
    """
    Q = list(Qcoeff.real)
    for i in range(len(Q)-1):
        (q, r) = divmod(Q[i], 2)
        Q[i+1] += q
        Q[i] = r
    return Q
################################################################################


def multiply_by_fft(Xcoeff, Ycoeff, n):
    """Given coefficient representation of two polynomials, compute the coefficient representation of their product using FFT.

    n is the number of values chosen when computing the value representation for the input polynomials

    You just need to fill in parts (ii), (iii) and (iv)
    """

    ################################################################################
    # part (ii) - get value representation for A(x) and B(x) using np.fft.fft
    # TODO: implement
    # HINT: use np.fft.fft as a helper function
    #       (do not implement the recursive FFT psuedocode we discussed in class)
    # NOTE: the second argument to np.fft.fft represents the number of values chosen to compute the value representation
    #       i.e. the n in {omega^0, omega^1, ..., omega^{n-1}}
    Xval = np.fft.fft(Xcoeff, n)
    Yval = np.fft.fft(Ycoeff, n)
    ################################################################################

    ################################################################################
    # part (iii) - get value representation of C(x), where C(x) = A(x) * B(x)
    # TODO: implement
    Cval = Xval * Yval
    ################################################################################

    ################################################################################
    # part (iv) - get the coefficients of the polynomial C(x)
    # HINT: use np.fft.ifft as a helper function, where ifft is the "inverse" FFT.
    #       In class we discussed how interpolation is done by computing the FFT
    #       algorithm with M^{-1}(omega), which is the same as M(omega^{-1}).
    #       In signal processing this is simply called computing the inverse FFT.
    # TODO: implement
    Ccoeff = np.fft.ifft(Cval).real.round().astype(int)
    ################################################################################

    ################################################################################
    # part (v) -  "clean up" the coefficients of C(x): if any coeffs are not in {0, 1},
    #      produce a new polynomial C'(x) such that all coeffs of C'(x) are binary,
    #      and C'(x=2) = C(x=2)
    #      (already implemented for you)
    Ccoeff = cleanup_coeffs(Ccoeff)  # leave this line unchanged
    ################################################################################

    return(Ccoeff)


def main():
    """
    Exercise 1:  Using the FFT to multiply two binary numbers.
    You just need to fill in parts (ii), (iii) and (iv) within multiply_by_fft
    """
    # The binary numbers and their product
    RANDOM_CHOICE = False  # set this as True to play around with different inputs
    if RANDOM_CHOICE:
        a = np.random.randint(0, 7)
        b = np.random.randint(0, 7)
    else:
        a = 0b1101  # A(x) = x^3 + x^2 + x
        b = 0b1011  # B(x) = x^3 + x + 1
    n = 8  # choose n >= 2d + 1, and a power of 2
    print(f'    a = {int(a)} (decimal)')
    print(f'    b = {int(b)} (decimal)')
    print(f'a * b = {int(a * b)} (decimal)')
    print()
    print(f'    a = {get_bitstring(int(a), n)} (binary)')
    print(f'    b = {get_bitstring(int(b), n)} (binary)')
    print(f'a * b = {get_bitstring(int(a * b), n)} (binary)')
    print('       ', '^' * n, '(the answer we want to get via fft)')

    ################################################################################
    # part (i) - express a and b in terms of their polynomial coefficients
    #            (already implemented for you)
    Acoeff = np.array(get_coeffs(a, n))
    Bcoeff = np.array(get_coeffs(b, n))
    assert np.polyval(list(reversed(Acoeff)),
                      2) == a, 'A(x=2) = a should hold!'
    assert np.polyval(list(reversed(Bcoeff)),
                      2) == b, 'B(x=2) = b should hold!'
    ################################################################################

    # multiply polynomials via FFT
    Ccoeff = multiply_by_fft(Acoeff, Bcoeff, n)
    print()
    print(
        f"a * b = {''.join(str(C) for C in list(reversed(Ccoeff)))} (binary)")
    # NOTE: to get binary number we scan over coefficients of C(x) in reverse order,
    #       i.e. c_{n-1}, c_{n-2}, ..., c_1, c_0
    print('       ', '^' * n, '(the answer we currently get using multiply_fft)')
    print()

    # testing modular exponentiation
    if np.linalg.norm(np.array(get_coeffs(a * b, n)) - Ccoeff) == 0.0:
        print("multiply_fft passed test")
    else:
        print(
            f"multiply_fft failed test: expected {np.array(get_coeffs(a * b, n))}, got {[int(C) for C in Ccoeff]}")


if __name__ == '__main__':
    main()
