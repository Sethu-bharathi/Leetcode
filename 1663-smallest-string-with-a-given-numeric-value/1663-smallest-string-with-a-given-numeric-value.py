class Solution:
        def getSmallestString(self, n: int, k: int) -> str:
            z, r = divmod(k - n, 25)
            return ('' if z == n else 'a' * (n - z - 1) + chr(ord('a') + r)) + 'z' * z