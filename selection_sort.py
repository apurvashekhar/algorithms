def my_sort_again(arr):
    arr_len = len(arr)
    i = 0
    while arr_len > 0 :
        smallest_number_yet = None
        smy_index = None
        num_index = i
        for number in arr[i:]:
            if smallest_number_yet is None or number < smallest_number_yet:
                smallest_number_yet = number
                smy_index = num_index
            num_index = num_index + 1
        temp_variable = arr[i]
        arr[i] = smallest_number_yet
        arr[smy_index] = temp_variable
        i = i + 1
        arr_len = arr_len - 1
    return arr

answer = my_sort_again([3,2,5,-1])
print(answer)
