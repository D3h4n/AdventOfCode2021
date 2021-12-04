import sys

class bingo_board:
   def __init__(self, board, size):
      self.table = self.create_table(board)
      self.size = size
      self.rows = [0] * size
      self.cols = [0] * size
      self.won = False 
   
   def update_board(self, number):
      try:
         [_val, x, y, marked] = self.table[number]

         if marked == False:
            self.rows[x] += 1
            self.cols[y] += 1
            self.table[number][3] = True

      except KeyError:
         pass


   def check_bingo(self):
      for row in self.rows:
         if (row == self.size):
            return True

      for col in self.cols:
         if (col == self.size):
            return True

      return False


   def sum_unmarked(self):
      sum = 0

      for x in list(self.table.values()):
         if not x[3]:
            sum += x[0]
          
      
      return sum

   @staticmethod
   def create_table(board):
      table = {}

      for row, r_val in enumerate(board):
         for col, c_val in enumerate(r_val):
            table[c_val] = [c_val, row, col, False] # thinking about making this a dataclass

      return table

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
            boards.append(bingo_board(board, len(board[0])))
            board = []

      boards.append(bingo_board(board, len(board[0])))

      for num in numbers:
         if not len(boards):
            break

         for board in boards:
            if board.won:
               continue

            board.update_board(num)
            
            if board.check_bingo():
               print (num * board.sum_unmarked())
               board.won = True

if __name__ == "__main__":
   main(sys.argv) 
