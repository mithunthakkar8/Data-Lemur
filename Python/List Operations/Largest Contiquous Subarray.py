def max_subarray_sum(input):
    j = 1
    max_sum = 0
    for i in range(len(input)):
        for j in range(i+1,len(input)+1):
            print(i,j, input[i:j], sum(input[i:j]))
            if sum(input[i:j])>max_sum:
                max_sum = sum(input[i:j])
    return max_sum
