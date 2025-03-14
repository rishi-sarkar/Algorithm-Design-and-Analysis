import math

################################################################################
# PROGRAMMING QUESTION SUBMISSION INSTRUCTIONS FOR A1Q5
#   1. Write your username and student number in the box below
#   2. Submit your code as A1Q5-<WatIAMusername>.py to the LEARN Dropbox
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


# part (i) for modular exponentiation -- fill in the code below
def modexp(x, y, N):
    if y == 0:
        return 1
    z = modexp(x, math.floor(y/2), N)
    if y % 2 == 0:  # y is even
        return (z * z) % N
    else:  # y is odd
        return (x * z * z) % N


# part (ii) for extended Euclid  -- fill in the code below
def extended_euclid(a, b):
    if b == 0:
        return (1, 0, a)
    (x_a, y_a, d) = extended_euclid(b, a % b)
    return (y_a, x_a-(math.floor(a/b)*y_a), d)


def main():
    """
    Testing the two functions on a few inputs
    """
    # testing modular exponentiation
    if modexp(10, 1200, 14) == 8:
        print("modexp passed test 1")
    else:
        print("modexp failed test 1")

    # modexp -- test 2
    if modexp(325942, 25000000, 7) == 1:
        print("modexp passed test 2")
    else:
        print("modexp failed test 2")

    # testing extended Euclid
    (x, y, d) = extended_euclid(125, 15)
    if d == 5 and x*125 + y*15 == d:
        print("extended_euclid passed test 1")
    else:
        print("extended_euclid failed test 1")

    # extended_euclid -- test 2
    (x, y, d) = extended_euclid(10203040, 20304)
    if d == 16 and x*10203040 + y*20304 == d:
        print("extended_euclid passed test 2")
    else:
        print("extended_euclid failed test 2")


if __name__ == '__main__':
    main()
