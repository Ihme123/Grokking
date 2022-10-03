def find_smallest(in_array):
    smallest_idx, smallest_num = 0, in_array[0]
    for idx, elem in enumerate(in_array):
        if elem < smallest_num:
            smallest_idx, smallest_num = idx, elem
    return smallest_idx

def ins_sort(in_array):
    sorted_array = []
    for i in range(len(in_array)):
        smallest = find_smallest(in_array)
        sorted_array.append(in_array.pop(smallest))
    return sorted_array