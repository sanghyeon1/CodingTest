n, k = map(int, input("Input n, k : ").split())
a = list(map(int, input("Input a :").split()))
b = list(map(int, input("Input b :").split()))

a.sort()
b.sort()
b.reverse()  # 정렬
print(a, b)

tmp = 0

for i in range(k):
    if a[i] < b[i]:
        tmp = a[i]
        a[i] = b[i]
        b[i] = tmp
    else:
        break

print(sum(a))


