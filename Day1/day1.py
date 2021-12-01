#!/bin/python3

def main():
   with open("input.txt") as f:
      prev = int(f.readline())

      count = 0

      for x in f.readlines():
         if int(x) > prev:
            count += 1 

         prev = int(x)

      print(count)

if __name__ == "__main__":
   main()
