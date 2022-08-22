def Sort(array):
    if len(array) > 1:
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]
        Sort(left)
        Sort(right)
        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
              array[k] = left[i]
              i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            array[k]=right[j]
            j += 1
            k += 1

array = [3,5,1,7,6,4,9,23,2]
Sort(array)
print("The sorted array is : ")
print(*array)