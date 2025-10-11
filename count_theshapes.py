from collections import defaultdict

def count_closed_shapes(segments):
    graph = defaultdict(list)
    edges = set()

    # Build graph
    for x1, y1, x2, y2 in segments:
        p1, p2 = (x1, y1), (x2, y2)
        graph[p1].append(p2)
        graph[p2].append(p1)
        edges.add(frozenset([p1, p2]))

    visited_edges = set()
    cycles = set()

    def dfs(current, start, path, visited):
        for neighbor in graph[current]:
            edge = frozenset([current, neighbor])
            if edge in visited:
                continue
            visited.add(edge)
            path.append(neighbor)
            if neighbor == start and len(path) > 3:
                cycles.add(tuple(sorted(path)))
            elif neighbor != start:
                dfs(neighbor, start, path[:], visited.copy())

    for p in graph:
        dfs(p, p, [p], set())

    return len(cycles)

# Input parsing
n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]
print(count_closed_shapes(segments))
