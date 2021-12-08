import sys

mapping = {
   2: 1,
   3: 7,
   4: 4,
   5: 5,
   6: 5,
   7: 8
}

def main(args):
   with open("test_input.txt" if len(args) > 1 and args[1] == "-t" else "input.txt") as f:
      counts = {
         1: 0,
         4: 0,
         7: 0,
         8: 0,
         5: 0
      }

      for line in f.readlines():
         [inp, out] = line.strip("\n").split(" | ")

         for val in out.split(" "):
            if len(val):
               counts[mapping[len(val)]] += 1

      print(sum(map(lambda x: x[1], filter(lambda x: x[0] != 5, counts.items()))))


if __name__ == "__main__":
   main(sys.argv) 
