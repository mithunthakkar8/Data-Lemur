def is_looping(n):
    visited = set() 

    def helper(num):
        if num == 1:
            return False

        if num in visited:
            return True 

        visited.add(num) 
        
        a = sum(int(i) ** 2 for i in str(num))
        
        return helper(a)

    return helper(n)
