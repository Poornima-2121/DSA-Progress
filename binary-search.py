def binarySearch(arr,key):
    low=0
    high=len(arr)-1
    result = -1
    while low<=high:
        mid=(low+high)//2
        if arr[mid] == key:
            result = mid
            high = mid-1 #if the array has multiple same numbers - get the first occurence
        elif arr[mid]<key:
            low = mid+1
        else:
            high=mid-1
    return result

arr = [1,1,1, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 4, 5, 5, 5]
key= 3
print(binarySearch(arr,key))
            