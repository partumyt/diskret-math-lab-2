"""
Lab 2 template
"""


def adjacency_matrix_transformer(lst: list[list]) -> dict[int, list[int]]:
    """
    Transforms matrix to dict
    >>> adjacency_matrix_transformer([[0, 1, 1], [1, 0, 1], [1, 1, 0]])
    {0: [1, 2], 1: [0, 2], 2: [0, 1]}
    """
    adjacency = {}
    mid = []
    q = 0
    for i, k in enumerate(lst):
        for e, _ in enumerate(k):
            if k[e] == 1:
                if adjacency.get(i):
                    mid = adjacency.get(i)
                    adjacency.pop(i)

                mid.append(e)
                adjacency.setdefault(i, mid)
                mid = []
                q += 1
        if q == 0:
            adjacency.setdefault(i, mid)
        q = 0

    return adjacency


def read_incidence_matrix(filename: str) -> list[list]:
    """
    :param str filename: path to file
    :returns list[list]: the incidence matrix of a given graph
    """
    edge = []
    mid = []
    final = []
    skip = 0
    q = 0
    with open(filename, "r", encoding="utf") as file:
        while True:
            edgecontent = file.readline().replace("\n", "")
            if skip == 0:
                skip += 1
                continue
            if edgecontent == "}":
                break
            mid = edgecontent.split()
            edge.append((int(mid[0]), int(mid[-1][0])))
    mid = []
    for i in edge:
        for e in i:
            if q < e:
                q = e
    for _ in range(len(edge)):
        mid.append(0)
    for _ in range(q + 1):
        final.append(mid.copy())
    for i, e in enumerate(edge):
        for k in e:
            final[k][i] = 1
    return final


def read_adjacency_matrix(filename: str) -> list[list]:
    """
    :param str filename: path to file
    :returns list[list]: the adjacency matrix of a given graph
    """
    edge = []
    mid = []
    final = []
    skip = 0
    q = 0
    with open(filename, "r", encoding="utf") as file:
        while True:
            edgecontent = file.readline().replace("\n", "")
            if skip == 0:
                skip += 1
                continue
            if edgecontent == "}":
                break
            mid = edgecontent.split()
            edge.append((int(mid[0]), int(mid[-1][0])))
    mid = []
    for i in edge:
        for e in i:
            if q < e:
                q = e
    for _ in range(q + 1):
        mid.append(0)
    for _ in range(q + 1):
        final.append(mid.copy())
    for i in edge:
        final[i[0]][i[1]] = 1
    return final


def read_adjacency_dict(filename: str) -> dict[int, list[int]]:
    """
    :param str filename: path to file
    :returns dict: the adjacency dict of a given graph
    """
    edge = []
    mid = []
    final = {}
    skip = 0
    with open(filename, "r", encoding="utf") as file:
        while True:
            edgecontent = file.readline().replace("\n", "")
            if skip == 0:
                skip += 1
                continue
            if edgecontent == "}":
                break
            mid = edgecontent.split()
            edge.append((mid[0], mid[-1][0]))
    mid = []
    for i in edge:
        if final.get(int(i[0])):
            mid = final.get(int(i[0]))
            final.pop(int(i[0]))
        mid.append(int(i[1]))
        final.setdefault(int(i[0]), mid)
        mid = []
    return final


def iterative_adjacency_dict_dfs(graph: dict[int, list[int]], start: int) -> list[int]:
    """
    :param list[list] graph: the adjacency list of a given graph
    :param int start: start vertex of search
    :returns list[int]: the dfs traversal of the graph
    >>> iterative_adjacency_dict_dfs({0: [1, 2], 1: [0, 2], 2: [0, 1]}, 0)
    [0, 1, 2]
    >>> iterative_adjacency_dict_dfs({0: [1, 2], 1: [0, 2, 3], 2: [0, 1], 3: []}, 0)
    [0, 1, 2, 3]
    """
    pass


def iterative_adjacency_matrix_dfs(graph: list[list], start: int) -> list[int]:
    """
    :param dict graph: the adjacency matrix of a given graph
    :param int start: start vertex of search
    :returns list[int]: the dfs traversal of the graph
    >>> iterative_adjacency_matrix_dfs([[0, 1, 1], [1, 0, 1], [1, 1, 0]], 0)
    [0, 1, 2]
    >>> iterative_adjacency_matrix_dfs([[0, 1, 1, 0], [1, 0, 1, 1], [1, 1, 0, 0], [0, 0, 0, 0]], 0)
    [0, 1, 2, 3]
    """
    pass


def recursive_adjacency_dict_dfs(
    graph: dict[int, list[int]], start: int, visited: set | None = None
) -> list[int]:
    """
    :param list[list] graph: the adjacency list of a given graph
    :param int start: start vertex of search
    :returns list[int]: the dfs traversal of the graph
    >>> recursive_adjacency_dict_dfs({0: [1, 2], 1: [0, 2], 2: [0, 1]}, 0)
    [0, 1, 2]
    >>> recursive_adjacency_dict_dfs({0: [1, 2], 1: [0, 2, 3], 2: [0, 1], 3: []}, 0)
    [0, 1, 2, 3]
    """
    if visited is None:
        visited = []
    if start not in visited:
        visited.append(start)
        for next_el in graph.get(start):
            recursive_adjacency_dict_dfs(graph, next_el, visited)

    return visited


def recursive_adjacency_matrix_dfs(
    graph: list[list[int]], start: int, visited: set | None = None
) -> list[int]:
    """
    :param dict graph: the adjacency matrix of a given graph
    :param int start: start vertex of search
    :returns list[int]: the dfs traversal of the graph
    >>> recursive_adjacency_matrix_dfs([[0, 1, 1], [1, 0, 1], [1, 1, 0]], 0)
    [0, 1, 2]
    >>> recursive_adjacency_matrix_dfs([[0, 1, 1, 0], [1, 0, 1, 1], [1, 1, 0, 0], [0, 0, 0, 0]], 0)
    [0, 1, 2, 3]
    """
    newgraph = adjacency_matrix_transformer(graph)
    return recursive_adjacency_dict_dfs(newgraph, start, visited)


def iterative_adjacency_dict_bfs(graph: dict[int, list[int]], start: int) -> list[int]:
    """
    :param list[list] graph: the adjacency list of a given graph
    :param int start: start vertex of search
    :returns list[int]: the bfs traversal of the graph
    >>> iterative_adjacency_dict_bfs({0: [1, 2], 1: [0, 2], 2: [0, 1]}, 0)
    [0, 1, 2]
    >>> iterative_adjacency_dict_bfs({0: [1, 2], 1: [0, 2, 3], 2: [0, 1], 3: []}, 0)
    [0, 1, 2, 3]
    """
    pass


def iterative_adjacency_matrix_bfs(graph: list[list[int]], start: int) -> list[int]:
    """
    :param dict graph: the adjacency matrix of a given graph
    :param int start: start vertex of search
    :returns list[int]: the bfs traversal of the graph
    >>> iterative_adjacency_matrix_bfs([[0, 1, 1], [1, 0, 1], [1, 1, 0]], 0)
    [0, 1, 2]
    >>> iterative_adjacency_matrix_bfs([[0, 1, 1, 0], [1, 0, 1, 1], [1, 1, 0, 0], [0, 0, 0, 0]], 0)
    [0, 1, 2, 3]
    """
    pass


def recursive_adjacency_dict_bfs(graph: dict[int, list[int]], start: int) -> list[int]:
    """
    :param list[list] graph: the adjacency list of a given graph
    :param int start: start vertex of search
    :returns list[int]: the bfs traversal of the graph
    >>> recursive_adjacency_dict_bfs({0: [1, 2], 1: [0, 2], 2: [0, 1]}, 0)
    [0, 1, 2]
    >>> recursive_adjacency_dict_bfs({0: [1, 2], 1: [0, 2, 3], 2: [0, 1], 3: []}, 0)
    [0, 1, 2, 3]
    """
    pass


def recursive_adjacency_matrix_bfs(graph: list[list[int]], start: int) -> list[int]:
    """
    :param dict graph: the adjacency matrix of a given graph
    :param int start: start vertex of search
    :returns list[int]: the bfs traversal of the graph
    >>> recursive_adjacency_matrix_bfs([[0, 1, 1], [1, 0, 1], [1, 1, 0]], 0)
    [0, 1, 2]
    >>> recursive_adjacency_matrix_bfs([[0, 1, 1, 0], [1, 0, 1, 1], [1, 1, 0, 0], [0, 0, 0, 0]], 0)
    [0, 1, 2, 3]
    """
    pass


def adjacency_matrix_radius(graph: list[list]) -> int:
    """
    :param list[list] graph: the adjacency matrix of a given graph
    :returns int: the radius of the graph
    >>> adjacency_matrix_radius([[0, 1, 1], [1, 0, 1], [1, 1, 0]])
    1
    >>> adjacency_matrix_radius([[0, 1, 1], [1, 0, 1], [1, 1, 0], [0, 1, 0]])
    2
    """
    pass


def adjacency_dict_radius(graph: dict[int : list[int]]) -> int:
    """
    :param dict graph: the adjacency list of a given graph
    :returns int: the radius of the graph
    >>> adjacency_dict_radius({0: [1, 2], 1: [0, 2], 2: [0, 1]})
    1
    >>> adjacency_dict_radius({0: [1, 2], 1: [0, 2], 2: [0, 1], 3: [1]})
    2
    """
    pass


# if __name__ == "__main__":
#     import doctest
#     doctest.testmod()
