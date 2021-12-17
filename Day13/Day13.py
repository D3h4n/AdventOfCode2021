import sys

READ_POINTS = 0
READ_FOLDS = 1

def main(args):
   with open("test_input.txt" if len(args) > 1 and args[1] == "-t" else "input.txt") as f:
      mode = READ_POINTS

      points = set()
      folds = []


      for line in f.readlines():
         line = line.strip("\n")

         if mode == READ_POINTS:
            if len(line) == 0:
               mode = READ_FOLDS
               continue
            else:
               [x, y] = line.split(",")
               points.add((int(x), int(y)))
         elif mode == READ_FOLDS:
            folds.append(line.split(" ")[2].split("="))

      for fold, val in folds:
         remove_points = []
         add_points = []

         line = int(val)

         if fold == "x":
            for point in points:
               if point[0] >= line:
                  remove_points.append(point)

                  if point[0] > line:
                     add_points.append((line + line - point[0], point[1]))
         elif fold == "y":
            for point in points:
               if point[1] >= line:
                  remove_points.append(point)

                  if point[1] > line:
                     add_points.append((point[0], line + line - point[1]))
      
         for point in remove_points:
            points.remove(point)

         for point in add_points:
            points.add(point)

      max_x = 0
      max_y = 0

      for x, y in points:
         max_x = max(max_x, x)
         max_y = max(max_y, y)

      for y in range(max_y + 1):
         for x in range(max_x + 1):
            if (x, y) in points:
               sys.stdout.write("#")
            else:
               sys.stdout.write(".")
         sys.stdout.write("\n")

if __name__ == "__main__":
   main(sys.argv) 
