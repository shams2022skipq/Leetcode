# Solution No: 1 --> Not optimized
def isPalindrome(string):
    new_str = ""

    for c in string:
        if c.isalnum():
            new_str += c.lower()
    return new_str == new_str[::-1]


s = 'A man, a plan, a canal: Panama'
print(isPalindrome(s))


# Solution No: 2 --> Better memory management and bad running time
def alpha_num(character):
    return (ord('A') <= ord(character) <= ord('Z') or
            ord('a') <= ord(character) <= ord('z') or
            ord('0') <= ord(character) <= ord('9'))


def is_palindrome(string):
    left, right = 0, len(string) - 1

    while left < right:
        while left < right and not alpha_num(string[left]):
            left += 1
        while right > left and not alpha_num(string[right]):
            right -= 1
        if string[left].lower() != string[right].lower():
            return False
        left, right = left + 1, right - 1
    return True


s = 'A man, a plan, a canal: Panama'
print(is_palindrome(s))


# Solution : 3 --> Another approach
def isPalindrome(self, s: str) -> bool:
    left = ""
    for i in s:
        if i.isalpha():
            left = left + i.lower()

        if i.isnumeric():
            left = left + i
    # print(l)
    if left == left[::-1]:
        return True

    return False
