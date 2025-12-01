class Solution:
    def convert(self, s: str, numRows: int) -> str:
        list_lines = []
        if numRows == 1:
            return s
        for line in range(numRows):
            list_lines.append('')
        i = 0
        for pos in range(len(s)):
            '''
            (i,j)
            0 -> numRows-1 (0,+1)
             -- -> 0 (+1,-1)
            (0,0)          (3,0)
            (0,1)     (2,1)(3,1)
            (0,2)(1,2)     (3,2)
            (0,3)          (3,3)
            '''
            print(i)
            if len(list_lines[i]) == 0:
                list_lines[i] = s[pos]
            else:
                list_lines[i] += s[pos]
            if i == numRows-1:
                decrement = True
            elif i == 0:
                decrement = False
            if decrement:
                i-=1
            else:
                i+=1
        exit_string = ''
        print(list_lines)
        for item in list_lines:
            exit_string+=item
        return exit_string
