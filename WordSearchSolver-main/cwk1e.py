def wordsearch(search_string):
    
    
    puzzle = [['R', 'U', 'N', 'A', 'R', 'O', 'U', 'N', 'D', 'D', 'L'], 
              ['E', 'D', 'C', 'I', 'T', 'O', 'A', 'H', 'C', 'Y', 'V'], 
              ['Z', 'Y', 'U', 'W', 'S', 'W', 'E', 'D', 'Z', 'Y', 'A'], 
              ['A', 'K', 'O', 'T', 'C', 'O', 'N', 'V', 'O', 'Y', 'V'], 
              ['L', 'S', 'B', 'O', 'S', 'E', 'V', 'R', 'U', 'C', 'I'], 
              ['B', 'O', 'B', 'L', 'L', 'C', 'G', 'L', 'P', 'B', 'D'], 
              ['L', 'K', 'T', 'E', 'E', 'N', 'A', 'G', 'E', 'D', 'L'], 
              ['I', 'S', 'T', 'R', 'E', 'W', 'Z', 'L', 'C', 'G', 'Y'], 
              ['A', 'U', 'R', 'A', 'P', 'L', 'E', 'B', 'A', 'Y', 'G'], 
              ['R', 'D', 'A', 'T', 'Y', 'T', 'B', 'I', 'W', 'R', 'A'], 
              ['T', 'E', 'Y', 'E', 'M', 'R', 'O', 'F', 'I', 'N', 'U']]
    
    try:
        str(search_string)
    except:
        return "Not found!"
    
    solver = Solution()
    return solver.exist(puzzle, str(search_string))
    



class Solution(object):
    
    def __init__(self):
        pass
    
    def exist(self, board, word):
        
        self.word = word.upper()
        self.found = False
        for row in range(len(board)):
            for col in range(len(board[0])):
                self.visited = []
                self.visitedSet = []
                self.dfs(board,row,col,0)
                if self.found:
                    return self.visitedSet
                    
        return "Not found!"

    
    def dfs(self,board,row,col,i):

        if i == len(self.word):
            self.found = True

        if not self.found and row >= 0 and col >= 0 and row<len(board) and col<len(board[0]) and board[row][col] == self.word[i] and (row,col) not in self.visitedSet:
            self.visited += [(row,col)]
            self.visitedSet.append((row,col))
            self.dfs(board,row+1,col-1,i+1)
            self.dfs(board,row+1,col+1,i+1)
            self.dfs(board,row-1,col-1,i+1)
            self.dfs(board,row-1,col+1,i+1)
            self.dfs(board,row+1,col,i+1)
            self.dfs(board,row-1,col,i+1)
            self.dfs(board,row,col+1,i+1)
            self.dfs(board,row,col-1,i+1)

            
        
            if not(self.found):
                self.visitedSet.remove(self.visited.pop())
