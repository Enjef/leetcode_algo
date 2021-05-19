class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = 'aeiou'
        s = list(s)
        i, j = 0, len(s) - 1
        while i < j:
            while i < j and lower(s[i]) not in vowels:
                i += 1
            while i < j and lower(s[j]) not in vowels:
                j -= 1
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        return "".join(s)