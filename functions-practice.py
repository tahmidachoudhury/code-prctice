def sumTwoNumbers(num1, num2):
    return num1 + num2

def sumThreeNumbers(num1, num2, num3):
    return num1 + num2 + num3

def secsinWeeks(X):
    days = X*7
    hours = 24*days
    minutes = 60*hours
    seconds = 60*minutes
    return seconds

print(secsinWeeks(10))

print(sumThreeNumbers(5, 10, 2))