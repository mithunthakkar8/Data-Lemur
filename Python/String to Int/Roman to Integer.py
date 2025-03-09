def romanToInt(s):
  
	mapping = {'I': 1,'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
	sum_int = 0
	
	for i, sub in enumerate(s):
	  if i+1<len(s):
	    if mapping[s[i]]<mapping[s[i+1]]:
	      print(i,s[i],mapping[s[i]], mapping[s[i+1]],mapping[sub])
	      sum_int -= mapping[sub]
	    else:
	      sum_int += mapping[sub]
	  else:
	    sum_int += mapping[sub]
	
	return sum_int
