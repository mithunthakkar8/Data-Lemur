from collections import deque
def another_one(digits):
  i = len(digits)-1
  while i>=0:
    if digits[i] < 9:
      digits[i] += 1
      break
    else:
      digits[i] = 0
    i -= 1

  digits = deque(digits)
  if all(x == 0 for x in digits):
    digits.appendleft(1)
  
  digits = list(digits)
  
  return digits
  
