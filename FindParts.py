def binary_search(parts_list, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if parts_list[mid] == target:
            return mid
        elif parts_list[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None


n = int(input("Number of Parts : "))
array = list(map(int, input("Parts : ").split()))
m = int(input("Number of Parts to find : "))
find = list(map(int,  input("Parts to find : ").split()))
array.sort()

for i in find:
    result = binary_search(array, i, 0, n-1)
    if result is not None:
        print("yes", end=' ')
    else:
        print("no", end=' ')
