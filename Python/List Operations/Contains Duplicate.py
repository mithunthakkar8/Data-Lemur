from collections import Counter
def contains_duplicate(input)-> bool:
  counter = Counter(input)
  for i in counter.values():
    if i > 1:
      return True
    else:
      return False
