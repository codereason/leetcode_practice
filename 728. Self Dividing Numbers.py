'''
A self-dividing number is a number that is divisible by every digit it contains.

For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.

Also, a self-dividing number is not allowed to contain the digit zero.

Given a lower and upper number bound, output a list of every possible self dividing number, including the bounds if possible.

Example 1:
Input: 
left = 1, right = 22
Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
Note:

The boundaries of each input argument are 1 <= left <= right <= 10000.
'''

class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        List=[]
        count = 0
        for i in range(left,right+1):
            List2 = []
            num1 = i
            while(num1):
                num = num1%10
                List2.append(num)
                num1 = num1/10
            # print List2
            if 0 in List2:continue //处理有0的 digit 情况，直接继续循环即可
            flag = True
            for digit in List2:
                # print digit
                
                if i%digit != 0:
                    flag = False
            if flag == True:
                List.append(i)
                # print  List
        return List
