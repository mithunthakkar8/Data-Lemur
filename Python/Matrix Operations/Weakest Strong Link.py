def weakest_strong_link(strength):
    # Find the minimum value in each row
    row_mins = [min(row) for row in strength]

    # Find the maximum value in each column.
    # zip(*strength) transposes the matrix
    col_maxes = [max(col) for col in zip(*strength)]

    # Check if any row min is also a column max
    for value in row_mins:
        if value in col_maxes:
            return value

    return -1  # Return -1 if no such value is found
