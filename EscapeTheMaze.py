from collections import deque

n, m = map(int, input("Input the size of maze : ").split())
maze = []
for i in range(n):
    maze.append(list(map(int, input("Input the type of maze : "))))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]  # Up, Down, Left, Right


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]  # 상하좌우로 더한 값
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if maze[nx][ny] == 0:
                continue
            if maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1
                queue.append((nx, ny))
    return maze[n-1][m-1]


print(bfs(0, 0))

# Page 152 - 154
