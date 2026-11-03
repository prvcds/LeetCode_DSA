class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ['a','e','i','o','u']
        wdo = s[:k]
        count = 0
        for i in wdo:
            if i in vowels:
                count+=1
        current_max = count

        for i in range(k,len(s)):
            if s[i-k] in vowels:
                count-=1
            if s[i] in vowels:
                count+=1

            current_max = max(current_max,count)

        return current_max          