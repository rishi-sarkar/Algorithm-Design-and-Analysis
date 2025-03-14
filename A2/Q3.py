# Assume its sorted from smallest to largest
def logn(A):
    l = 0
    r = len(A)-1

    while (l <= r):
        mid = (l+r) // 2
        if (A[mid] > mid):
            r = mid - 1
        elif (A[mid] < mid):
            l = mid + 1
        else:
            return True
    return False



def main():
    a = [-5, -4, 1, 2, 4]
    ans = logn(a)
    print(ans)

main()