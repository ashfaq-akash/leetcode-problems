def merge_sort(arr):
    if len(arr)<=1:
        return arr
    
    mid=len(arr)//2
    left_arr=arr[:mid]
    right_arr=arr[mid:]

    # Recursively sort both halves until reach one element
    left_arr=merge_sort(left_arr)
    right_arr=merge_sort(right_arr)

    # Merge the sorted halves
    return merge(left_arr,right_arr)


def merge(left,right):
    l_index=0
    r_index=0
    res=[]

    # Traverse through both arrays
    while l_index<len(left) and r_index<len(right):
        if left[l_index]<right[r_index]:
            res.append(left[l_index])
            l_index +=1
        else:
            res.append(right[r_index])
            r_index +=1
    
    # If left list still has elements, add them to result
    while l_index<len(left):
         res.append(left[l_index])
         l_index +=1
    
    # If right list still has elements, add them to result
    while r_index<len(right):
         res.append(right[r_index])
         r_index +=1
    
    return res

arr = [38, 27, 43, 3, 9, 82, 10]
print(merge_sort(arr))

