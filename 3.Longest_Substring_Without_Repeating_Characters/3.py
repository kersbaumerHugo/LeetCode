class Solution:
 def lengthOfLongestSubstring(self, s: str) -> int:
        temp_dict = {}
        max_len = 0
        new_len = 0
        pos = 0
        for pos in range(len(s)):
            temp_str = ''
            for pos2 in range(pos,len(s)):
                if s[pos2] not in temp_str:
                    temp_str+=s[pos2]
                    #print('here')
                else:
                    break
            if len(temp_str) > max_len:
                    max_len = len(temp_str)
                
        return max_len
