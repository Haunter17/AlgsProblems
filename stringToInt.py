from sets import Set
class Solution:
    # @param str: a string
    # @return an integer
    def atoi(self, s):
        # write your code here
        num = 0
        positive = True
        MAX = 2147483647
        MIN = -MAX - 1
        
        
        # empty: return 0
        if len(s) == 0:
            return 0
        
        s = s.replace(' ','')
        valid = Set(['0', '1', '2', '3','4', \
        '5', '6', '7','8','9', '.'])
        
        # if only one char
        if (len(s) == 1 and s[0] not in valid) or s[0] == '.':
            return 0
            
        if s[0] == '-':
            positive = False
            s = s[1:]
        if s[0] == '+':
            s = s[1:]
        
        # processing invalid input and dots
        # dotCnt = 0
        # for ch in s:
        #     if ch not in valid:
        #         return 0
        #     if ch == '.':
        #         dotCnt += 1
                
        # if dotCnt >= 2:
        #     return 0
        # if dotCnt == 1:
        #     dotIndex = s.index('.')
        #     for ch in s[dotIndex + 1:]:
        #         if ch != '0':
        #             return 0
        #     s = s[:dotIndex]
        validUntil = 0
        while validUntil < len(s):
            if s[validUntil] not in valid or s[validUntil] == '.':
                break
            validUntil += 1

        s = s[:validUntil]
        
        for ch in s:
            num = 10 * num + int(ch)
            if positive and num > MAX:
                num = MAX
                break
            if not positive and num > MAX + 1:
                num = MAX + 1
                break
        
        if not positive:
            num = -num
        return num

s = '+52113.14era.23'
print Solution().atoi(s)