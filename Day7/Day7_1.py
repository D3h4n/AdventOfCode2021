import sys
from functools import reduce

def main(args):
   with open("test_input.txt" if len(args) > 1 and args[1] == "-t" else "input.txt") as f:
      nums = list(map(lambda x: int(x), f.readline().split(',')))

      min_val = reduce(lambda x, y: min(x, y), nums)
      max_val = reduce(lambda x, y: max(x, y), nums)

      min_fuel = float('inf')

      # don't like this solution but it works
      # tried using statistics and failed :^(
      for i in range(min_val, max_val + 1):
         total = 0
         for num in nums:
            total += abs(i - num)

         min_fuel = min(total, min_fuel)

      print(min_fuel)

if __name__ == "__main__":
   main(sys.argv) 
