# Dijkstra algorithm
from collections import deque
INF = float("inf")
# Describe the graph
graph = {}
#graph['first'] = {'A': 6, 'B': 2}
#graph['A'] = {'end': 1}
#graph['B'] = {'A': 3, 'end': 5}
#graph['end'] = {}

graph['first'] = {'A': 5, 'B': 2}
graph['A'] = {'C': 4, 'D': 2}
graph['B'] = {'A': 8, 'D': 7}
graph['C'] = {'end': 3, 'D': 6}
graph['D'] = {'end': 1}
graph['end'] = {}  # Ans: 8

#graph['first'] = {'A': 10}
#graph['A'] = {'B': 20}
#graph['B'] = {'C': 1, 'end': 30}
#graph['C'] = {'A': 1}
#graph['end'] = {} # Ans: 60

#graph['first'] = {'A': 2, 'B': 2}
#graph['A'] = {'end': 2, 'C': 2}
#graph['B'] = {'A': 2}
#graph['C'] = {'end': 2, 'B': -1}
#graph['end'] = {} # Ans: 4?
# Dict for the parents of the nodes
parents = {}

# Dict for the shortest path to each node
paths = {}

def find_node_with_shortest_path(paths, completed):
    min_key, min_value = None, INF
    for key, value in paths.items():
        if value <= min_value and not key in completed:
            min_key, min_value = key, value
    return min_key


def dijkstra(graph, parents, paths, head):
    node = head
    # Shows the nodes that are already processed
    completed = []
    while node:
        neighbors = graph[node]
        for key, value in neighbors.items():
            # Calculate new path to the neighboring node
            new_path = paths.get(node, 0) + value
            # If path to this neighboring node isn't in 'paths', then it is set to infinity
            if new_path < paths.get(key, INF):
                # New path is set only if it is shorter then the previous one
                paths[key] = new_path
                parents[key] = node
        completed.append(node)
        #print(f'Paths {paths}')
        node = find_node_with_shortest_path(paths, completed)
    return paths, parents

dejikstra(graph, parents, paths, 'first')