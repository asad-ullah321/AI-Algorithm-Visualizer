import networkx as nx
DG = nx.DiGraph()
G = nx.Graph()
Goal_list = []

class UCS:
    def __init__(self, graph, graphType):
        self.graph = graph
        self.graphType = graphType

    def ucsTraversal(self, bfsPath):
        for i in range(len(bfsPath)-1):
            print(bfsPath[i], end=" ")
        print()
        print("Path Cost: ", bfsPath[-1])

    def ucsSearch(self, s, g):
        visited = []
        queue = []
        path = []
        queue.append([0, s])
        visited.append(s)

        while queue:
            queue.sort(key=lambda x: x[0])
            current = queue.pop(0)


            if current[1] in g:
                current.reverse()
                return current

            neighbors = self.graph[current[1]]
            neighborsInOrder = sorted(neighbors)  #visits in the order they were expanded

            for neighbor in neighborsInOrder:
                if neighbor not in visited:
                    visited.append(neighbor)
                    tempPath = [current[0]+int(neighbors[neighbor]['weight']), neighbor]
                    for parents in current[1:]:
                        tempPath.append(parents)
                    queue.append(tempPath)
        return []

    def ucs(self, s, g):
        return self.ucsSearch(s, g)




# G.add_edge( 'A', 'B', weight=2)
# G.add_edge('B', 'C', weight=1)
# G.add_edge('C', 'D', weight=1)
# G.add_edge('A', 'E', weight=1)
# G.add_edge('E', 'D', weight=2)
# G.add_edge('A', 'F', weight=1)
#
#
#
# D = UCS(G, "nothing")
# D.ucsTraversal(D.ucs('A', 'D'))