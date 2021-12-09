import sys

def main(args):
   with open("test_input.txt" if len(args) > 1 and args[1] == "-t" else "input.txt") as f:
      heights = []
      lowest = []

      for line in f.readlines():
         line = line.strip("\n")
         heights.append(list(map(lambda x: int(x), list(line))))

      for i, row in enumerate(heights):
         for j, col in enumerate(row):
            # top row
            if i == 0:
               # top left corner
               if j == 0:
                  if col < row[j + 1] and col < heights[i + 1][j]:
                     lowest.append(col)
               # top right corner
               elif j == len(row) - 1:
                  if col < row[j - 1] and col < heights[i + 1][j]:
                     lowest.append(col)
               # middle of top row
               elif col < row[j - 1] and col < row[j + 1] and col < heights[i + 1][j]:
                  lowest.append(col)
            # bottom row
            elif i == len(heights) - 1:
               # bottom left
               if j == 0 and col < row[j + 1] and col < heights[i - 1][j]:
                  lowest.append(col)
               # bottom right
               elif j == len(row) - 1 and col < row[j - 1] and col < heights[i - 1][j]:
                  lowest.append(col)
               # middle of bottom row
               elif col < row[j - 1] and col < row[j + 1] and col < heights[i - 1][j]:
                  lowest.append(col)
            # centre of map
            else:
               # left edge
               if j == 0:
                  if col < row[j + 1] and col < heights[i + 1][j] and col < heights[i - 1][j]:
                     lowest.append(col)
               # right edge
               elif j == len(row) - 1: 
                  if col < row[j - 1] and col < heights[i + 1][j] and col < heights[i - 1][j]:
                     lowest.append(col)
               # center centre
               elif col < row[j - 1] and col < row[j + 1]  and col < heights[i + 1][j] and col < heights[i - 1][j]:
                  lowest.append(col)

      print(sum(map(lambda x: x + 1, lowest)))
if __name__ == "__main__":
   main(sys.argv) 
