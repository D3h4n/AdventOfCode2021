import sys

def main(args):
   with open("test_input.txt" if args[0] == "-t" else "input.txt") as f:
      pass

if __name__ == "__main__":
   main(sys.argv) 
