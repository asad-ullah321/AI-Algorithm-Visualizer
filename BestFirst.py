import networkx as nx
DG = nx.DiGraph()
G = nx.Graph()
Goal_list = []

class BestFS:
    def __init__(self, graph, graphType, H_dict):
        self.graph = graph
        self.graphType = graphType
        self.HeuristicDict = H_dict

    def BestFSTraversal(self, bfsPath):
        for i in range(len(bfsPath)-1):
            print(bfsPath[i], end=" ")
        print()

    def BestFSSearch(self, s, g):
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
                    tempPath = [self.HeuristicDict[neighbor], neighbor]
                    for parents in current[1:]:
                        tempPath.append(parents)
                    queue.append(tempPath)
        return []

    def bestFS(self, s, g):
        return self.BestFSSearch(s, g)




G.add_edge( 'A', 'B', weight=2)
G.add_edge('B', 'C', weight=1)
G.add_edge('C', 'D', weight=1)
G.add_edge('A', 'E', weight=1)
G.add_edge('E', 'D', weight=2)
G.add_edge('A', 'F', weight=1)

H = {'A': 2, 'B': 1, 'C': 1, 'D': 2, 'E': 3, 'F': 1}

D = BestFS(G, "nothing", H)
D.BestFSTraversal(D.bestFS('A', 'D'))