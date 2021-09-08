N = int(input())


def hanoi(n, start, end, aux):

    if (n == 1):
        print(start, end)


    else:
        hanoi(n-1, start, aux, end)
        print(start, end)
        hanoi(n-1, aux, end, start)

print(2**N-1)
hanoi(N,1,3,2)