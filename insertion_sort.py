def insertion_sort(arr):
    #in python range works from initial value to upperbound-1
    for i in range (1,len(arr)):
        j=i-1
        while j>=0:
            if arr[j+1]<arr[j]:
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
            j=j-1
    
    return arr

arr = [38, 27, 43, 3, 9, 82, 10]
print(insertion_sort(arr))