# staircase
def ex7(n):
  res = ""

  def underscores(direction):
    a = 1
    if not direction:
      a = a - 1
    def c1(n, i):
      return n-i-a
  
    return c1

  def grid(direction):
    a = 1
    if not direction:
      a = a - 1
    def c2(n, i):
      return n-(n-i-a)
    return c2
  
    

  first, second = None, None
  if n > 0:
    first = underscores(True)
    second = grid(True)
  else:
    first = grid(False)
    second = underscores(False)
  n = abs(n)

  for i in range(n):
    for ii in range(first(n, i)):
      res += "_"
    for ii in range(second(n, i)):
      res += "#"
    res += "\n"
  return res

print(ex7(3))

def ex8(s):
  reduced = ""
  i = 1
  while i < len(s):
    if s[i] == s[i-1]:
      if i + 2 > len(s):
        i = i + 1
      else:
        i = i + 2
      continue
    else:
      reduced += s[i-1]
  
    i = i + 1
  return reduced


print(ex8("aaabccddd"))
