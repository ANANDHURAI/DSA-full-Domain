def BubbleSort(arr):
    for i in range(len(arr)):
        for j in range(i+1 ,len(arr)):
            if arr[i] < arr[j]:
                arr[i] ,arr[j] = arr[j],arr[i]
    return arr
arr=[32,64,12,43,23,432,9,123,1444]
print(BubbleSort(arr))


# def BubbleSortwithRecurtion(arr):
#     if len(arr) == 0 or len(arr)==1:
#         return arr
#     BubbleSortwithRecurtion(arr)
#     return arr
# arr=[32,64,12,43,23,432,9,123,1444]
# print(BubbleSortwithRecurtion(arr))

def insertion(arr):
    for i in range(len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = key

    return arr
arr= [12,75,334,11,223,9,56,7]
print(insertion(arr))


def selection(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1 , len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i] , arr[min_index] = arr[min_index] , arr[i]
    return arr

arr= [12,75,334,11,223,9,56,7]
print(selection(arr))


def mergesort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]

        mergesort(left)
        mergesort(right)
        i = j= k = 0
        while i < len(left) and j < len(right) :
            if left[i] < right[j]:
                arr[k] = left[i]
                i+=1
            else:
                arr[k] = right[j]
                j+=1
            k+=1
        while i < len(left):
            arr[k] = left[i]
            i+=1
            k+=1
        while j < len(right):
            arr[k] = right[j]
            j+=1
            k+=1
    return arr

arr= [12,75,334,11,223,9,56,7]
print(mergesort(arr))





def shellsort(arr):
    gap = len(arr) // 2
    while gap >0:
        for i in range(gap , len(arr)):
            temp = arr[i]
            j = i
            while j >= gap and arr[j-gap] > temp :
                arr[j] = arr[j-gap]
                j-=gap
            arr[j] = temp
        gap = gap // 2
    return arr
arr= [12,75,334,11,223,9,56,7]
print(shellsort(arr))
        



def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr

print(heap_sort([5, 3, 8, 4, 2]))



def bucket_sort(arr):
    max_value = max(arr)
    size = len(arr)
    buckets = [[] for _ in range(size)]

    for num in arr:
        index = int(num * size)
        buckets[index].append(num)

    for i in range(size):
        buckets[i] = sorted(buckets[i])

    return [num for bucket in buckets for num in bucket]

print(bucket_sort([0.42, 0.32, 0.58, 0.29, 0.93]))
