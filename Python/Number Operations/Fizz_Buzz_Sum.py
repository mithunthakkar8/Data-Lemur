def fizz_buzz_sum(target):
  store = set()
  for i in range(1,target//3+1):
    if 3*i<target:
      store.add(3*i)
    if 5*i<target:
      store.add(5*i)
  return sum(store)
