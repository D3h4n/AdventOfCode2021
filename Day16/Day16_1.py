from functools import reduce, total_ordering
import sys
from types import prepare_class

def main(args):
   global total

   with open("test_input.txt" if len(args) > 1 and args[1] == "-t" else "input.txt") as f:
      # conversion table
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
      
      transmission = f.readline().strip("\n")

      # convert table from hex to binary
      decoded = ""
      for x in transmission:
         decoded += hex_to_bin[x]

      # parse packet and print total
      total = 0
      parse_packet(decoded)
      print("\nTotal:", total)

def parse_packet(packet):
   global total

   # parse version and type id
   v = int(packet[:3], base=2)
   t = int(packet[3:6], base=2)
   packet = packet[6:]

   # update total
   total += v

   # check if literal
   if t == 4:
      last = False
      val = ""

      # loop through each packet
      while not last:
         sub_packet = packet[:5]
         packet = packet[5:]

         val += sub_packet[1:]

         if sub_packet[0] == "0":
            last = True

      # display packet value
      print("\nLiteral:", "\nVersion:", v, "Type ID:", t, "\nValue:", int(val, base=2))
   else:
      # get length type id
      i = int(packet[:1])
      packet = packet[1:]

      # parse based on length type
      match i:
         case 0:
            # get number of bits
            length = int(packet[:15], base=2)
            packet = packet[15:]

            # print operator type and info
            print("\nOperator:", "\nVersion:", v, "Type ID:", t, "\nLength type:", i, "Length:", length)

            # get sub packet
            sub_packet = packet[:length]
            packet = packet[length:]

            # parse subpacket
            while len(sub_packet):
               sub_packet = parse_packet(sub_packet)
            
         case 1:
            # parse number of subpackets
            num = int(packet[:11], base=2)
            packet = packet[11:]

            # print operator and info
            print("\nOperator:", "\nVersion:", v, "Type ID:", t, "\nLength type:", i, "Number:", num)

            # parse num packets
            for _ in range(num):
               packet = parse_packet(packet)

   # return remaining data
   return packet


if __name__ == "__main__":
   main(sys.argv) 
