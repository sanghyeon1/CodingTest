n = int(input())
num = []
for i in range(n):
    num.append(int(input()))

temp = 0
for i in range(n):
    j = i+1
    for j in range(n):
        if j >= len(num):
            break
        if num[i] < num[j]:
            continue
        elif num[i] >= num[j]:
            temp = num[i]
            num[i] = num[j]
            num[j] = temp

print(num)

# Page 178 - 179
