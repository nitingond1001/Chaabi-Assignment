# Q10. Of date and days
# Write a func that takes 2 args:
# date - string representing a date in the form of 'yy-mm-dd'
# n - integer
# Returns the string representation of date n days before 'date'
# E.g. f('16-12-10', 11) should return '16-11-29'



from datetime import datetime, timedelta

def func_days(days,n):
    date = datetime.strptime(date, "%Y-%m-%d")

    new_date = date - timedelta(days=n)

    return new_date.strftime("%Y-%m-%d")

print(func_days('16-12-10', 11))

# # Output:
# # '16-11-29'