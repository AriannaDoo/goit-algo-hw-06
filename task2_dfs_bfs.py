import networkx as nx
from collections import deque
from task1_graph import build_graph

"""
Пошук шляхів у графі за допомогою DFS та BFS
"""

def dfs(graph: nx.Graph, start: str) -> list:
    """Пошук у глибину (DFS)"""
    visited = []
    stack = [start]

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.append(vertex)
            stack.extend(reversed(list(graph.neighbors(vertex))))

    return visited


def bfs(graph: nx.Graph, start: str) -> list:
    """Пошук у ширину (BFS)"""
    visited = []
    queue = deque([start])

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.append(vertex)
            queue.extend(graph.neighbors(vertex))

    return visited


def main():
    G = build_graph()

    dfs_path = dfs(G, "Groenplaats")
    bfs_path = bfs(G, "Groenplaats")

    print("DFS шлях:")
    print(dfs_path)

    print("\nBFS шлях:")
    print(bfs_path)

    print("""
Висновок :
DFS заглиблюється в одну гілку графа, перш ніж повернутися назад.
BFS обходить граф рівень за рівнем, що краще підходить
для транспортних мереж і пошуку найкоротшких маршрутів.
""")


if __name__ == "__main__":
    main()
