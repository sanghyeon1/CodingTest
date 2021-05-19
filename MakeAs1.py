x = int(input("Input Number : "))
count = 0

while x != 1:
    if (x - 1) % 5 == 0:
        x -= 1
        count += 1
    if x % 5 == 0:
        x //= 5
        count += 1
    if x % 3 == 0:
        x //= 3
        count += 1
    if x % 2 == 0:
        x //= 2
        count += 1

print(count)
# Page 217 - 219
