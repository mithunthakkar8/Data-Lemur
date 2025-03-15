def spiral_order(matrix):
    output = []
    while matrix:
        output += matrix.pop(0)  # Take the top row
        
        if matrix and matrix[0]:  # Take the right column
            for row in matrix:
                output.append(row.pop())
        
        if matrix:  # Take the bottom row (in reverse)
            output += matrix.pop()[::-1]
        
        if matrix and matrix[0]:  # Take the left column (in reverse)
            for row in reversed(matrix):
                output.append(row.pop(0))
    
    return output
