class Solution:
    
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        self.minm = float('inf')
        cookies.sort(reverse = True)
        self.bucket = [0] * k
        self.fair(cookies, 0, k)
        return self.minm

    def fair(self, cookies, idx, k):
        # if k == len(cookies):
        #     self.minm = max(cookies)
        #     return

        if idx >= len(cookies):
            self.minm = min(self.minm, max(self.bucket))
            return

        if self.minm < max(self.bucket) :
            return 

        for i in range(k):
            self.bucket[i] += cookies[idx]
            self.fair(cookies, idx + 1, k)
            self.bucket[i] -= cookies[idx]
        return