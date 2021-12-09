from functools import reduce
import sys

class bcolors:
   HEADER = '\033[95m'
   OKBLUE = '\033[94m'
   OKCYAN = '\033[96m'
   OKGREEN = '\033[92m'
   WARNING = '\033[93m'
   FAIL = '\033[91m'
   ENDC = '\033[0m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'

def main(args):
   with open("test_input.txt" if len(args) > 1 and args[1] == "-t" else "input.txt") as f:
      heights = []
      lowest = []

      for line in f.readlines():
         line = line.strip("\n")
         heights.append(list(map(lambda x: int(x), list(line))))

      for i, row in enumerate(heights):
         low = True
         for j, col in enumerate(row):
            # check left
            try:
               low = col < row[j - 1]
            except:
               pass
            
            # check right
            try:
               low = low and col < row[j + 1]
            except:
               pass

            # check up
            try:
               low = low and col < heights[i - 1][j]
            except:
               pass

            # check down
            try:
               low = low and col < heights[i + 1][j]
            except:
               pass

            if low:
               lowest.append((i, j, col))

      sizes = []

      visited = {}
      for low_point in lowest:
         queue = [low_point]
         size = 0

         while len(queue):
            # visit node
            (i, j, val) = queue.pop(0)
            
            if visited.get((i, j)) is not None or val == 9:
               continue

            size += 1
            visited[(i, j)] = True

            row = heights[i]

            # check left
            if j > 0:
               left = row[j - 1]

               if left > val:
                  queue.append((i, j - 1, left))
            # check right
            try:
               right = row[j + 1]

               if right > val:
                  queue.append((i, j + 1, right))
            except:
               pass

            # check up
            if i > 0:
               up = heights[i - 1][j]

               if up > val:
                  queue.append((i - 1, j, up))
               
            # check down
            try:
               down = heights[i + 1][j]

               if down > val:
                  queue.append((i + 1, j, down))
            except:
               pass
         
         visited[low_point[:2]] = False
         sizes.append(size)

      for i, row in enumerate(heights):
         for j, col in enumerate(row):
            typ = visited.get((i, j))

            if typ == False:
               sys.stdout.write(f"{bcolors.FAIL}{col}{bcolors.ENDC}")
            elif typ:
               sys.stdout.write(f"{bcolors.OKGREEN}{col}{bcolors.ENDC}")
            else:
               sys.stdout.write(str(col))
         sys.stdout.write("\n")

      sizes.sort(reverse=True)
      print(sizes[:3], sizes[0] * sizes[1] * sizes[2])

if __name__ == "__main__":
   main(sys.argv) 
