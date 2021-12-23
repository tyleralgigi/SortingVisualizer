import numpy as np
from numpy.core.numeric import full  

full_copies = []
arr = np.round(np.linspace(0,1000, 30),0)
np.random.shuffle(arr)
print(arr)

def insertionSort(arr):
    i = 1
    while i < len(arr):
        j = i
        while j > 0 and arr[j-1] > arr[j]:
            temp = arr[j]
            full_copies.append(np.copy(arr))
            arr[j] = arr[j-1]
            full_copies.append(np.copy(arr))
            arr[j-1] = temp
            full_copies.append(np.copy(arr))
            j -= 1
        i += 1
    return arr

arr = insertionSort(arr)
print(len(full_copies))
print(arr)

"""
i ← 1
while i < length(A)
    j ← i
    while j > 0 and A[j-1] > A[j]
        swap A[j] and A[j-1]
        j ← j - 1
    end while
    i ← i + 1
end while
"""