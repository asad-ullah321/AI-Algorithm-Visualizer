import networkx as nx
DG = nx.DiGraph()
G = nx.Graph()
Goal_list = []
class BIDS:
    def __init__(self, graph, graphType):
        self.graph = graph
        self.graphType = graphType

    def bidsTraversal(self, bfsPath):
        for i in bfsPath:
            print(i, end=" ")
        print()

    def bidsSearch(self, s, g):
        visitedS = [s]
        queueS = [[s]]
        visitedG = [g[0]]
        queueG = [[g[0]]]
        path = []

        while queueS and queueG:
            currentS = queueS.pop(0)
            currentG = queueG[0]


            neighbors = self.graph[currentS[0]]
            neighborsInOrder = sorted(neighbors)  #visits in the order they were expanded

            for neighbor in neighborsInOrder:
                if neighbor not in visitedS:
                    visitedS.append(neighbor)
                    tempPath = [neighbor]
                    for parents in currentS:
                        tempPath.append(parents)

                    if neighbor in visitedG:
                        print("merge point: ", neighbor)
                        for j in queueG:
                            if j[0][0] == neighbor:
                                tempPath.reverse()
                                for k in j[1:]:
                                    tempPath.append(k)
                                return tempPath

                    queueS.append(tempPath)

            neighbors = self.graph[currentG[0]]
            neighborsInOrder = sorted(neighbors)  # visits in the order they were expanded
            for neighbor in neighborsInOrder:
                if neighbor not in visitedG:
                    visitedG.append(neighbor)
                    tempPath = [neighbor]
                    for parents in currentG:
                        tempPath.append(parents)
                    queueG.append(tempPath)
            queueG.pop(0)

        return []

    def bids(self, s, g):
        return self.bidsSearch(s, g)


G.add_edge('A', 'B', weight=1)
G.add_edge('B', 'C', weight=1)
G.add_edge('C', 'D', weight=1)
G.add_edge('A', 'E', weight=1)
G.add_edge('E', 'D', weight=1)
G.add_edge('A', 'F', weight=1)

D = BIDS(G, "nothing")
print(D.bids('A', 'D'))