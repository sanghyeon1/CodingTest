# 공백으로 구분하여 n, m 입력받기
n, m = map(int, input().split())

data = [], tmp = []
for i in range(n):
    data.append(list(map(int, input().split())))
    tmp.append(min(data[i]))

result = max(tmp)
print(result)

# Page 96 - 98
