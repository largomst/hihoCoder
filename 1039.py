n = int(raw_input())
for i in range(n):
    arr = raw_input()
    new_arr = list()
    new_arr.append(arr[0])
    for i in range(len(arr) - 1):
        if arr[i] != arr[i + 1]:
            new_arr.append(arr[i + 1])
    print(len(new_arr))
