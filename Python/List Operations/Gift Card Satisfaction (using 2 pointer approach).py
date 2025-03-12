def max_satisfaction(expectations, cards):
    # Sort the expectations in ascending order to process them efficiently
    expectations.sort()
    
    # Sort the cards in ascending order so we can match them optimally
    cards.sort()
    
    # Initialize a counter to keep track of satisfied expectations
    count = 0  
    
    # Initialize two pointers: 
    # `i` for traversing the expectations list
    # `j` for traversing the cards list
    i, j = 0, 0  
    
    # Iterate through both lists using two pointers
    while i < len(expectations) and j < len(cards):
        
        # If the current expectation can be satisfied by the current card
        if expectations[i] <= cards[j]:  
            # Increase the count of satisfied expectations
            count += 1  
            # Move to the next expectation since this one is satisfied
            i += 1  
        
        # Move to the next card, whether it was used or not
        j += 1  
    
    # Return the total number of expectations that were satisfied
    return count  
