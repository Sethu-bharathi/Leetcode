class Solution:
    def average(self, salary: List[int]) -> float:
        if len(salary)<3:
            return 0
        min_sal=min(salary)
        max_sal=max(salary)
        count= (sum(salary)-max_sal-min_sal)
        return (count/(len(salary)-2))
        