if __name__ == '__main__':
    ss = input()
    alnum = []
    alpha = []
    digit = []
    low = []
    up = []
    for s in ss:
        alnum.append(s.isalnum())
        alpha.append(s.isalpha())
        digit.append(s.isdigit())
        low.append(s.islower())
        up.append(s.isupper())

    print(any(alnum))
    print(any(alpha))
    print(any(digit))
    print(any(low))
    print(any(up))
