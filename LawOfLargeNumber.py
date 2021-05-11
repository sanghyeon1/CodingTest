n, m, k = map(int, input().split())

data = []
data = list(map(int, input().split()))

maxNum = int(max(data))
print(maxNum)
secNum = 0
count = 0
total = 0

myIndex = data.index(max(data))
for i in range(n):
    if i == myIndex:
        pass
    elif i != myIndex and secNum < data[i]:
        secNum = data[i]

while count < m:
    for j in range(k):  # 최댓값을 k번 더하는거
        total += maxNum
        count += 1
    total += secNum
    count += 1
print(total)

# Page 92 - 95
