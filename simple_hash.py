def simple_hash_func(string: str) -> int:
    hash_tab = {'a': 1, 'b': 2, 'c': 3, 'd': 5, 'e': 7, 'f': 11, 'g': 13, 'h': 17, 'i': 19, 'j': 23, 'k': 31, 'l': 37, 'm': 41, 'n': 43, 'o': 47, 'p': 51, 'q': 53, 'r': 57, 's': 61, 't': 67, 'u': 71, 'v': 73, 'w': 79, 'x': 83, 'y': 87, 'z': 91}
    hash_size = 10
    if string == '':
        return 0
    
    char_sum = 0
    for char in string:
        char_sum += hash_tab[char]
    return char_sum % hash_size