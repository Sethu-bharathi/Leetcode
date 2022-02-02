class Solution:
    def jump(self, nums: List[int]) -> int:
        reached=0
        ladder=0
        jumps=0
        for i in range(len(nums)-1):
            ladder=max(ladder,i+nums[i])
            if reached==i:
                reached=ladder
                jumps+=1
        return jumps
                