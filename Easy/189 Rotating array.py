class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        k%=len(nums)
        nums[:]=nums[-k:]+nums[:-k]
nums=list(map(int,input("enter the array").split()))
k=int(input("Number of rotations"))
