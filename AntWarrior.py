n = int(input("Input the Number of storage : "))
k = list(map(int, input("Input the Number of food : ").split()))
d = [0] * 100

d[0] = k[0]
d[1] = max(k[0], k[1])
for i in range(2, n):
    d[i] = max(d[i-1], d[i-2] + k[i])
print(d[n-1])
# Page 220 - 222