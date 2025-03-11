def generate(numRows): 
    # Initialize Pascal's Triangle as a list of lists
    # Each row starts with the appropriate number of elements initialized to 0
    pascal = [[0] * i for i in range(1, numRows + 1)]
    
    # Iterate through each row
    for i in range(len(pascal)):
        # Set the first and last elements of each row to 1
        pascal[i][0] = 1
        pascal[i][-1] = 1
        
        # Iterate through the inner elements of the row
        # range(1, i) ensures we skip the first two rows of the triangle as this loop would start when i=2
        for j in range(1, i):
            # Compute the value using the sum of two elements directly above in the previous row
            pascal[i][j] = pascal[i-1][j] + pascal[i-1][j-1]
    
    return pascal  # Return the generated Pascal's Triangle
