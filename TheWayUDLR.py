n = int(input("Input size of map : "))
move = map(str, input("Input where to go : ").split())
way = ['L', 'R', 'U', 'D']
x = 1
y = 1
# x,y좌표 처음 시작점.

for i in move:
    if i == 'L' and y-1 > 0:
        y -= 1
    elif i == 'R' and y+1 <= n:
        y += 1
    elif i == 'U' and x-1 > 0:
        x -= 1
    elif i == 'D' and x+1 <= n:
        x += 1
    else:
        pass
print("The location is ({}, {})".format(x, y))

# Page 110 - 112


