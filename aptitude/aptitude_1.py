a = []
a.append(2)  # 1
a.append(3)  # 2
a.append(1)  # 3
a.append(5)  # 4
a.append(7)  # 5
a.append(6)  # 6
a.append(21)  # 7
a.append(7)  # 8
a.append(11)  # 9
a.append(9)  # 10
a.append(0)  # 11
a.append(2)  # 12

a[10] = a[2] + a[10]
a[4] = a[0] + a[10]
a[11] = a[11] * a[11]
while a[4] != a[9]:
    if a[4] == a[9]:
        a[7] = a[6] - a[4]
        break
    else:
        a[11] = a[11] - 2
        a[4] = a[4] + a[1]

a[5] = a[11] + a[8]

print(a[5])
