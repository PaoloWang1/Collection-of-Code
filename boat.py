def max_num_people(weights):
    weights = sorted(weights)
    left = 500
    for x in range(len(weights)):
        left -= weights[x]
        if left < 0:
            return x
    return len(weights)

print(max_num_people([161, 192, 178, 30, 71, 45]))
