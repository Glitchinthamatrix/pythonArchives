def selection_sort(arr):
    size=len(arr)
    for i in range(size-1):
        min_index=i
        for j in range(i+1,size):
            if arr[i]>arr[j]:
                min_index=j
                arr[i],arr[j]=arr[j],arr[i]
    print("finished")            

test=[89, 78, 61, 53, 23, 21, 17, 12, 9, 7, 6, 2, 1]
selection_sort(test)  
print(test)      