class Solution(object):
    def rotatedDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        for i in range(1, n + 1):
            num = str(i) 
            new_num = ''
            for n in num:
                if n == '3' or n == '4' or n == '7':
                    new_num = num
                    break
                elif n == '2':
                    new_num += '5'
                elif n == '5':
                    new_num += '2'
                elif n == '6':
                    new_num += '9'
                elif n == '9':
                    new_num += '6'
                else:
                    new_num += n
            
            res += 1 if new_num != num else 0
        
        return res