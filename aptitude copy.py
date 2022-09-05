a = []
a.append(6)  # 1
a.append(3)  # 2
a.append(9)  # 3
a.append(2)  # 4
a.append(11)  # 5
a.append(2)  # 6
a.append(91)  # 7
a.append(48)  # 8
a.append(66)  # 9
a.append(1)  # 10


a[6] = a[3] + a[1]
a[5] = a[6] + a[1]

print(a[5]*a[0])
