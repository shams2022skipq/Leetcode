import collections


# Solution: 1 --> Easy and less optimized
def longestPalindrome(self, s: str) -> int:
    odds = sum(v & 1 for v in collections.Counter(s).values())
    return len(s) - odds + bool(odds)


print(longestPalindrome("abccccdd"))


# Solution: 2 --> Manual and less optimized
def longestPalindrome(self, s: str) -> int:
    hash = set()
    for c in s:
        if c not in hash:
            hash.add(c)
        else:
            hash.remove(c)
    # len(hash) is the number of the odd letters
    return len(s) - len(hash) + 1 if len(hash) > 0 else len(s)


# Solution: 3 --> Optimized solution
def longestPalindrome(self, s: str) -> int:
    freq = [0] * 128

    for c in s: freq[ord(c)] += 1
    OddGroup = 0
    for i in freq: OddGroup += i & 1
    return len(s) - OddGroup + (OddGroup > 0)
