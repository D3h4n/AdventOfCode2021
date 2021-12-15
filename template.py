import sys

def main(args):
   with open("test_input.txt" if len(args) > 1 and args[1] == "-t" else "input.txt") as f:
      for x in f.readlines():
         print(x)

if __name__ == "__main__":
   main(sys.argv) 
