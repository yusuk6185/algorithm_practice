# Time complexity: O(NlogN)

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        # repeat until finding bigger data than the pivot
        while left <= end and array[left] <= array[pivot]:
            left += 1
        # repeat until finding smaller data than the pivot
        while right > start and array[right] >= array[pivot]:
            right -= 1
        # when the searches from left and right cross out, swap the smallest data and the pivot
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        # if not crossed, swap the biggest data and the smallest data
        else:
            array[left], array[right] = array[right], array[left]
    # After the division, left and right partitions perform the sorting
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)

quick_sort(array, 0, len(array) - 1)
print(array)
