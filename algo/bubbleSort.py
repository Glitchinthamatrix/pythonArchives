import time
import random
def bubble_sort(elements):
    now=time.time()
    size = len(elements)

    for i in range(size-1):
        swapped = False
        for j in range(size-1-i):
            if elements[j] > elements[j+1]:
                tmp = elements[j]
                elements[j] = elements[j+1]
                elements[j+1] = tmp
                swapped = True

        if not swapped:
            break
    print(f"time taken is {time.time()-now}seconds")    

arr=[random.randrange(1000) for i in range(10000)]
bubble_sort(arr)
print(arr)