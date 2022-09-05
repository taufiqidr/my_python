a = [1, 2, 3, 4, 5, 6]
b = [1, 2, 3, 4, 5, 6]
s = []

for i in range(len(a)):
    for j in range(len(b)):
        smu = a[i]+b[j]
        if a[i] != b[j] and smu == 6:
            s.append(smu)

print(len(s))
