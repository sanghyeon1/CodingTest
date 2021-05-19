n, m = map(int, input("number, length : ").split())
height = list(map(int, input("height of RiceCake : ").split()))
height.sort()
max_len = int(height[n-1])
result = 0

while True:
    for i in height:
        if i > max_len:
            result += i - max_len
        else:
            pass
    if max_len == 0:
        print("Error")
        break
    if result >= m:
        print(max_len)
        break
    max_len -= 1
    result = 0

# Page 201 - 205
