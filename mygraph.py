from graphviz import Digraph

class Graph:
   def __init__(self):
       self.graph = {}

   def add_edge(self, u, v):
       if u not in self.graph:
           self.graph[u] = []
       self.graph[u].append(v)

   def to_graphviz(self):
        dot = Digraph()
        for u in self.graph:
            for v in self.graph[u]:
                dot.edge(str(u), str(v))
        return dot   

  #  def print_graph(self):
  #      # {0: [1, 4], 1: [2, 3, 4], 2: [3], 3: [4]}
  #      for node in self.graph:
  #          print(node, "->", " -> ".join(map(str, self.graph[node])))

# Создание экземпляра графа и добавление ребер
g = Graph()

g.add_edge(0, 1)
g.add_edge(0, 4)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 3)
g.add_edge(3, 4)

# g.print_graph()

# Конвертация в объект Graphviz и визуализация
dot = g.to_graphviz()

# Сохранение графа в файл PNG
dot.render(filename='graph', format='png', cleanup=True)

# Команда `render` создаст файл `graph.png` в текущей рабочей директории.