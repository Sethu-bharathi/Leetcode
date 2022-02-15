class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        first,last=0,0
        while first<len(name) and last<len(typed):
            if first <len(name) and name[first]==typed[last]:
                first+=1
                last+=1
            elif last>0 and typed[last]==typed[last-1]:
                last+=1
            else:
                return 0
        while len(typed)>last and typed[last]==typed[last-1]:
            last+=1
        return len(name)==first and len(typed)==last