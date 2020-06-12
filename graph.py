class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)


class Stack():
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None

    def size(self):
        return len(self.stack)


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}
        self.toExplore = set(self.vertices.keys())

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("Vertex does not exist")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Create an empty queue and enqueue with the starting vertex ID
        q = Queue()
        q.enqueue(starting_vertex)

        # Keep track of visited vertices
        visited = set()

        # While the queue is not empty
        while q.size() > 0:
            # Pop the front of the queue
            v = q.dequeue()

            if v not in visited:
                #     self.toExplore.remove(v)

                # Visit
                print(v)

                # Mark it as visited
                visited.add(v)

                # Add all of its neighbors to the back of the queue
                for next_vert in self.get_neighbors(v):
                    q.enqueue(next_vert)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """

        # Begin stack with starting vertex
        s = Stack()
        s.push(starting_vertex)

        # Track visited
        visited = set()

        # While stack is not empty
        while s.size() > 0:
            # Pop the top
            v = s.pop()

            if v not in visited:
                print(v)

                visited.add(v)

                for next_vert in self.get_neighbors(v):
                    s.push(next_vert)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        if visited == None:
            visited = set()

        if starting_vertex not in visited:
            print(starting_vertex)
            visited.add(starting_vertex)

            for next_node in self.get_neighbors(starting_vertex):
                self.dft_recursive(next_node, visited)

    def bfs_order(self, starting_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breadth-first order.
        """

        # Keep track of visited vertices
        visited = []

        # Create an empty queue and enqueue with the starting vertex ID
        q = Queue()
        q.enqueue([starting_vertex])

        # While the queue is not empty
        while q.size() > 0:
            # Pop the front of the queue
            path = q.dequeue()
            currentNode = path[-1]

            if currentNode not in visited:

                visited.append(currentNode)
                # self.toExplore.remove(currentNode)

                if len(visited) == 500:
                    return visited

                # Add all of its neighbors to the back of the queue
                for next_vert in self.get_neighbors(currentNode):
                    pathCopy = list(path)
                    pathCopy.append(next_vert)
                    q.enqueue(pathCopy)
        return None

    def bfs_path(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breadth-first order.
        """

        # Keep track of visited vertices
        visited = []

        # Create an empty queue and enqueue with the starting vertex ID
        q = Queue()
        q.enqueue([starting_vertex])

        # While the queue is not empty
        while q.size() > 0:
            # Pop the front of the queue
            path = q.dequeue()
            currentNode = path[-1]

            if currentNode not in visited:

                visited.append(currentNode)
                # self.toExplore.remove(currentNode)

                if currentNode == destination_vertex:
                    return path

                # Add all of its neighbors to the back of the queue
                for next_vert in self.get_neighbors(currentNode):
                    pathCopy = list(path)
                    pathCopy.append(next_vert)
                    q.enqueue(pathCopy)
        return None

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Keep track of visited vertices
        visited = set()

        # Create an empty queue and enqueue with the starting vertex ID
        s = Stack()
        s.push([starting_vertex])

        # While the queue is not empty
        while s.size() > 0:
            # Pop the front of the queue
            path = s.pop()
            currentNode = path[-1]

            if currentNode not in visited:

                visited.add(currentNode)
                if currentNode == destination_vertex:
                    return path

                # Add all of its neighbors to the back of the queue
                for next_vert in self.get_neighbors(currentNode):
                    pathCopy = list(path)
                    pathCopy.append(next_vert)
                    s.push(pathCopy)
        return None

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=[]):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if starting_vertex == destination_vertex:
            print('Prints:', path)
            return path

        if visited == None:
            visited = set()

        if path == []:
            path.append(starting_vertex)

        if starting_vertex not in visited:
            visited.add(starting_vertex)

            for next_node in self.get_neighbors(starting_vertex):
                pathCopy = list(path)
                pathCopy.append(next_node)

            return self.dfs_recursive(
                next_node, destination_vertex, visited, pathCopy)


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)

    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print("BFS")
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''

    print("DFS")
    print(graph.dfs(1, 6))
    print('Recursive DFS')
    print('Returns:', graph.dfs_recursive(1, 6))
