def binary_to_grey(n):
    if not(n):
        return 0

    a = n % 10

    b = int(n/10) % 10

    if(a and not(b)) or (not(a) and b):
        return (1 + 10 * binary_to_grey(int(n/10)))

    return (10 * binary_to_grey(int(n/10)))

binary_number = 1011101
print(binary_to_grey(binary_number), end='')
