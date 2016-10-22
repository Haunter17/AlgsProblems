class Solution:
    # @param board, a list of lists of 1 length string
    # @param word, a string
    # @return a boolean
    def exist(self, board, word):
        # write your code here
        if len(board) == 0 or len(board[0]) == 0:
        	return False

        visited = [[False for x in range(len(board[0]))] for y in range(len(board))]
        for row in range(len(board)):
        	for col in range(len(board[0])):
        		if self.wordSearch(board, word, row, col, 0, visited):
        			return True

        return False

    def wordSearch(self, board, word, row, col, index, visited):
    	if index == len(word):
    		return True
    	if row < 0 or col < 0 or row >= len(board) or col >= len(board[0]) \
    		or visited[row][col] or board[row][col] != word[index]:
    		return False

    	visited[row][col] = True
    	diffRow = [1,-1,0,0]
    	diffCol = [0,0,1,-1]
    	for i in range(len(diffRow)):
    		opt = self.wordSearch(board, word, row + diffRow[i], col + diffCol[i], index + 1, visited)
    		if opt:
    			return True
    	visited[row][col] = False
    	return False



board = [
  "ABCE",
  "SFCS",
  "ADEE"
]
word = "ASADC"
soln = Solution()
print soln.exist(board, word)