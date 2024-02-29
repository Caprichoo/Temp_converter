print("**Welcome to Temperature Convertor**\n")
option = int(input('Do you want to convert to celsius  from fahrenheit or vice-versa, Type 1 for celsius  to fahrenheit or Type 2 for fahrenheit to celsius \n'))
if option == 1:
    celsius = float(input('Enter the temperature in celsius : '))
    result = float((celsius * 9/5) + 32)
    print(f'The temperature in fahrenheit is {result}')
elif option == 2:
    fahrenheit = float(input('Enter the temperature in fahrenheit: '))
    result1 = float((fahrenheit - 32) * 5/9)
    print(f'The temperature in celsius is {result1}')
else:
    print("Wrong input entered, please enter 1 or 2.")
