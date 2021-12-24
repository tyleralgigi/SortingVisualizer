import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
from numpy.core.fromnumeric import repeat
from matplotlib.widgets import Button, Slider, RadioButtons
from matplotlib.ticker import AutoLocator

#array size
n = 30
#animation play state 
pause = False
#array of data
arr = np.round(np.linspace(0,2000,n),0)
np.random.shuffle(arr)

full_copies = []
idx = []
access = []
count = 0
sortName = 'Shell Sort'

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

class Index:
    ind = 0
    def refresh(self, val):
        global bars, arr, n, ani, full_copies, idx, access, pause
        full_copies = []
        idx = []
        access = []
        n = int(n_slider.val)
        arr = np.round(np.linspace(0,2000,n),0)
        np.random.shuffle(arr)
        ax.cla()
        bars.remove()
        bars= ax.bar(np.arange(0, len(arr), 1),arr, align='center')
        if val == 'Shell Sort':
            arr = shellSort(arr)
        elif val == "Bubble Sort":
            arr = bubbleSort(arr)
        elif val == "Insertion Sort":
            arr = insertionSort(arr)
        ani = FuncAnimation(fig, update, frames=range(len(full_copies)), blit=False,
                                interval=1000/60, repeat=False)
        pause = False
        ani.resume()

    def pause(self, event):
        global pause
        pause = True
        ani.pause()

    def play(self, event):
        global pause, ani
        pause = False
        ani.resume()
    

def update(frames):
    global full_copies, idx, access, count
    if not pause:
        for (rectangle, height) in zip(bars.patches, full_copies[frames]):
            rectangle.set_height(height)
            rectangle.set_color('#1f77b4')
                    
        idxVal = idx[frames]
        accessVal = access[frames]
        if accessVal == 'get':
            bars.patches[idxVal].set_color('black')
        elif accessVal == 'set':
            bars.patches[idxVal].set_color('red')
                
        if frames == len(full_copies)-1:
            for (rectangle, height) in zip(bars.patches, full_copies[frames]):
                rectangle.set_height(height)
                rectangle.set_color('red')

        return bars

fig, ax = plt.subplots()
bars = ax.bar(np.arange(0, len(arr), 1),arr, align='edge')
plt.subplots_adjust(bottom=0.45)
axfreq = plt.axes([0.25, 0.1, 0.25, 0.03])
n_slider = Slider(
    ax=axfreq,
    label='Array Size',
    valmin=30,
    valmax=100,
    valinit=n,
)


arr = shellSort(arr)

callback = Index()
axpause = plt.axes([0.7, 0.05, 0.1, 0.075])
axradio = plt.axes([0.7, 0.2, 0.2, 0.15])
axplay = plt.axes([0.59, 0.05, 0.1, 0.075])
axrefresh = plt.axes([0.81, 0.05, 0.1, 0.075])

brefresh = Button(axrefresh, 'Refresh')
breplay = Button(axplay, 'Play')
brepause = Button(axpause, 'Pause')
radio1 = RadioButtons(axradio, ('Shell Sort', 'Bubble Sort', 'Insertion Sort', ))

brefresh.on_clicked(callback.refresh)
breplay.on_clicked(callback.play)
brepause.on_clicked(callback.pause)
n_slider.on_changed(callback.refresh)
radio1.on_clicked(callback.refresh)

ani = FuncAnimation(fig, update, frames=range(len(full_copies)), blit=False,
                                interval=1000/60, repeat=False)
plt.show()
