class Solution:
    def containsNearbyDuplicate(self,nums ,k):
        if len(nums)==len(set(nums)):
            return False
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] == nums[j] and abs(i-j)<=k:
                    return True
        return False
        