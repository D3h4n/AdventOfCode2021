import sys

DAYS = 18 

def main(args):
   with open("test_input.txt" if len(args) > 1 and args[1] == "-t" else "input.txt") as f:
      # map of fish timer -> number of fish
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

      # initialise map
      for fish in map(lambda x: int(x), f.readline().split(",")):
         fish_map[fish] += 1

      # iterate for n days
      for x in range(DAYS):
         # handle fish reproducing
         new_fish = fish_map[0]
         fish_map[7] += new_fish

         # iterate through other stages and iterate fish timers
         for timer in range(1, 9):
            fish_map[timer - 1] = fish_map[timer]

         # add new fish after day
         fish_map[8] = new_fish

      print(sum(fish_map.values())) # print the total number of fish

if __name__ == "__main__":
   main(sys.argv)
