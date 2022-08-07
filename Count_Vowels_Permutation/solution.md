https://leetcode.com/problems/count-vowels-permutation/

```{Python}
class Solution:
    def countVowelPermutation(self, n: int) -> int:
        count = [1,1,1,1,1]
        while True:
            if n == 1:
                return sum(count) % (10 ** 9 + 7)
            count = [count[1] + count[2] + count[4], 
                     count[0] + count[2], 
                     count[1] + count[3], 
                     count[2], 
                     count[2] + count[3]]
            n -= 1
```

A list is not needed. Ints are better but I can't be bothered.

The naive approach is to simulate the process and count length of list.

We can think of each iteration as producing all possible strings by adding a character at the end of each existing string (following the rules). It turns out that only the last character matters, which means we only need to keep the last characters in the list. Even better, since these characters are the same (a, e, i, o, u), we only need to store their counts instead. 

We can deduce the count of strings ending with certain character in the next interation by looking at existing counts. E.g., only 'e' and 'u' may be followed by 'a', so in the next iteration, there is going to be (strings ending with 'e') + (strings ending with 'u') strings ending with 'a'.



