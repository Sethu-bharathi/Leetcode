class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        matrix1=[]
        for i in range(len(matrix[0])):
            matrix1.append([])
            for j in range(len(matrix)):
                matrix1[-1].append(matrix[j][i])
        return matrix1