def addEdge(node1, node2, cost, graph):
    if node1 not in graph:
        graph[node1] = []
    if node2 not in graph:
        graph[node2] = []
    graph[node1].append((node2, cost))
    graph[node2].append((node1, cost))

with open(file="graph.txt", mode="r") as file:
    data = file.readlines()
    vertices, edges = data[0].split()

my_graph = {}
for i in range(1, len(data)):
    node1, node2, cost = data[i].split()
    addEdge(node1,node2,int(cost),my_graph)

print(f"Elements of my graph: {my_graph}")

print(f"Vertices: {list(my_graph.keys())}")

print("Edges:")
for key, val in my_graph.items():
    print(f"{key}-->{val}")

