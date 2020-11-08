def isPalindrome(str):
    # Check for palindrome.
    n = len(str)
    for i in range(n // 2):
        if (str[i] != str[n - i - 1]):
            return False

    # palindrome string
    return True


# function to find maximum length
# substring which is not palindrome
def maxLengthNonPalinSubstring(str):
    n = len(str)
    ch = str[0]

    # to check whether all characters
    # of the string are same or not
    i = 1
    for i in range(1, n):
        if (str[i] != ch):
            break

    # All characters are same, we can't
    # make a non-palindromic string.
    if (i == n):
        return 0

    # If string is palindrome, we can make
    # it non-palindrome by removing any
    # corner character
    if (isPalindrome(str)):
        return n - 1

    # Complete string is not a palindrome.
    return n


# Driver Code
if __name__ == "__main__":
    str = "abba"
    print("Maximum length =",
          maxLengthNonPalinSubstring(str))
