while 1:
    price = int(input("Price of Item : "))
    if price % 10 != 0:
        print("Input the number which is multiple of 10.")
    else:
        break

coin_types = [500, 100, 50, 10]

total = 0
for coin in coin_types:
    total += price // coin
    price %= coin*total

print("Change is : {}".format(total))

# Page 86 - 91
