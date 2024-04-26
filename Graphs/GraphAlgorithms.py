from collections import deque

def depthFirstSearchAdjacencyList(graph, start, visited=None):
    if visited is None:
        visited = set()
    
    visited.add(start)
    print(start, end=' ')
    
    for neighbor in graph[start]:
        if neighbor not in visited:
            depthFirstSearchAdjacencyList(graph, neighbor, visited)
    
    return visited

def depthFirstSearchAdjacencyMatrix(graph, start, visited=None):
    if visited is None:
        visited = set()
        
    n = len(graph)
    stack = [start]
    
    while stack:
        node = stack.pop()
        if node not in visited:
            print(node)
            visited.add(node)
            for neighbor in range(n):
                if graph[node][neighbor] == 1 and neighbor not in visited:
                    stack.append(neighbor)

def breadthFirstSearchAdjacencyList(graph, start):
    visited = set()
    queue = deque([start])
    
    while queue:
        vertex = queue.popLeft()
        if vertex not in visited:
            print(vertex)
            visited.add(vertex)
            for neighbor in graph.get(vertex, []):
                if neighbor not in visited:
                    queue.append(neighbor)
                    
def breadthFirstSearchAdjacencyMatrix(graph, start):
    numVertices = len(graph)
    visited = set()
    queue = deque([start])
    
    while queue:
        vertex = queue.popLeft()
        if vertex not in visited:
            print(vertex)
            visited.add(vertex)
            for neighbor in range(numVertices):
                if graph[vertex][neighbor] == 1 and neighbor not in visited:
                    queue.append(neighbor)
