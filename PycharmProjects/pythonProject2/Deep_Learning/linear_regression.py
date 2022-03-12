def program_4(n):
  i = 1
  for k in range(n):
      i*=2
      ##print(i)
  j=1
  for k in range(i):
      j*=2
      print(j)
  t=1
  if n%3 == 0:
      for r in range(i):
          t+=r*(r+1)
  return t

program_4(4)