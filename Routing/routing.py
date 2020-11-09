import dijkstra
from dijkstra.dijkstra import DijkstraSPF
from dijkstra.graph import Graph


class ApplyDijkstra:

    def __init__(self, new_list, target_list, source, target):
        self.source = source
        self.target = target
        self.new_list = new_list
        self.nodes = list(new_list)
        self.graph = Graph()
        for i in range(len(target_list)):
            self.graph.add_edge(
                target_list[i][0], target_list[i][1], target_list[i][2])

        self.algo_result = DijkstraSPF(self.graph, source)

    def findSmallestPath(self):
        print("->".join(self.algo_result.get_path(self.target)))
        print("Distance :",
              self.algo_result.get_distance(self.target))


# refer the new image added in Maps
source = input("Enter source:")
target = input("Enter source:")
new_list = "ABCD"
target_list = [['A', 'B', 20], ['B', 'A', 16], ['A', 'C', 24], ['C', 'A', 25], [
    'C', 'B', 22], ['B', 'C', 22], ['D', 'C', 22], ['C', 'D', 24], ['D', 'A', 9], ['A', 'D', 7]]
algo = ApplyDijkstra(new_list, target_list, source, target)
algo.findSmallestPath()
