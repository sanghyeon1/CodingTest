n, m = map(int, input("Input the size of map : ").split())
a, b, d = map(int, input("Input coordinates of character and direction : ").split())
map_type = []
v = [[0] * m for _ in range(n)]  # 방문처리 변수

for i in range(n):
    map_type.append(list(map(int, input("Input type of map : ").split())))

v[a][b] = 1  # 처음위치 방문처리

da = [-1, 0, 1, 0]
db = [0, 1, 0, -1]


def turn_left():
    global d
    d -= 1
    if d == -1:
        d = 3


count = 1
turn_time = 0
while True:
    turn_left()
    na = a + da[d]
    nb = b + db[d]

    if v[na][nb] == 0 and map_type[na][nb] == 0:
        v[na][nb] = 1
        a = na
        b = nb
        count += 1
        turn_time = 0
    else:
        turn_time += 1

    if turn_time == 4:
        na = a - da[d]
        nb = b - db[d]
        if map_type[na][nb] == 0:
            a = na
            b = nb
        else:
            break
        turn_time = 0

print(count)

# Page 118 - 121
