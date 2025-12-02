class Solution:
    def reverse(self, x: int) -> int:
        x = str(x)
        x = x[::-1]
        if "-" in x:
            x = x[:-1]
            x = "-"+x
        x = int(x)
        if x>(2**31-1):
            return 0
        elif x<-(2**31):
            return 0
        else:
            return x
