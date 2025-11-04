from collections import deque

class Graph:
    def __init__(self, directed=False, weighted=False):
        self.graph = {}
        self.directed = directed
        self.weighted = weighted

    
    def add_vertex(self, vertex):
        if vertex not in self.graph:
            if self.weighted:
                self.graph[vertex] = {}  
            else:
                self.graph[vertex] = []  

    
    def add_edge(self, vertex1, vertex2, weight=None):
        if vertex1 not in self.graph:
            self.add_vertex(vertex1)
        if vertex2 not in self.graph:
            self.add_vertex(vertex2)
        
        if self.weighted:
            self.graph[vertex1][vertex2] = weight  # Add weighted edge
            if not self.directed:
                self.graph[vertex2][vertex1] = weight  # Add reverse edge for undirected
        else:
            self.graph[vertex1].append(vertex2)  # Add unweighted edge
            if not self.directed:
                self.graph[vertex2].append(vertex1)  # Add reverse edge for undirected

   
    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.graph and vertex2 in self.graph[vertex1]:
            if self.weighted:
                del self.graph[vertex1][vertex2]
                if not self.directed:
                    del self.graph[vertex2][vertex1]
            else:
                self.graph[vertex1].remove(vertex2)
                if not self.directed:
                    self.graph[vertex2].remove(vertex1)

    
    def remove_vertex(self, vertex):
        if vertex in self.graph:
            del self.graph[vertex]
            for v in self.graph:
                if vertex in self.graph[v]:
                    if self.weighted:
                        del self.graph[v][vertex]
                    else:
                        self.graph[v].remove(vertex)

   
    def display(self):
        for vertex , edges in self.graph.items():
            if self.weighted:
                print(f"{vertex} -> {edges}")
            else:
                print(f"{vertex} -> {edges}")

    # BFS traversal
    def bfs(self, start):
        visited = set()
        queue = deque([start])
        while queue:
            vertex = queue.popleft()
            if vertex not in visited:
                print(vertex, end=" ")
                visited.add(vertex)
                
                for neighbor in self.graph[vertex]:
                    if neighbor not in visited:
                        queue.append(neighbor)
                


    def dfs(self, start):
        visited = set()
        stack = [start]

        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                print(vertex, end=" ")
                visited.add(vertex)

                for neighbor in reversed(self.graph[vertex]):
                    if neighbor not in visited:
                        stack.append(neighbor)


    # Check if the graph is finite
    def is_finite(self):
        return len(self.graph) < float('inf')

    # Check if the graph is trivial (has only one vertex)
    def is_trivial(self):
        return len(self.graph) == 1

    # Check if the graph is simple (no loops or multiple edges)
    def is_simple(self):
        for vertex in self.graph:
            if self.weighted:
                if vertex in self.graph[vertex]:
                    return False  # Has a loop
            else:
                if vertex in self.graph[vertex]:
                    return False  # Has a loop
                if len(self.graph[vertex]) != len(set(self.graph[vertex])):
                    return False  # Has multiple edges
        return True

    # Check if the graph is a multi-graph (has multiple edges between vertices)
    def is_multi_graph(self):
        for vertex in self.graph:
            if not self.weighted and len(self.graph[vertex]) != len(set(self.graph[vertex])):
                return True
        return False

    # Check if the graph is null (no edges)
    def is_null_graph(self):
        for vertex in self.graph:
            if self.graph[vertex]:
                return False
        return True

    # Check if the graph is complete (every pair of distinct vertices is connected)
    def is_complete(self):
        n = len(self.graph)
        for vertex in self.graph:
            if self.weighted:
                if len(self.graph[vertex]) != n - 1:
                    return False
            else:
                if len(self.graph[vertex]) != n - 1:
                    return False
        return True

    # Check if the graph is regular (all vertices have the same degree)
    def is_regular(self):
        degrees = [len(self.graph[vertex]) for vertex in self.graph]
        return all(deg == degrees[0] for deg in degrees)

    # Check if the graph is connected (all vertices are reachable from any vertex)
    def is_connected(self):
        if not self.graph:
            return False
        start_vertex = next(iter(self.graph))
        visited = set()
        stack = [start_vertex]
        
        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.add(vertex)
                if self.weighted:
                    stack.extend(self.graph[vertex].keys())
                else:
                    stack.extend(self.graph[vertex])
        return len(visited) == len(self.graph)

    # Check if the graph is cyclic (contains at least one cycle)
    def is_cyclic(self):
        visited = set()

        for start in self.graph:
            if start not in visited:
                stack = [(start, None)]  # (current_node, parent)
                while stack:
                    vertex, parent = stack.pop()

                    if vertex in visited:
                        return True  # cycle found

                    visited.add(vertex)

                    for neighbor in self.graph[vertex]:
                        if neighbor != parent:  # avoid going back to parent
                            stack.append((neighbor, vertex))

        return False



    # Check if the graph is acyclic (contains no cycles)
    def is_acyclic(self):
        return not self.is_cyclic()

    # Check if the graph is a directed acyclic graph (DAG)
    def is_dag(self):
        return self.directed and self.is_acyclic()

    # Check if the graph is a subgraph of another graph
    def is_subgraph(self, other_graph):

        for vertex in other_graph.graph:
            if vertex not in self.graph:
                return False
            
            # Check each neighbor of this vertex
            for neighbor in other_graph.graph[vertex]:
                if neighbor not in self.graph[vertex]:
                    return False  # A required edge is missing
        
        # If all vertices and edges exist
        return True



    # Check if the graph is weighted
    def is_weighted(self):
        return self.weighted

    # Check if the graph is directed
    def is_directed(self):
        return self.directed

    # Check if the graph is undirected
    def is_undirected(self):
        return not self.directed

    # Check if the graph is disconnected
    def is_disconnected(self):
        return not self.is_connected()
    



# Create a directed, unweighted graph
g = Graph(directed=True, weighted=True)

# Add vertices
g.add_vertex('A')
g.add_vertex('B')
g.add_vertex('C')
g.add_vertex('D')

# Add edges
g.add_edge('A', 'B', 5)
g.add_edge('B', 'C' , 10)
g.add_edge('C', 'A' , 20)  
g.add_edge('D', 'A',30)


# Display the graph
print("Graph:")
g.display()

# Perform BFS traversal
print("\nBFS Traversal starting from 'A':")
g.bfs('A')

# Perform DFS traversal
print("\nDFS Traversal starting from 'A':")
g.dfs('A')

# Check if the graph is finite
print("\nIs the graph finite?", g.is_finite())

# Check if the graph is trivial

print("Is the graph trivial?", g.is_trivial())
# Check if the graph is simple
print("Is the graph simple?", g.is_simple())

# Check if the graph is a multi-graph
print("Is the graph a multi-graph?", g.is_multi_graph())

# Check if the graph is null
print("Is the graph null?", g.is_null_graph())

# Check if the graph is complete
print("Is the graph complete?", g.is_complete())

# Check if the graph is regular
print("Is the graph regular?", g.is_regular())

# Check if the graph is connected
print("Is the graph connected?", g.is_connected())

# Check if the graph is cyclic
print("Is the graph cyclic?", g.is_cyclic())

# Check if the graph is acyclic
print("Is the graph acyclic?", g.is_acyclic())

# Check if the graph is a DAG
print("Is the graph a DAG?", g.is_dag())

# Check if the graph is weighted
print("Is the graph weighted?", g.is_weighted())

# Check if the graph is directed
print("Is the graph directed?", g.is_directed())

# Check if the graph is undirected
print("Is the graph undirected?", g.is_undirected())

# Check if the graph is disconnected
print("Is the graph disconnected?", g.is_disconnected())

# Create another graph to test subgraph functionality
g2 = Graph(directed=True, weighted=True)
g2.add_vertex('A')
g2.add_vertex('B')
g2.add_edge('A', 'B')

# Check if g2 is a subgraph of g
print("\nIs g2 a subgraph of g?", g.is_subgraph(g2))