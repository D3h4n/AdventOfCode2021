def main():
   with open("input.txt") as f:
      arr = [x.split(" ") for x in f.readlines()]
      x = 0
      y = 0
      aim = 0;

      for command in arr:
         value = int(command[1])

         if command[0] == "forward":
            y += value * aim 
            x += value
         elif command[0] == "down":
            aim += value
         elif command[0] == "up":
            aim -= value
         
      print(x * y)


if __name__ == "__main__":
   main()
