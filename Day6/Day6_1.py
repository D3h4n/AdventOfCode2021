import sys

DAYS = 80 

def main(args):
   with open("test_input.txt" if len(args) > 1 and args[1] == "-t" else "input.txt") as f:
      fish_list = list(map(lambda x: int(x), f.readline().split(",")))
      
      new_fish_count = 0

      for x in range(0, DAYS + 1):
         # add new fish to fish_list at the start of the new day
         fish_list.extend([8] * new_fish_count)
         new_fish_count = 0

         for i, fish in enumerate(fish_list):
            if (fish == 0):
               fish = 7
               new_fish_count += 1

            fish -= 1

            fish_list[i] = fish
         

      print(len(fish_list))

if __name__ == "__main__":
   main(sys.argv)
