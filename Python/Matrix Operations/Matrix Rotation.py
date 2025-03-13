def find_rotation(mat, target):
    rotation = mat
    for _ in range(4):
        rotation = [list(row) for row in zip(*rotation[::-1])]
        if rotation == target:
            return True
    
    return False
    
        
