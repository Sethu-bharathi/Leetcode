class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left=0
        right=len(letters)-1
        fn=ord
        while left<=right:
            mid=left+(right-left)//2
            if fn(letters[mid])>fn(target) and fn(letters[mid-1])<=fn(target):
                return letters[mid]
            elif fn(letters[mid])>fn(target) and fn(letters[mid-1])>fn(target):
                right=mid-1
            else:
                left=mid+1
        return letters[0]