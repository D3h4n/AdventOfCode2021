from itertools import permutations
from functools import reduce
from typing import Set
import sys

# convert values to ordered set of wires
val_to_display = {
   0: "abcefg",
   1: "cf",
   2: "acdeg",
   3: "acdfg",
   4: "bcdf",
   5: "abdfg",
   6: "abdefg",
   7: "acf",
   8: "abcdefg",
   9: "abcdfg"
}

# convert ordered set of wires to value
display_to_val = {
   "abcefg": 0,
   "cf": 1,
   "acdeg": 2,
   "acdfg": 3,
   "bcdf": 4,
   "abdfg": 5,
   "abdefg": 6,
   "acf": 7,
   "abcdefg": 8,
   "abcdfg": 9
}

# convert the number of wires to a known value
len_to_val = {
   2: 1,
   3: 7,
   4: 4,
   7: 8
}

def get_display(map_value, map_string, query_value):
   # get original displays for values
   map_og_display = val_to_display[map_value]
   val_og_display = val_to_display[query_value]

   assert(len(map_string) == len(map_og_display))
   assert(len(val_og_display) <= len(map_og_display))
 
   mapping = {}

   # create map of letters from the original map to the new map
   for i, c in enumerate(map_og_display):
      mapping[c] = map_string[i]

   # use letters to figure out what the query_value would be in the input map
   output = ""
   for c in val_og_display:
      output += mapping[c]

   return output

def get_val(map_string, input_string):
   mapping = {}

   # create a mapping from map_string to base
   for i, c in enumerate(map_string):
      mapping[c] = "abcdefg"[i]

   # convert from mapped string to base string
   resolved_string = ""

   for c in input_string:
      resolved_string += mapping[c]

   # get all permutations of the resolved string
   possible_strings = list(map(lambda arr: reduce(lambda a, b: a + b, arr), list(permutations(list(resolved_string)))))
   
   val = -1

   # try to get the value from one of the permutations
   for string in possible_strings:
      try:
         val = display_to_val[string]
         break
      except:
         pass

   return val

def main(args):
   # tests
   assert(get_display(8, "gfedcba", 1) == "eb")
   assert(get_display(8, "gfedcba", 7) == "geb")
   assert(get_display(8, "gfedcba", 4) == "fedb")
   assert(get_display(7, "fca", 1) == "ca")
   assert(get_display(4, "fdcb", 1) == "db")

   assert(get_val("gfedcba", "eb") == 1)
   assert(get_val("gfedcba", "geb") == 7)

   with open("test_input.txt" if len(args) > 1 and args[1] == "-t" else "input.txt") as f:
      notes = []

      # get entries
      for line in f.readlines():   
         vals = line.strip("\n").split(" | ")
         notes.append({
            "input": vals[0].split(" "), 
            "output": vals[1].split(" ")
         })

      total = 0
      
      # for each note get all possible values for 1, 4, 7 and 8
      for note in notes:
         mappings = {
            1: [],
            4: [],
            7: [],
            8: []
         }

         # get all possible mappings for 1, 4, 7 and 8 
         for val in note["input"]:
            idx = len(val)

            if len_to_val.get(idx) is not None:
               mappings[len_to_val[idx]] += list(map(lambda arr: reduce(lambda prev, curr: prev + curr, arr), permutations(list(val))))

         # create maps dictionary to store valid mappings
         maps = dict(map(lambda x: (x, 1), mappings[1]))

         # test 7 maps against 1 maps
         for mapping in mappings[7]:
            try:
               maps[get_display(7, mapping, 1)]

               maps[mapping] = 7
            except Exception:
               pass

         # test 4 maps against 1 maps
         for mapping in mappings[4]:
            try:
               maps[get_display(4, mapping, 1)]

               maps[mapping] = 4
            except Exception:
               pass

         possible_maps = []

         # test 8 maps against 1, 4 and 7 maps
         for mapping in mappings[8]:
            try:
               maps[get_display(8, mapping, 1)]
               maps[get_display(8, mapping, 4)]
               maps[get_display(8, mapping, 7)]

               possible_maps.append(mapping)
            except Exception:
               pass
      
         # for each possible map try to decode the input
         for test in note["input"]:
            failures = []
            count = 0
            for possible_map in possible_maps:
               if get_val(possible_map, test) == -1:
                  failures.append(possible_map)

            for failure in failures:
               possible_maps.remove(failure)
               count += 1

         # get the first valid map
         [mapping] = possible_maps

         # generate the output for that entry
         result = 0         
         for output in note["output"]:
            result = (result * 10) + get_val(mapping, output)

         # add to total
         total += result

      print(total)
         

if __name__ == "__main__":
   main(sys.argv) 
