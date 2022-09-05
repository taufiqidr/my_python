n = 30
k = 20

for m in range(n):

    print((n - (k % n) + m) % n)
