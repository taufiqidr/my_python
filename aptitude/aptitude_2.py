n = []
n.append(-8)  # 1
n.append(13)  # 2
n.append(1)  # 3
n.append(6)  # 4
n.append(2)  # 5
n.append(5)  # 6
n.append(13)  # 7
n.append(6)  # 8
n.append(4)  # 9
n.append(7)  # 10
n.append(5)  # 11
n.append(2)  # 12
n.append(6)  # 13
n.append(7)  # 14
n.append(9)  # 15

n[0] = n[3] - n[12]
n[0] = n[0] + n[5]

while n[0] % 4 != 0:
    if n[0] % 4 == 0:
        pass
    else:
        n[0] = n[0] + n[5+n[n[10]]]
        if n[1] > 5:
            n[9] = n[9] - 2


print(n[0])
