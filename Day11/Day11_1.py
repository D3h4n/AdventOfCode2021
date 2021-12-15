from dataclasses import dataclass
from types import *
import sys

NUM_DAYS = 100

# Yay! I finally did data classes
@dataclass 
class Octopus:
   pos: tuple[int, int]
   energy: int

   def __hash__(self):
      return self.pos.__hash__()

# position shifts
TOP_LEFT = (-1, -1)
TOP_MIDDLE = (0, -1)
TOP_RIGHT = (1, -1)

LEFT = (-1, 0)
RIGHT = (1, 0)

BOTTOM_LEFT = (-1, 1)
BOTTOM_MIDDLE = (0, 1)
BOTTOM_RIGHT = (1, 1)

POSITIONS = [TOP_LEFT, TOP_MIDDLE, TOP_RIGHT, LEFT, RIGHT, BOTTOM_LEFT, BOTTOM_MIDDLE, BOTTOM_RIGHT]

total = 0

def getPos(pos, shift) -> tuple[int, int]:
   return tuple(map(sum, zip(pos, shift)))

def glow(octopodes: dict[Octopus], octo: Octopus, tired: set[Octopus]):
   global total

   total += 1
   octo.energy = 0

   tired.add(octo)

   for shift in POSITIONS:
      newPos = getPos(octo.pos, shift)

      try:
         adj = octopodes[newPos]

         if adj not in tired:
            if adj.energy == 9:
               glow(octopodes, adj, tired)
            else:
               adj.energy += 1
      except:
         pass

def main(args):
   with open("test_input.txt" if len(args) > 1 and args[1] == "-t" else "input.txt") as f:
      global total

      octopodes = {}

      rows = [x.strip('\n') for x in f.readlines()]

      for y, row in enumerate(rows):
         for x, col in enumerate(row):
            new = Octopus((x, y), int(col))
            octopodes[new.pos] = new

      for _ in range(NUM_DAYS):
         tired = set()
         for octopus in octopodes.values():
            if octopus not in tired:
               octopus.energy += 1

               if octopus.energy > 9:
                  glow(octopodes, octopus, tired)

      print(total)
         

if __name__ == "__main__":
   main(sys.argv) 
