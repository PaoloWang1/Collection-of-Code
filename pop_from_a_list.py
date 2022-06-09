def pop_from_a_list(a_list, remove_indices):
    greatest = -1
    index = 0
    for y in range(len(remove_indices)):
        for x in range(len(remove_indices)):
            if remove_indices[x] > greatest:
                greatest = remove_indices[x]
                index = x
        popped = remove_indices.pop(index)
        popped = a_list.pop(greatest)
        greatest = -1
    
    return(a_list)
