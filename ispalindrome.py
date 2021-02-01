# Check whether a given string is a palindrome.
# Bart Massey 2021

# Strip all non-alphabetic characters out of the given
# string and return the remainder as lowercase.
def canonize(string):
    # Build up the result starting with the empty string.
    result = ""
    # Look at each character of the string.
    for c in string:
        # Ignore non-alphabetic characters.
        if c.isalpha():
            # Append the alphabetic character to the result.
            result = result + c
    # Lowercase and return the result.
    return result.lower()

# Check that canonize() works on some simple cases.
def test_canonize():
    # Assert statement will cause the program to crash if
    # the next expression is not True. Really useful for
    # debugging and testing.
    assert canonize('') == ''
    assert canonize('X') == 'x'
    assert canonize(' X@.yZ0  \n  ') == 'xyz'

# Return True iff (if and only if) the given string is a
# palindrome (reads the same front-to-back and
# back-to-front).
def ispalindrome(string):
    nstring = len(string)
    # Idea: work from the left and right simultaneously
    # checking that the characters there match. Stop on
    # first failure.
    for i in range(nstring):
        # XXX Here's a bug. See it?
        if string[i] != string[nstring - i - 1]:
            return False
    # Didn't find any failures, so must be OK.
    return True

# Check that ispalindrome() works on some simple cases.
def test_ispalindrome():
    assert ispalindrome('')
    assert ispalindrome('x')
    assert ispalindrome('xx')
    assert not ispalindrome('xy')
    assert ispalindrome('xyx')
    assert ispalindrome('xyyx')
    assert not ispalindrome('xyzx')


# Start by running the tests.
test_canonize()
test_ispalindrome()

# Prompt the user for a string, check and report.
candidate = input("string to test? ")
pal = ispalindrome(canonize(candidate))
if pal:
    print(f"'{candidate}' is a palindrome")
else:
    print(f"'{candidate}' is not a palindrome")
