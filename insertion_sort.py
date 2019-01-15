def my_insertion_sort(arr):
    print(arr)
    idx = 1
    while idx < len(arr): #2 < 4
        pointer = idx - 1 #1
        while pointer >= 0:
            if arr[pointer + 1] < arr[pointer]:
                temp_variable = arr[pointer]
                arr[pointer] = arr[pointer + 1]
                arr[pointer + 1] = temp_variable
                print(arr)
            pointer = pointer - 1
        idx = idx + 1


    print(arr)


my_insertion_sort([4,3,1,-2])
