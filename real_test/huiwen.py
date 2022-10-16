def longestPalindrome(s: str) -> str:
    if s == s[::-1]:
        return s
    for i in range(1, len(s)):
        a, b = 0, len(s) - i
        while b <= len(s):
            if s[a:b] == s[a:b][::-1]:
                return s[a:b]
            a, b = a + 1, b + 1


if __name__ == '__main__':
    ret = longestPalindrome('abcbab')
    print(ret)
