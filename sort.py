def bubblesort(li):
    for element in range(len(li)-1,0,-1):
        for ele in range(element):
            if li[ele] > li[ele+1]:
                temp=li[ele]
                li[ele]=li[ele+1]
                li[ele+1]=temp
    return li
    
li=[32,12,54,34,23,987,453,93,5,3,1]
print(bubblesort(li))
        
def bubble_sort_recursive(arr, n=None):
    if n is None:
        n = len(arr)
    if n == 1:
        return arr
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
    return bubble_sort_recursive(arr, n-1)

arr = [64, 34, 25, 12, 22, 11, 90]
print(bubble_sort_recursive(arr))


def mergesort(unsort_list):
    if len(unsort_list) <= 1:
        return unsort_list
    
    mid=len(unsort_list)//2
    left_side=unsort_list[:mid]
    right_side=unsort_list[mid:]

    left_side=mergesort(left_side)
    right_side=mergesort(right_side)

    return list(merge(left_side,right_side))

def merge(left_half , right_half):
    result=[]

    while len(left_half)!=0 and len(right_half)!=0:
        if left_half[0] > right_half[0]:
            result.append(left_half[0])
            left_half.remove(left_half[0])
        else:
            result.append(right_half[0])
            right_half.remove(right_half[0])
    
    if len(left_half) == 0:
        result = result + right_half
    else:
        result = result + left_half
    
    return result


unsort_list=[12,434,1231,90,76,34,756,263,746,23,143,532,1]
print(mergesort(unsort_list))



def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

arr = [12, 11, 13, 5, 6]
print(insertion_sort(arr))



def insertion_sort_recursive(arr, n):
    if n <= 1:
        return
    insertion_sort_recursive(arr, n-1)
    last = arr[n-1]
    j = n-2
    while j >= 0 and arr[j] > last:
        arr[j+1] = arr[j]
        j -= 1
    arr[j+1] = last

arr = [12, 11, 13, 5, 6]
insertion_sort_recursive(arr, len(arr))
print(arr)




def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

arr = [64, 25, 12, 22, 11]
print(selection_sort(arr))




def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    return arr

arr = [12, 34, 54, 2, 3]
print(shell_sort(arr))





def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

print("quick sort: ",quick_sort([5, 3, 8, 4, 2]))



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
        arr[i], arr[0] = arr[0], arr[i]  # Swap
        heapify(arr, i, 0)  # Heapify the root

arr = [4, 10, 3, 5, 1]
heap_sort(arr)
print("Sorted array is:", arr)


def counting_sort(arr):
    max_value = max(arr)
    count = [0] * (max_value + 1)

    for num in arr:
        count[num] += 1

    result = []
    for i in range(len(count)):
        result.extend([i] * count[i])

    return result

print(counting_sort([5, 3, 8, 4, 2]))





def counting_sort_for_radix(arr, exp):
    output = [0] * len(arr)
    count = [0] * 10

    for num in arr:
        index = num // exp
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = len(arr) - 1
    while i >= 0:
        num = arr[i]
        index = num // exp
        output[count[index % 10] - 1] = num
        count[index % 10] -= 1
        i -= 1

    for i in range(len(arr)):
        arr[i] = output[i]

def radix_sort(arr):
    max_value = max(arr)
    exp = 1
    while max_value // exp > 0:
        counting_sort_for_radix(arr, exp)
        exp *= 10
    return arr

print(radix_sort([170, 45, 75, 90, 802, 24, 2, 66]))


