import sys

class bingo_board:
   def __init__(self, board):
      self.board, self.table = self.create_board(board)
   
   def update_board(self, number):
      try:
         x, y = self.table[number]

         self.board[x][y][1] = True
      except KeyError:
         pass

   def check_bingo(self):
      for row in self.board:
         count = 0

         for col in row:
            if not col[1]:
               break
            else:
               count += 1
         
         if (count == len(self.board[0])):
            return True
      
      return False

   def sum_unmarked(self):
      sum = 0

      for row in self.board:
         for col in row:
            if (not col[1]):
               sum += col[0]
      
      return sum

   @staticmethod
   def create_board(board):
      newBoard = []
      table = {}

      for row in range(len(board)):
         newRow = []
         for col in range(len(board[row])):
            table[board[row][col]] = (row, col)
            newRow.append([board[row][col], False])
         
         newBoard.append(newRow)

      return newBoard, table

def main(args):
   file = "test_input.txt" if len(args) > 1 and args[1] == "-t" else "input.txt"
   with open(file) as f:
      numbers = list(map(lambda x: int(x), f.readline().split(",")))

      board = []
      boards = []

      f.readline() # skip empty line
      for row in f.readlines():
         row = row.strip("\n")
         newRow = []
         if (len(row)):
            for num in row.split():
               newRow.append(int(num))
            
            board.append(newRow)
         else:
            boards.append(bingo_board(board))
            board = []

      boards.append(bingo_board(board)) #add last board

      for num in numbers:
         for board in boards:
            board.update_board(num)
            
            if board.check_bingo():
               print (num * board.sum_unmarked())
               exit(0)

if __name__ == "__main__":
   main(sys.argv) 
