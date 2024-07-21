# Q7. Calculate the factorial of a number using lambda function.

function = lambda a: a+function(a-1) if a!=1 else 1

sums = function(10)
print(sums)


