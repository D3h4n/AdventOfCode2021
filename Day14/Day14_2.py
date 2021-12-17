import sys

NUM_STEPS = 40

def main(args):
   with open("test_input.txt" if len(args) > 1 and args[1] == "-t" else "input.txt") as f:
      string = f.readline().strip("\n")
      pairs = {}

      f.readline() # remove space

      nums = {}
      for line in f.readlines():
         line = line.strip("\n")
         a,b = line.split(" -> ")

         pairs[a] = [b, 0]

         # init count for characters
         nums[a[0]] = 0
         nums[a[1]] = 0
         nums[b] = 0


      nums[string[0]] = 1

      # init pairs and character counts
      for i in range(len(string) - 1):
         pair = string[i] + string[i + 1]
         char, count = pairs[pair]
         pairs[pair] = [char, count + 1]
      
         nums[string[i + 1]] += 1

      for _ in range(NUM_STEPS):
         new_pairs = []
         for pair in pairs:
            c, count = pairs[pair]

            if count > 0:
               pair1 = pair[0] + c
               pair2 = c + pair[1]

               nums[c] += count
            
               pairs[pair] = [c, 0]
               new_pairs.append([pair1, count])
               new_pairs.append([pair2, count])


         for pair, add in new_pairs:
            c, count = pairs[pair]
            pairs[pair] = [c, count + add]       
      
      counts = list(nums.values())

      counts.sort(reverse=True)

      print(counts[0] - counts[-1])

if __name__ == "__main__":
   main(sys.argv) 
