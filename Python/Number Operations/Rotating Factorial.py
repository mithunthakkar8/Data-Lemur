def rotating_factorial(n):
    operations = ["*", "//", "+", "-"]
    expression = [str(n)] 
    
    for i, num in enumerate(range(n - 1, 0, -1)):
        operation = operations[i % 4]
        expression.append(operation)
        expression.append(str(num))
    
    return eval(" ".join(expression))
