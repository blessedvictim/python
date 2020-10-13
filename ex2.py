def ex4(seats):
  if len(seats) == 0:
    return None
  l = len(seats[0])
  for i, r in enumerate(seats):
    if i == 0:
      continue
    if len(r) != l:
      return None
    if seats[i-1] >= r:
      return False
  return True

print(ex4([
[2, 0, 0],
[1, 1, 1],
[2, 2, 2],]))

print(ex4([
[0, 0, 0],
[1, 1, 1],
[2, 2, 2]
]))

from datetime import datetime

def ex5(dates, mode):
  if mode.upper() == "ASC":
    dates.sort(key=lambda date: datetime.strptime(date, "%d-%m-%Y_%H:%M"))
  if mode.upper() == "DESC":
     dates.sort(key=lambda date: datetime.strptime(date, "%d-%m-%Y_%H:%M"),reverse = True)
  return dates
  
print(ex5(["10-02-2018_12:30", "10-02-2016_12:30", "10-02-2018_12:15"], "ASC"))
print(ex5(["10-02-2018_12:30", "10-02-2016_12:30", "10-02-2018_12:15"], "desc")) 

import re

def ex6(num):
  return not bool(re.match(r'(.).*\1', num))

print(ex6("123"))
print(ex6("112233"))
print(ex6("1025"))
