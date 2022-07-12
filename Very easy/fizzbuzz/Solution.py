class Solution:
    def fizzBuzz(self, A):
        out=[]
        for x in range(A):
            if (x+1) % 3 == 0 and (x+1) % 5 == 0:
                out.append("FizzBuzz")
            elif (x+1) % 3 == 0:
                out.append('Fizz')
            elif (x+1) % 5 == 0:
                out.append('Buzz')
            else:
                out.append(x+1)
        return list(out)