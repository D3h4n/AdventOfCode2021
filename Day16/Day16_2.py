from functools import reduce
import sys

def main(args):
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

      # decode transmission
      decoded = ""
      for x in transmission:
         decoded += hex_to_bin[x]

      # parse packet and calculate value
      val, _ = parse_packet(decoded)

      # print value
      print(val)

def parse_packet(packet):
   # parse type
   t = int(packet[3:6], base=2)
   packet = packet[6:]

   # check if literal value
   if t == 4:
      last = False
      val = ""

      while not last:
         # get sub-packet
         sub_packet = packet[:5]
         packet = packet[5:]

         # append value
         val += sub_packet[1:]

         # check if final sub-packet
         if sub_packet[0] == "0":
            last = True

      # return value and remaining data
      return  int(val, base=2), packet
   else:
      # parse length type id
      i = int(packet[:1])
      packet = packet[1:]

      # parse operands based on length type
      operands = []
      match i:
         case 0:
            # parse length
            length = int(packet[:15], base=2)
            packet = packet[15:]

            # get sub_packets
            sub_packet = packet[:length]
            packet = packet[length:]

            # parse sub-packets for values
            while len(sub_packet):
               val, sub_packet = parse_packet(sub_packet)
               operands.append(val)
            
         case 1:
            # get number of sub-packets
            num = int(packet[:11], base=2)
            packet = packet[11:]

            # parse num sub-packets for values
            for _ in range(num):
               val, packet = parse_packet(packet)
               operands.append(val)

      # perform operation and store result
      val = 0
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

      # return result and remaining data
      return val, packet


if __name__ == "__main__":
   main(sys.argv) 
