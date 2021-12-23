import winsound

frequency = 500  # Set Frequency To 2500 Hertz
duration = 100  # Set Duration To 1000 ms == 1 second

for i in range(0,10):
    frequency = (i*10) + 100
    winsound.Beep(frequency, duration)

    