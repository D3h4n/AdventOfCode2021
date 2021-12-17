import sys

NUM_STEPS = 40

def main(args):
   with open("test_input.txt" if len(args) > 1 and args[1] == "-t" else "input.txt") as f:
      string = f.readline().strip("\n")
      pairs = {}

      f.readline() # remove space

      for line in f.readlines():
         line = line.strip("\n")
         a,b = line.split(" -> ")

         pairs[a] = b

      for _ in range(NUM_STEPS):
         result = str(string[0])
         for i in range(len(string) - 1):
            pair = string[i] + string[i + 1]

            result += pairs[pair] + string[i + 1]

         string = result      

      nums = {}
      for c in string:
         count = nums.get(c)

         if count is None:
            nums[c] = 1
         else:
            nums[c] = count + 1

      counts = list(nums.values())

      counts.sort(reverse=True)

      print(counts[0] - counts[-1])

if __name__ == "__main__":
   main(sys.argv) 
