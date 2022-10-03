# Dinamic programming
weight = {
    'water': 3,
    'book': 1,
    'food': 2,
    'jacket': 2,
    'camera': 1
}
utility = {
    'water': 10,
    'book': 3,
    'food': 9,
    'jacket': 5,
    'camera': 6
}

def get_cell_value(dinamic_table, utility, weight, weights, num, col, name):
    """
    Formula goes like this: dinamic_table[i][j] = max (previous maximum, current element utility + utility of the remaining weight) =
    = max (dinamic_table[i-1][j], utility[name] + dinamic_table[i-1][col - 
    """
    # If the current thing can't fit in
    previous_max = dinamic_table[num-1][col]
    # If after the current thing is added there is still some space
    free_weight = weights[col] - weight[name]
    if free_weight > 0:
        free_weight_index = weights.index(free_weight)
        cost_of_free_space = dinamic_table[num-1][free_weight_index]
        utility_and_free_space = utility[name] + cost_of_free_space
        return max(previous_max, utility_and_free_space)
    elif free_weight == 0:
        return max(previous_max, utility[name])
    else:
        return previous_max

def din_prog(weight, utility, max_weight):
    # Make weights from min_weight up to the max_weight with the needed period
    weight_discreet = min(weight.values())
    weights = [weight_discreet * (1+i) for i in range(max_weight // weight_discreet)]
    # Set ids for every item in store
    ids = {}
    for num, item in enumerate(weight.keys()):
        ids[item] = num
    
    num_weights, num_ids = len(weights), len(ids) 
    # Generate table
    dinamic_table = [[0 for i in range(num_weights)] for j in range(num_ids)]
    for name, num in ids.items():
        # If it's the first row in the table, then fill it up with just item utility for every weight in weights
        if num == 0:
            dinamic_table[num] = [utility[name] if weight[name] <= weights[col] else 0 for col in range(num_weights)]
        else:
            dinamic_table[num] = [get_cell_value(dinamic_table, utility, weight, weights, num, col, name) for col in range(num_weights)]
    return dinamic_table
din_prog(weight, utility, 6)