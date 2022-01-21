class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if c*r!=len(mat)*len(mat[0]):
            return mat
        output=[[]]
        for i in mat:
            for j in i:
                if(len(output[-1])!=c):
                    output[-1].append(j)
                else:
                    output.append([j])
        return output
                