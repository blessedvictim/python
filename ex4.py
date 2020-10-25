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


def ex9(stime, hours, minutes, seconds):
  import datetime
  dt = datetime.time.fromisoformat(stime)
  dt = dt.replace(hour=dt.hour + hours, minute=dt.minute+ minutes, second=dt.second+seconds)
  return dt

print(ex9("01:00:00", 1, 30, 10))
