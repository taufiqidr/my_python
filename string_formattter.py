def print_formatted(number):
    width = len(str(bin(number)[2:]))

    for i in range(1, number+1, 1):
        decimal = str(i).rjust(width)
        octal = str(oct(i)[2:]).rjust(width)
        hexa = str(hex(i)[2:]).upper().rjust(width)
        binary = str(bin(i)[2:]).rjust(width)
        print(decimal, octal, hexa, binary)

    # print(binary)


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
