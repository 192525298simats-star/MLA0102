import heapq

graph = {
    'A': [('B', 4), ('C', 2)],
    'B': [('D', 5), ('E', 1)],
    'C': [('F', 3)],
    'D': [],
    'E': [],
    'F': []
}

heuristic = {
    'A': 6,
    'B': 4,
    'C': 2,
    'D': 3,
    'E': 1,
    'F': 0
}

def best_first_search(start, goal):
    pq = []
    visited = []

    heapq.heappush(pq, (heuristic[start], start))

    while pq:
        h, node = heapq.heappop(pq)

        if node not in visited:
            print(node, end=" ")
            visited.append(node)

            if node == goal:
                print("\nGoal Found")
                return

            for neighbor, cost in graph[node]:
                heapq.heappush(pq, (heuristic[neighbor], neighbor))

best_first_search('A', 'F')
