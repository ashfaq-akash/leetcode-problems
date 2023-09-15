def quick_sort(arr,s,e):
    if (e-s+1<=1):
        return arr
    
    #last element is pivot element
    pivot=arr[e]
    left=s

    for i in range(s,e):
        if arr[i]<pivot:
            temp=arr[left]
            arr[left]=arr[i]
            arr[i]=temp
            left +=1

    #swapping between left index element and pivot element which is end of index    
    arr[e]=arr[left]
    arr[left]=pivot
    
    #applying sorting to the left side of pivot element
    quick_sort(arr,s,left-1)
     #applying sorting to the right side of pivot element
    quick_sort(arr,left+1,e)

arr = [38, 27, 43, 3, 9, 82, 10]
quick_sort(arr, 0, len(arr) - 1)
print(arr)  # This will print the sorted array

