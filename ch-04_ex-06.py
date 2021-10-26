## Rewrite your pay computation to give the employee 1.5
##times the hourly rate for hours worked above 40 hours.
##Enter Hours: 45
##Enter Rate: 10
##Pay: 475.0

def computepay(hours, rate):
    if hours > 40:
        overtimeHours = hours - 40.0
        regularPay = rate * 40.0
        overtimePay = overtimeHours * (1.5 * rate)
        actualPay = overtimePay + regularPay
    else:
        actualPay = rate * hours
    return actualPay

try:
    hours = float(input('Enter Hours: '))
    rate = float(input('Enter Rate: '))
except:
    print('Error, please enter numberic input')
    quit()

print('Pay: $' + str(computepay(hours, rate)))





