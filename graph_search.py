from collections import deque

# Replace this with your own graph (adjacency list)
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E'],
}


def build_path(parent, target):
    path = []
    while target is not None:
        path.append(target)
        target = parent[target]
    return path[::-1]


def bfs(graph, start, target):
    print(f"\n=== BFS: {start} -> {target} ===")
    visited = {start}
    parent = {start: None}
    queue = deque([start])
    steps = checks = 0

    while queue:
        node = queue.popleft()
        steps += 1
        print(f"Step {steps}: visiting {node} | queue: {list(queue)}")

        checks += 1  # compare node with target
        if node == target:
            path = build_path(parent, node)
            print(f"FOUND {target}! Path: {' -> '.join(path)}")
            print(f"Steps: {steps}, Checks: {checks}")
            return path, steps, checks

        for nb in graph.get(node, []):
            checks += 1  # visited check
            if nb not in visited:
                visited.add(nb)
                parent[nb] = node
                queue.append(nb)
                print(f"   discovered {nb}")

    print(f"{target} NOT found. Steps: {steps}, Checks: {checks}")
    return None, steps, checks


def dfs(graph, start, target):
    print(f"\n=== DFS: {start} -> {target} ===")
    visited = set()
    parent = {start: None}
    stack = [start]
    steps = checks = 0

    while stack:
        node = stack.pop()
        checks += 1  # visited check on pop
        if node in visited:
            continue
        visited.add(node)
        steps += 1
        print(f"Step {steps}: visiting {node} | stack: {stack}")

        checks += 1  # compare node with target
        if node == target:
            path = build_path(parent, node)
            print(f"FOUND {target}! Path: {' -> '.join(path)}")
            print(f"Steps: {steps}, Checks: {checks}")
            return path, steps, checks

        for nb in reversed(graph.get(node, [])):
            checks += 1  # visited check
            if nb not in visited:
                parent[nb] = node
                stack.append(nb)
                print(f"   pushed {nb}")

    print(f"{target} NOT found. Steps: {steps}, Checks: {checks}")
    return None, steps, checks


if __name__ == "__main__":
    start = input("Start node: ").strip()
    target = input("Target node: ").strip()

    if start not in graph or target not in graph:
        print("Start or target node is not in the graph.")
    else:
        bfs(graph, start, target)
        dfs(graph, start, target)
