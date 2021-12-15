import sys
from enum import Enum, auto

class Node:
   class types(Enum):
      start = auto()
      small = auto()
      big = auto()

   def __init__(self, name, adjacent_nodes = []):
      self.adjacent_nodes = set(adjacent_nodes)
      self.name = name
      self.type = Node.getType(name)

   def add_adjacent_node(self, node):
      self.adjacent_nodes.add(node)

   def get_adjacent_nodes(self) -> list[str]:
      return list(self.adjacent_nodes)

   @staticmethod
   def getType(name):
      if name == "start":
         return Node.types.start

      if 'a' <= name[0] <= 'z':
         return Node.types.small
      
      if 'A' <= name[0] <= 'Z':
         return Node.types.big
      

      return None

def path_to_end(name: str, visited: list[str], twice: bool):
   global nodes

   node = nodes.get(name)

   if (node is None) or (node.type == Node.types.start and name in visited):
      return 0

   if (node.type == Node.types.small and name in visited):
      if not twice:
         twice = True
      else:
         return 0

   visited = visited + [name]
   
   num_paths = 0

   for child in node.get_adjacent_nodes():
      if child == "end":
         num_paths += 1
         continue

      num_paths += path_to_end(child, visited, twice)


   return num_paths

def main(args):
   with open("test_input3.txt" if len(args) > 1 and args[1] == "-t" else "input.txt") as f:
      global nodes
      nodes = dict()

      lines = [x.strip('\n').split('-') for x in f.readlines()]

      for a, b in lines:
         node_a = nodes.get(a)
         node_b = nodes.get(b)

         if node_a is None:
            node_a = Node(a, [b])
            nodes[a] = node_a
         else:
            node_a.add_adjacent_node(b)

         if node_b is None:
            node_b = Node(b, [a])
            nodes[b] = node_b
         else: 
            node_b.add_adjacent_node(a)

      print(path_to_end("start", [], False))

if __name__ == "__main__":
   main(sys.argv) 
