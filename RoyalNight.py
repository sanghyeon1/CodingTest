x = [1, 2, 3, 4, 5, 6, 7, 8]  # 행
y = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']  # 열

night = input("Input the start point of Night : ")

steps = [(-1, 2), (-1, -2), (1, 2), (1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]
count = 0
crd = [0, 0]  # 좌표(coordinates)
for i in range(len(y)):
    if night[0] == y[i]:
        crd[0] = i + 1
        crd[1] = int(night[1])
    else:
        pass

for i in range(len(steps)):
    if 0 < steps[i][0] + crd[0] <= 8 and 0 < steps[i][1] + crd[1] <= 8:
        count += 1
    else:
        pass
print(count)

# Page 115 - 117
