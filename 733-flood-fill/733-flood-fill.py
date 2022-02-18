class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        if not len(image) or image[sr][sc]==newColor:
            return image

        color=image[sr][sc]
        R,L=len(image),len(image[0])
        def dfs(r,c):
            if image[r][c]==color:
                image[r][c]=newColor
                if r-1>=0:
                    dfs(r-1,c)
                if r+1<R:
                    dfs(r+1,c)
                if c>=1:
                    dfs(r,c-1)
                if c+1<L:
                    dfs(r,c+1)
        dfs(sr,sc)
        return image
                    
            