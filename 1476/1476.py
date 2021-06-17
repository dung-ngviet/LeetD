class SubrectangleQueries(object):
    
    def __init__(self, rectangle):
        """
        :type rectangle: List[List[int]]
        """
        self.rectangle = rectangle
        
    def updateSubrectangle(self, row1, col1, row2, col2, newValue):
        if col1 > col2 or row1 > row2:
            return

        for row in range(row1, row2 + 1):
            for col in range(col1, col2 + 1):
                self.rectangle[row][col] = newValue

    def getValue(self, row, col):
        return self.rectangle[row][col]
        


# Your SubrectangleQueries object will be instantiated and called as such:
# obj = SubrectangleQueries(rectangle)
# obj.updateSubrectangle(row1,col1,row2,col2,newValue)
# param_2 = obj.getValue(row,col)

obj = SubrectangleQueries([[1,2,1],[4,3,4],[3,2,1],[1,1,1]])
print(obj.getValue(0,2))
obj.updateSubrectangle(0,0,3,2,5)
print(obj.getValue(0,2))