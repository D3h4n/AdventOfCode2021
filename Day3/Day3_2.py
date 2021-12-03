from io import SEEK_SET

def getMajorityBit(numbers, row):
   bits = 0

   for x in numbers:
      if x[row] == "0":
         bits += 1
      elif x[row] == "1":
         bits -= 1

   return bits
               

def main():
   with open("input.txt") as f:
      numbers = list(map(lambda num: num.strip("\n"), f.readlines()))
      c02 = numbers.copy()

      col = 0

      while len(numbers) > 1:
         # get most common bit in column
         bit = getMajorityBit(numbers, col)

         # filter numbers that have correct bit at col
         if bit > 0:
            numbers = list(filter(lambda x: x[col] == "0", numbers))
         else:
            numbers = list(filter(lambda x: x[col] == "1", numbers))

         col += 1

      col = 0

      while len(c02) > 1:
         # get most common bit in column
         bit = getMajorityBit(c02, col)

         # filter numbers that have correct bit at col
         if bit > 0:
            c02 = list(filter(lambda x: x[col] == "1", c02))
         else:
            c02 = list(filter(lambda x: x[col] == "0", c02))

         col += 1

      # convert answers to ints and print result
      print(int(numbers[0], 2) * int(c02[0], 2))

if __name__ == "__main__":
   main() 
