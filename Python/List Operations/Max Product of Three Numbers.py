import math
def max_three(input):
    largest_triplet = []
    sorted_input = sorted(input)
    if sorted_input[0] > 0 or sorted_input[1] > 0:
        largest_triplet = sorted_input[-3:]
    else:
        while len(largest_triplet) < 2:
            if abs(sorted_input[0])<sorted_input[-1]:
                largest_triplet.append(sorted_input.pop())
            else:
                largest_triplet.append(sorted_input.pop(0))
                
        if math.prod(largest_triplet)<0:
            largest_triplet.append(sorted_input.pop(0))
        else:
            largest_triplet.append(sorted_input.pop())
    
    return math.prod(largest_triplet)
