def qsort(arr):
    if len(arr) < 2:
        return arr
    
    root_el = arr[0]
    smaller = [i for i in arr[1:] if i < root_el]
    greater = [i for i in arr[1:] if i >= root_el]
    return qsort(smaller) + [root_el] + qsort(greater)

array = [8, 3, 3, 4, 3, 10, 12, 2]
qsort(array)