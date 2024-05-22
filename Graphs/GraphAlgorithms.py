from collections import deque
import heapq

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
                    
def detectCycle(graph):
    visited = set()
    stack = set()
    
    def dfs(node):
        visited.add(node)
        stack.add(node)
        
        for neighbor in graph.get(node, []):
            if neighbor in stack:
                return True
            if neighbor not in visited:
                if dfs(neighbor):
                    return True
        stack.remove(node)
        return False
    
    for node in graph:
        if node not in visited:
            if dfs(node):
                return True
    return False

def dijkstrasAlgorithm(graph, start):
    distances = {node : float('inf') for node in graph}
    distances[start] = 0
    
    pq = [(0, start)]
    
    while pq:
        current_distance, current_node = heapq.heappop(pq)
        
        if current_distance > distances[current_node]:
            continue
        
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    return distances 

def bellmanFordAlgorithm():
    pass
        
