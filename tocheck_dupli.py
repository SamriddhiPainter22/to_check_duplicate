class Solution:
    def duplicate(self,list1):
        new_value=set(list1)


        if len(new_value)==len(list1):
            return'false'
        else:
            return'true'

nums = [1,2,3,6,6,7,8,1]
obj=Solution()
print(obj.duplicate(nums))