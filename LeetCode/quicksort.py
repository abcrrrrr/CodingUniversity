def partition(array, start, end):
    pivot = array[start]
    low = start + 1
    high = end

    while True:
        while low <= high and array[low] <= pivot:
            low += 1
        while low <= high and array[high] >= pivot:
            high -= 1
        if low > high:
            break
        array[low], array[high] = array[high], array[low]

    array[start], array[high] = array[high], array[start]
    return high

def quick_sort(array, start, end):
    if start >= end:
        return
    mid = partition(array, start, end)
    quick_sort(array, mid+1, end)
    quick_sort(array, start,mid-1)

nums = [5,3,7,4,6,8,9,23,43,67,3,6,0]
quick_sort(nums,0,len(nums)-1)
print(nums)

