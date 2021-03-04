def is_palindrome_reverse(s):
    # https://www.geeksforgeeks.org/reverse-string-python-5-different-ways/
    return s == ''.join(reversed(s))

def is_palindrome_iterate(s):
    n = len(s)
    for i in range(n // 2):
        if s[i] != s[n - 1 - i]:
            return False
    return True

big_palindrome = "a" * 10**8
big_fake = "b" + "a" * (10**8 - 1)

print("starting")
print("rp", is_palindrome_reverse(big_palindrome))
print("ip", is_palindrome_iterate(big_palindrome))
print("rf", is_palindrome_reverse(big_fake))
print("if", is_palindrome_iterate(big_fake))
