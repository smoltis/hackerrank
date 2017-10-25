class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        comp = {}
        for i,num in enumerate(nums):
            prev = comp.get(num,'#') 
            if  prev != '#':
                print([comp.get(num), i])
            else:
                lookup = target-num
                comp[lookup]=i
        

if __name__ == "__main__":
    c = Solution()
    c.twoSum([2, 7, 11, 15], 9) # [1,2]