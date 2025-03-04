def is_same_stripes(matrix):
  result = True
  for i in range(len(matrix)-1):
    if matrix[i][0:len(matrix[0])-1] != matrix[i+1][1:len(matrix[0])]:
      result = False
  return result
   
