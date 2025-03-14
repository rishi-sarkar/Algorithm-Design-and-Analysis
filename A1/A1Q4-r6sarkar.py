import time
import datetime

################################################################################
# PROGRAMMING QUESTION SUBMISSION INSTRUCTIONS FOR A1Q4
#   1. Write your username and student number in the box below
#   2. Submit your code as A1Q4-<WatIAMusername>.py to the LEARN Dropbox
#      where <WatIAMusername> is replaced by your WatIAM username
#   3. Submit the signed Academic Integrity form to the LEARN Dropbox
#      (You only need to do this once, typically with the first assignment)
#   4. Submit a screencap of the functions you implemented 
#      and the comment box containing your username and student
#      number to Crowdmark.
################################################################################

################################################################################
# student info
#
# WatIAM username: r6sarkar
# Student number: 20894095
################################################################################


def fib1(n):
    """An inefficient implementation of computing the n-th Fibonacci number"""
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib1(n-2) + fib1(n-1)

def fib2(n):
    """An efficient implementation of computing the n-th Fibonacci number"""
    if n == 0:
        return 0
    fib = [0] * (n+1)
    fib[0] = 0
    fib[1] = 1
    for i in range(2,n+1):
        fib[i] = fib[i-2] + fib[i-1]
    return fib[n]

def main():
    """Time both Fibonacci implementations for a fixed n"""
    N = 10 # feel free to play around with this parameter while prototyping

    # time a run using fib1
    t = datetime.datetime.now()
    F_N = fib1(N)
    duration = datetime.datetime.now() - t
    print(f'Computing the Fibonacci sequence using fib1 took {duration} seconds')
    print(f'The {N}-th Fibonacci number is {F_N}')

    # time a run using fib2
    t = datetime.datetime.now()
    F_N = fib2(N)
    duration = datetime.datetime.now() - t
    print()
    print(f'Computing the Fibonacci sequence using fib2 took {duration} seconds')
    print(f'The {N}-th Fibonacci number is {F_N}')


if __name__ == '__main__':
    main()