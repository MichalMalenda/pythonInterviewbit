class Solution:
    def titleToNumber(self, A):
        place=0
        for i in range(-1,-len(A)-1,-1):
            place=place+(ord(A[i])-64)*(26**(-i-1))
        return place