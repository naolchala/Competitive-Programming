m, n = [int(x) for x in input().split(" ")]

if m % 2 == 0:
    print(m//2 * n)
else:
    print((m//2 * n) + n//2)
