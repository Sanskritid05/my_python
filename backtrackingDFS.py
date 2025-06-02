matrix = [
    [1, 2],
    [3, 4]
]

def dfs(i, j, matrix, visited):
    rows = len(matrix)
    cols = len(matrix[0])

    # Fix boundary condition:
    if i < 0 or i >= rows or j < 0 or j >= cols or visited[i][j]:
        return

    visited[i][j] = True
    print(f"Visited Cell: ({i}, {j}) with value {matrix[i][j]}")

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right

    for dr, dc in directions:
        dfs(i + dr, j + dc, matrix, visited)

visited = [[False for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
dfs(0, 0, matrix, visited)
