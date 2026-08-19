import heapq

def greedy_best_first_search(graph, heuristic, start, goal):
    # Priority queue: (heuristic value, node)
    open_list = []
    heapq.heappush(open_list, (heuristic[start], start))

    visited = set()
    parent = {start: None}

    while open_list:
        h, current = heapq.heappop(open_list)

        if current in visited:
            continue

        visited.add(current)

        if current == goal:
            # Reconstruct path
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]
            return path[::-1]

        for neighbor in graph[current]:
            if neighbor not in visited:
                parent[neighbor] = current
                heapq.heappush(open_list, (heuristic[neighbor], neighbor))

    return None


# Example graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': ['H'],
    'F': [],
    'G': [],
    'H': []
}

# Heuristic values (estimated distance to goal H)
heuristic = {
    'A': 7,
    'B': 6,
    'C': 5,
    'D': 4,
    'E': 2,
    'F': 3,
    'G': 6,
    'H': 0
}

start = 'A'
goal = 'H'

path = greedy_best_first_search(graph, heuristic, start, goal)

if path:
    print("Path found:", " -> ".join(path))
else:
    print("No path found")
