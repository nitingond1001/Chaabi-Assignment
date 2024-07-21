
# 9.Write a func that takes 3 args:
# from_date - string representing a date in the form of 'yy-mm-dd'
# to_date - string representing a date in the form of 'yy-mm-dd'
# difference - int
# Returns True if from_date and to_date are less than difference days away from each other, else
# returns False



from datetime import datetime
def func_datetime(from_date, to_date, difference):

  from_date = datetime.strptime(from_date, "%Y-%m-%d")
  to_date = datetime.strptime(to_date, "%Y-%m-%d")
  difference_in_days = (to_date - from_date).days

  return difference_in_days < difference

print(func_datetime("2023-05-27", "2023-05-28", 2))

# Output:

# False