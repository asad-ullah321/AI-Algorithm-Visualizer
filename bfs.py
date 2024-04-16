class BFS:
    def __init__(self, graph, graphType):
        self.graph = graph
        self.graphType = graphType

    def bfsTraversal(self, bfsPath):
        for i in bfsPath:
            print(i, end=" ")
        print()

    def bfsSearch(self, s, g):
        visited = []
        queue = []
        path = []
        queue.append(s)
        visited.append(s)

        while queue:
            current = queue.pop(0)


            if current[0] in g:
                current.reverse()
                return current

            neighbors = self.graph[current[0]]
            neighborsInOrder = sorted(neighbors)  #visits in the order they were expanded

            for neighbor in neighborsInOrder:
                if neighbor not in visited:
                    visited.append(neighbor)
                    tempPath = [neighbor]
                    for parents in current:
                        tempPath.append(parents)
                    queue.append(tempPath)
        return []

    def bfs(self, s, g):
        return self.bfsSearch(s, g)