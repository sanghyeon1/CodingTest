n, m = map(int, input("Input the size of Ice frame : ").split())
frame = []
for i in range(n):
    frame.append(list(map(int, input("Input the type of frame : "))))


def dfs(a, b):
    if a < 0 or a >= n or b < 0 or b >= m:
        return False
    if frame[a][b] == 0:  # 방문하지 않은 노드의 경우
        frame[a][b] = 1  # 방문 처리
        dfs(a-1, b)  # 상
        dfs(a+1, b)  # 하
        dfs(a, b-1)  # 좌
        dfs(a, b+1)  # 우 재귀함수 호출
        return True
    return False


result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j):
            result += 1
print(result)

# Page 149 - 151
