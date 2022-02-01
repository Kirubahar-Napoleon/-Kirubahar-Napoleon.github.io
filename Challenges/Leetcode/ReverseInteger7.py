# Given a signed 32-bit integer x, return x with its digits reversed. 
# If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

# Example 1:

# Input: x = 123
# Output: 321
# Example 2:

# Input: x = -123
# Output: -321
# Example 3:

# Input: x = 120
# Output: 21
 

# Constraints:
# -231 <= x <= 231 - 1

#This can be just accomplished by using string conversion and if statements as below,
class Solution:
    def reverse(self, x: int) -> int:
        self.num = x
        if self.num < 0 and int(str(self.num)[0]+str(self.num)[1::][::-1]) < (-2**31):
            return 0
        elif self.num < 0:
            return int(str(self.num)[0]+str(self.num)[1::][::-1])
        elif self.num > 0 and int((str(self.num)[::-1])) > (2**31 - 1):
            return 0
        else:
            return int((str(self.num)[::-1]))

x = Solution()
print(x.reverse(123))


#Alternatively, we could use algorothm to solve this as below,
class AlgoSolution:
    def reverse(self, num: int) -> int:
        sum = 0
        sign = 1
        if num < 0: #trying to check if the integet is in negative
            sign = -1 #Setting the sign to negative
            num = num*sign #Converting the num to positive by multiplying with -1
        while num > 0:
            x = num % 10
            sum = sum*10 + x
            num = num // 10
        # What we are doing here is that, we are first get the remainder of the value by diving it by 10.
        # If the value is 123, we will get the remainder as 3
        # Now we are multiplying sum with 10 and adding the remainder which gives 0 * 10 + 3 = 3
        # we are then changing the number as its quotient num = num // 10. thje quotient here will be 12
        # since the num is greater than 0 the loop will be executed again and this now will result in remainder of 2 and quotient as 1
        # sum will be now 3*10 + 2 = 32 -> as we could see the number is reversing
        # the num // 10 allows us to have only integer value and not float, so when we divide 1 / 10 in the next execution, we get a remainder of 1 which will add to num as last digit, but quotient will be 0.1
        # the // operator will only hand back 0 as the value which is less than 0 so the while loop will exit and we will have a sum as 321.
        
        
        sum = sum * sign # we are now setting back the value to either positive or nrgative as what we have received.

        if (-2**31) <= sum >= ((2**31) - 1):
            return 0
        else:
            return sum

