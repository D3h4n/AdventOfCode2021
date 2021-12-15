import sys
from enum import Enum, auto

class Chars(Enum):
   PARENTHESIS = 1
   SQUARE_BRACKET = 2
   CURLY_BRACKET = 3
   GREATER_THAN = 4

   @staticmethod
   def toSymbol(num):
      if num == Chars.PARENTHESIS:
         return ')'
      elif num == Chars.SQUARE_BRACKET:
         return ']'
      elif num == Chars.CURLY_BRACKET:
         return '}'
      elif num == Chars.GREATER_THAN:
         return '>'
      else:
         return '\0'

def parseLine(line):
   stack = []

   for c in line:
      if c == '(':
         stack.append(Chars.PARENTHESIS)
      elif c == '[':
         stack.append(Chars.SQUARE_BRACKET)
      elif c == '{':
         stack.append(Chars.CURLY_BRACKET)
      elif c == '<':
         stack.append(Chars.GREATER_THAN)
      else:
         if c != Chars.toSymbol(stack.pop(-1)):
            return []
   
   return stack

def main(args):
   with open("test_input.txt" if len(args) > 1 and args[1] == "-t" else "input.txt") as f:
      scores = []
      
      for x in f.readlines():
         total = 0
         x = x.strip('\n')
         remaining = parseLine(x)
         
         for x in range(len(remaining) - 1, -1, -1):
            total *= 5
            total += remaining[x].value
            
         if total > 0:
            scores.append(total)

      scores.sort()
      print(scores[len(scores) // 2])

if __name__ == "__main__":
   main(sys.argv) 
