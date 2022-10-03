def bin_search(in_array, item: int) -> int:
    list_len = len(in_array)
    min_pos, max_pos = 0, list_len-1
    while (min_pos < max_pos):
        mid_pos = (min_pos + max_pos) // 2
        #print(mid_pos)
        mid_num = in_array[mid_pos]
        if item == mid_num:
            return mid_pos
        elif item < mid_num:
            max_pos = mid_pos - 1
        else:
            min_pos = mid_pos + 1
    return None