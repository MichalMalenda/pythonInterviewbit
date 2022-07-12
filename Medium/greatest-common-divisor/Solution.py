class Solution:
    def gcd(self, A, B):
        return B if A==0 else self.gcd(B%A,A)