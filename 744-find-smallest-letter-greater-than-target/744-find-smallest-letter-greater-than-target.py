class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left=0
        right=len(letters)-1
        while left<=right:
            mid=left+(right-left)//2
            if ord(letters[mid])>ord(target) and ord(letters[mid-1])<=ord(target):
                return letters[mid]
            elif ord(letters[mid])>ord(target) and ord(letters[mid-1])>ord(target):
                right=mid-1
            else:
                left=mid+1
        return letters[0]