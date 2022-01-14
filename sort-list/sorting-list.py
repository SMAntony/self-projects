_list = [100, 34, 2, 89, 77, 81, 450, 666]

# naive method
def naive_method(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return _list

# using build-in methods
def build_in_method(arr):
    arr.sort()
    return(arr)

print("Unsorted List: ", _list)
print("Using Naive approach: ",naive_method(_list), "\nUsing built-in method: ", build_in_method(_list))
