class Solution:
    def countVowelPermutation(self, n: int) -> int:
        count = [1,1,1,1,1]
        while True:
            if n == 1:
                return sum(count) % (10 ** 9 + 7)
            count = [count[1] + count[2] + count[4], count[0] + count[2], count[1] + count[3], count[2], count[2] + count[3]]
            n -= 1
            
            
