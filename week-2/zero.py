def shift_zero(arr, n):
    count = 0

    for i in range(n):
        if arr[i] != 0: 
            arr[count] = arr[i]
            count+=1

    while count<n:
        arr[count] = 0
        count+=1

arr = [3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1]
n = len(arr)
shift_zero(arr,n)
print(arr)