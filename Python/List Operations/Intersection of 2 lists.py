from collections import Counter

def intersection(a, b):
  # Create frequency count of elements in both lists
  a = Counter(a)  # Dictionary-like object with element counts from lst1
  b = Counter(b)  # Dictionary-like object with element counts from lst2
  
  # Perform element-wise intersection (keeps min count from both lists) 
  # ensuring duplicates are accounted for
  return list(a & b)  # Returns a Counter with min occurrences in both lists
