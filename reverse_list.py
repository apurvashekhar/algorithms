arr = [1,2,3,4]
i = 0
n = len(arr)
while n > i:
    temp_variable = arr[n - 1]
    arr[n - 1] = arr[i]
    arr[i] = temp_variable
    i = i + 1
    n = n - 1
print(arr)
