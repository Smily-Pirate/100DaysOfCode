def sumVowel(string):
    n = len(string)
    sum = 0
    string = string.lower()

    for i in range(0, n):
        s = string[i]
        if (s == "a" or s == "e" or s == "i" or s == "o" or s == "u"):
            sum += ((n - i) * (i + 1))

    return sum


if __name__ == '__main__':
    string = "ghanshyam"
    print(sumVowel(string))
