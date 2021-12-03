from functools import reduce

def main():
   with open("input.txt") as f:
      numbers = list(map(lambda x: x.strip("\n"), f.readlines()))
      bits = [0] * len(numbers[0])

      # get most popular bit for each column
      for x in numbers:
         for i in range(len(x)):
            if x[i] == "0":
               bits[i] += 1
            elif x[i] == "1":
               bits[i] -= 1
               
      gammaRate = list(map(lambda x: "0" if x > 0 else "1", bits)) # convert into ascii values
      gammaRate = reduce(lambda a, b: a + b, gammaRate, "") # condense array into binary string
      gammaRate = int(gammaRate, 2) # convert binary string to int

      epsilonRate = list(map(lambda x: "1" if x > 0 else "0", bits)) # convert into ascii values
      epsilonRate = reduce(lambda a, b: a + b, epsilonRate, "") # condense array into binary string
      epsilonRate = int(epsilonRate, 2) # convert binary string to int

      print(gammaRate * epsilonRate)

      pass

if __name__ == "__main__":
   main() 
