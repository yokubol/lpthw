number1 = int(input("Enter a dividend: "))
number2 = int(input("Enter a devisor: "))
number3 = round(number1/number2)
remainder = number1 % number2

print('The quotient of ', number1, ' and ', number2, ' is ', number3, ' with a remainder of ', remainder, sep='')
