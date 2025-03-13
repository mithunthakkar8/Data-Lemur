from collections import deque

def min_amplitude(arr):
    if len(arr) <= 4:
        return 0

    arr.sort()
    arr = deque(arr)
    
    for _ in range(3):
        if arr[-1] - arr[1] > arr[-2] - arr[0]:
            arr.pop()
        else:
            arr.popleft() 

    return arr[-1] - arr[0]
