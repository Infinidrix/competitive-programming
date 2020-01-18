
# https://leetcode.com/problems/flood-fill/

class Solution:
    def __init__(self):
        self.dir = [[0,1], [0, -1], [1, 0], [-1, 0]]
    
    def fill_flood(self, image, check, sr, sc, old, new):
        for i in self.dir:
            new_sr = sr + i[0]
            new_sc = sc + i[1]
            if 0 <= new_sr < len(image) and 0 <= new_sc < len(image[0]) and not check[new_sr][new_sc] and image[new_sr][new_sc] == old:
                check[new_sr][new_sc] = True
                image[new_sr][new_sc] = new
                self.fill_flood(image, check, new_sr, new_sc, old, new)
                
    
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        check_image = [[False for i in range(len(image[0]))] for j in range(len(image))]
        oldColor = image[sr][sc]
        image[sr][sc] = newColor
        check_image[sr][sc] = True
        self.fill_flood(image, check_image, sr, sc, oldColor, newColor)
        return image
