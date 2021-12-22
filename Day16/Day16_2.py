from functools import reduce, total_ordering
import sys
from types import prepare_class

def main(args):
   with open("test_input.txt" if len(args) > 1 and args[1] == "-t" else "input.txt") as f:
      hex_to_bin = {
         "0": "0000",
         "1": "0001",
         "2": "0010",
         "3": "0011",
         "4": "0100",
         "5": "0101",
         "6": "0110",
         "7": "0111",
         "8": "1000",
         "9": "1001",
         "A": "1010",
         "B": "1011",
         "C": "1100",
         "D": "1101",
         "E": "1110",
         "F": "1111",
      }
      
      decoded = ""

      transmission = f.readline().strip("\n")

      for x in transmission:
         decoded += hex_to_bin[x]

      val, packet = parse_packet(decoded)

      print(val)

def parse_packet(packet):
   v = int(packet[:3], base=2)
   t = int(packet[3:6], base=2)
   packet = packet[6:]

   match t:
      case 4:
         last = False
         val = ""

         while not last:
            sub_packet = packet[:5]
            packet = packet[5:]

            val += sub_packet[1:]

            if sub_packet[0] == "0":
               last = True

         return  int(val, base=2), packet

      case _:
         i = int(packet[:1])
         packet = packet[1:]
         operands = []
         val = 0

         match i:
            case 0:
               length = int(packet[:15], base=2)
               packet = packet[15:]

               sub_packet = packet[:length]
               packet = packet[length:]
            
               while len(sub_packet):
                  val, sub_packet = parse_packet(sub_packet)
                  operands.append(val)
               
            case 1:
               length = int(packet[:11], base=2)
               packet = packet[11:]

               for _ in range(length):
                  val, packet = parse_packet(packet)
                  operands.append(val)

         match t:
            case 0:
               val = sum(operands)

            case 1:
               val = reduce(lambda x, y: x * y, operands)

            case 2:
               val = reduce(lambda x, y: min(x, y), operands)

            case 3:
               val = reduce(lambda x, y: max(x, y), operands)

            case 5:
               val = int(operands[0] > operands[1])

            case 6:
               val = int(operands[0] < operands[1])

            case 7:
               val = int(operands[0] == operands[1])

         return val, packet


if __name__ == "__main__":
   main(sys.argv) 
