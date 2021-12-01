#!/bin/python3

def main():
   with open("input.txt") as f:
      count = 0
      window_sum = 0
      prev_window_sum = 0

      arr = [int(x) for x in f.readlines()]

      prev_window_sum = arr[0] + arr[1] + arr[2]

      for i in range(3, len(arr)):
         window_sum = prev_window_sum - arr[i - 3] + arr[i]
         if (prev_window_sum < window_sum):
            count += 1

         prev_window_sum = window_sum

      print(count)

if __name__ == "__main__":
   main()
