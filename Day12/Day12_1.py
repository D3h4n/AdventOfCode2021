import sys
from enum import Enum, auto

class Node:
   class types(Enum):
      start = auto()
      end = auto()
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
      if 'a' <= name[0] <= 'z':
         return Node.types.small
      
      if 'A' <= name[0] <= 'Z':
         return Node.types.big
      

      return None

def path_to_end(name: str, visited: list[str]):
   global nodes

   node = nodes.get(name)

   if (node is None) or (name in visited and (node.type == Node.types.small or node.type == Node.types.start)):
      return []

   visited = visited + [name]
   
   paths = []

   for child in node.get_adjacent_nodes():
      if child == "end":
         paths.append([name, child])
         continue

      child_to_end = path_to_end(child, visited)

      for path in child_to_end:
         paths.append([name] + path)

   return paths

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


      paths = path_to_end("start", [])

      print(paths)
      print(len(paths))

if __name__ == "__main__":
   main(sys.argv) 
