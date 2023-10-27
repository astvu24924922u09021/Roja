def isLeapyear(year):
  if(year%4==0 and year %100!=0)or year%400==0:
    return True
  else:
    return False
Year = int (input ("enter a year:"))
if isLeapYear(year):
  print("{} is aLeapyear.".format(year))
else:
  print("{} is not a Leap year.".format(year))
  
