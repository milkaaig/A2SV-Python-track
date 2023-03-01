from collections import defaultdict

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        longest = 0
        trees = len(fruits)
        left = 0
        freq = defaultdict(int)

        for right in range(trees):
            freq[fruits[right]] = right
            # print(fruits[left: right])
            # print(count)
            while len(freq) > 2:
                remove = min(freq, key = lambda x : freq[x])
                index = freq[remove]
                del freq[remove]
                left = index + 1

            longest = max(longest, right - left + 1)

        return longest