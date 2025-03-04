def convertToBase13(num):
  if num == 0:
    return "0"  # Handle the special case for zero
  
  mapping = '0123456789ABC'
  
  result = ''
  
  negative_flag = 0
  if num<0:
    num = -num
    negative_flag = 1
  
  while num>0:
    result = mapping[num%13] + result
    num = num // 13
  
  if negative_flag == 1:
    result = '-'+result
    
  return result
