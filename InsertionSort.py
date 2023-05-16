def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

arr = [5, 2, 7, 3, 9, 1, 56, 5666664, 3454353, 3454, 5435]
insertion_sort(arr)
print(arr)
