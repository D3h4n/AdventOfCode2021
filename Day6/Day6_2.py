import sys

DAYS = 256 

def main(args):
   with open("test_input.txt" if len(args) > 1 and args[1] == "-t" else "input.txt") as f:
      fish_map = {
         0: 0,
         1: 0,
         2: 0,
         3: 0,
         4: 0,
         5: 0,
         6: 0,
         7: 0,
         8: 0
      }

      for fish in map(lambda x: int(x), f.readline().split(",")):
         fish_map[fish] += 1

      for x in range(DAYS):
         print(f"Day {x}", list(fish_map.values()))
         
         new_fish = fish_map[0]
         fish_map[0] = 0
         fish_map[7] += new_fish

         for timer in range(1, 9):
            fish = fish_map[timer]
            fish_map[timer] = 0
            fish_map[timer - 1] = fish

         fish_map[8] = new_fish

      print(f"Day {DAYS}", list(fish_map.values()))
      num_fish = sum(fish_map.values())
      print(num_fish)
            


if __name__ == "__main__":
   main(sys.argv)
