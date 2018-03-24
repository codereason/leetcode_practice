'''
We define the Perfect Number is a positive integer that is equal to the sum of all its positive divisors except itself.

Now, given an integer n, write a function that returns true when it is a perfect number and false when it is not.
Example:
Input: 28
Output: True
Explanation: 28 = 1 + 2 + 4 + 7 + 14
Note: The input number n will not exceed 100,000,000. (1e8)
'''

class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 1:return False

        List=[]
        i =1
        while (i <= num**0.5):
            if num%i == 0 :
                List.append(i)
                List.append(num/i)
            i+=1
        List.remove(num)
        count = 0
        for i in List:
            count = count+i
        if count == num:return True
        else:return False
