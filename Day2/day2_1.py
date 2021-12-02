def main():
   with open("test_input.txt") as f:
      arr = [x.split(" ") for x in f.readlines()]
      x = 0
      y = 0

      for command in arr:
         if command[0] == "forward":
            x += int(command[1])
         elif command[0] == "down":
            y += int(command[1])
         elif command[0] == "up":
            y -= int(command[1])
         
      print(x * y)



if __name__ == "__main__":
   main()


