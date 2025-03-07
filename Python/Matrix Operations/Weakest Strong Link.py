def weakest_strong_link(strength):
    # Iterate over each row in the 2D list (matrix)
    for i, row in enumerate(strength):
        # Iterate over each element (column) in the current row
        for j, column in enumerate(strength[i]):
            # Check if the minimum value in the current row 
            # is also the maximum value in its column
            if min(row) == max(row[j] for row in strength):
                return min(row)  # Return the weakest strong link (min value of row)

    return -1  # Return -1 if no such value is found
