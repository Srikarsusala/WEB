from collections import defaultdict, deque

graph = defaultdict(dict)

def add_edge(u, v, weight):
    graph[u][v] = weight
    graph[v][u] = weight
def bfs(start):
    visited = set()
    q = deque()
    bfs_forest = defaultdict(list)
    parent_map = {}

    q.append(start)
    visited.add(start)
    parent_map[start] = ""

    print("Starting with node", start)

    while q:
        node = q.popleft()

        print("\nVisiting node", node)

        for neighbor, weight in graph[node].items():
            if neighbor not in visited:
                visited.add(neighbor)
                q.append(neighbor)
                parent_map[neighbor] = node
                bfs_forest[node].append((neighbor, "solid"))
                print("Adding neighbor", neighbor, "to the queue")
            elif parent_map[node] != neighbor:
                bfs_forest[node].append((neighbor, "dotted"))

        print("BFS traversal: [", end="")
        for current_node, edges in bfs_forest.items():
            for child_node, edge_type in edges:
                print("({}, {}, {})".format(current_node, child_node, edge_type), end=" ")
        print("]")

        print("Queue: [", end="")
        for item in q:
            print(item, end=" ")
        print("]")

    return bfs_forest

# Add all edges
add_edge('A', 'B', 10)
add_edge('A', 'K', 3)
add_edge('B', 'C', 36)
add_edge('C', 'D', 3)
add_edge('D', 'K', 16)
add_edge('D', 'X', 1)
add_edge('F', 'X', 10)
add_edge('E', 'X', 22)
add_edge('E', 'I', 3)
add_edge('E', 'H', 10)
add_edge('I', 'N', 4)
add_edge('I', 'n', 1)
add_edge('n', 'J', 4)
add_edge('K', 'J', 18)
add_edge('n', 'M', 4)
add_edge('N', 'M', 21)
add_edge('N', 'Z', 16)
add_edge('Z', 'Q', 4)
add_edge('Z', 'H', 13)
add_edge('H', 'O', 4)
add_edge('O', 'h', 13)
add_edge('h', 'R', 27)
add_edge('J', 'L', 16)
add_edge('L', 'Y', 3)
add_edge('h', 'P', 17)
add_edge('Y', 'P', 6)
add_edge('Y', 'S', 8)
add_edge('P', 'S', 4)
add_edge('O', 'T', 8)
add_edge('T', 'V', 16)
add_edge('T', 'U', 1)
add_edge('S', 'U', 9)
add_edge('U', 't', 1)
add_edge('t', 'W', 8)
add_edge('t', 'G', 9)

# Perform BFS traversal and obtain BFS forest
bfs_forest = bfs("A")

# Print BFS forest
print("\nBFS FOREST: solid represents tree edges and dotted represents cross edges.")
for node, edges in bfs_forest.items():
    for child, edge_type in edges:
        print(node, "-", child, "(", edge_type, ")")
```
