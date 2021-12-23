import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
from numpy.core.fromnumeric import repeat

full_copies = []
idx = []
access = []

def main():
    global full_copies, idx, access
    run = True
    while run:
        print("Welcome to the Sorting Visualizer \n")
        #array size
        #n = int(input('Pleas enter the length of the array: '))
        arr = np.round(np.linspace(0,1000,128),0)
        print("Array of size "+ str(30) + " in range of 0-1000:")
        np.random.shuffle(arr)
        print(arr)

        fig, ax = plt.subplots()
        container = ax.bar(np.arange(0, len(arr), 1),arr, align='edge')

        print("Which sorting algothrim would you like to use: \n  1. Insertion Sort \n  2. Bubble Sort \n  3. Shell Sort")
        sorting = int(input('Pleas enter the length of the array: '))
        if sorting == 1:
            arr = insertionSort(arr)
        elif sorting == 2:
            arr = bubbleSort(arr)
        elif sorting == 3:
            arr = shellSort(arr)
        else:
            print("A correction option was not selection, so we will run insertion sort...")
            arr = insertionSort(arr)

        def update(frames):
            for (rectangle, height) in zip(container.patches, full_copies[frames]):
                rectangle.set_height(height)
                rectangle.set_color('#1f77b4')
            
            idxVal = idx[frames]
            accessVal = access[frames]
            if accessVal == 'get':
                container.patches[idxVal].set_color('black')
            elif accessVal == 'set':
                container.patches[idxVal].set_color('red')
            return container
        
        ani = FuncAnimation(fig, update, frames=range(len(full_copies)), blit=False,
                                interval=1000/60, repeat=False)
        plt.show()
        print("Sorted Array: ")
        print(arr)
        print("Would you like to run again: (Y for yes / N for no)")
        ans = input('Y or N: ')
        if ans == "n" or  ans == "N":
            full_copies = []
            idx = []
            access = []
            print("Ending...")
            run = False

def insertionSort(arr):
    i = 1
    while i < len(arr):
        j = i
        while j > 0 and arr[j-1] > arr[j]:
            idx.append(j)
            access.append('get')
            temp = arr[j]
            full_copies.append(np.copy(arr))
            
            idx.append(j)
            access.append('set')
            arr[j] = arr[j - 1]
            full_copies.append(np.copy(arr))
            
            
            idx.append(j-1)
            access.append('set')
            arr[j - 1] = temp
            full_copies.append(np.copy(arr))
            j -= 1
            
        i += 1
    return arr

def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j + 1] < arr[j]:
                temp = arr[j]
                full_copies.append(np.copy(arr))
                idx.append(j)
                access.append('get')
                
                arr[j] = arr[j + 1]
                full_copies.append(np.copy(arr))

                idx.append(j)
                access.append('set')
                
                arr[j + 1] = temp
                full_copies.append(np.copy(arr))
                idx.append(j+1)
                access.append('set')
    return arr

def shellSort(arr):
    gap = len(arr) // 2
    while gap > 0:
        i = 0
        j = gap
        while j < len(arr):
            if arr[i]>arr[j]:
                temp = arr[j]
                full_copies.append(np.copy(arr))
                idx.append(j)
                access.append('get')
                
                arr[j] = arr[i]
                full_copies.append(np.copy(arr))

                idx.append(j)
                access.append('set')
                
                arr[i] = temp
                full_copies.append(np.copy(arr))
                idx.append(i)
                access.append('set')   
            i += 1
            j += 1
            
            k = i
            while k - gap > -1:
 
                if arr[k - gap] > arr[k]:
                    temp = arr[k-gap]
                    full_copies.append(np.copy(arr))
                    idx.append(k-gap)
                    access.append('get')
                    
                    arr[k-gap] = arr[k]
                    full_copies.append(np.copy(arr))

                    idx.append(k-gap)
                    access.append('set')
                    
                    arr[k] = temp
                    full_copies.append(np.copy(arr))
                    idx.append(k)
                    access.append('set') 

                k -= 1
        gap //= 2
    return arr


if __name__== "__main__":
    main()
