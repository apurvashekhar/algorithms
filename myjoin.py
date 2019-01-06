# You are given an array of strings @arr and another string called @separator.
# Write a method that joins all elements of @arr with @separator. For example -
# if @arr = ['This', 'is', 'some', 'text'] and @separator is "==", the returned
# value shold be 'This==is==some==text'.
def myjoin(arr, separator):
    n = 0
    answer_string = ""
    #while n < len(arr): #3
    #    print('n =', n)
    #    answer_string += arr[n] + separator
    #    print('arr[n] = ',arr[n])
    #    print('answer_string = ', answer_string)
    #    n = n + 1
    #separator_len = len(separator)
    #answer_string = answer_string[0:-separator_len]
    while n < (len(arr)-1): #2
        print('n =', n)
        answer_string += arr[n] + separator
        print('arr[n] = ',arr[n])
        print('answer_string = ', answer_string)
        n = n + 1
    #answer_string = answer_string + list1[len(list1)- 1]
    return (answer_string)

list1 = ['a', 'b','c']
x = myjoin(list1, '==')
print(x)
