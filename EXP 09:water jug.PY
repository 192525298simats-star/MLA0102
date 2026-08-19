from collections import deque

def water_jug_bfs(jug1, jug2, target):
    visited = set()
    queue = deque()

    # Initial state: both jugs are empty
    queue.append((0, 0, []))

    while queue:
        x, y, path = queue.popleft()

        if (x, y) in visited:
            continue

        visited.add((x, y))
        path = path + [(x, y)]

        # Check if target is reached
        if x == target or y == target:
            print("Solution Path:")
            for state in path:
                print(state)
            return

        # Possible operations
        next_states = [
            (jug1, y),                         # Fill Jug1
            (x, jug2),                         # Fill Jug2
            (0, y),                            # Empty Jug1
            (x, 0),                            # Empty Jug2
            # Pour Jug1 -> Jug2
            (x - min(x, jug2 - y), y + min(x, jug2 - y)),
            # Pour Jug2 -> Jug1
            (x + min(y, jug1 - x), y - min(y, jug1 - x))
        ]

        for state in next_states:
            if state not in visited:
                queue.append((state[0], state[1], path))

    print("No solution exists.")

# Example
jug1 = 4
jug2 = 3
target = 2

water_jug_bfs(jug1, jug2, target)
