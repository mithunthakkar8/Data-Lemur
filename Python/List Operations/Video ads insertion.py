def can_insert_ads(feed_items, n):
    if n == 0:
        return True
    
    if feed_items[-1]==0:
        n -= 1
    
    if feed_items[0] == 0:
        n -= 1
    
    for i in range(len(feed_items)-1):
        if feed_items[i]==0 and feed_items[i+1]==0:
            if n > 0:
                n -= 1
            else:
                return True
    
    if n<=0:
        return True
    
    return False
            
	  
    
