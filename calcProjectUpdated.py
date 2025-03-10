import math

start_operator = int(input('Enter one of the following numbers and press \"Enter\". '
    'If you want to close calculator, type \"q\":\n'
    '[1] addition   [2] subtraction     [3] multiplication\n'
    '[4] division   [5] power           [6] square root\n'
    '[q] quit calculator\n'))

print()

## cancel calculator
if start_operator == 'q':
    print('Calculator closed.')
    
## if operation is not available
elif start_operator not in range(1, 7):
    print('Invalid input.')

## if the operation is available
elif start_operator == 1:
    first_num = input('Enter first number. Then, press \'Enter\': ')
    second_num = input('Enter second number. Then, press \'Enter\': ')
    if '.' in first_num and '.' not in second_num:
        first_num = float(first_num)
        second_num = int(second_num)
        print(f'{first_num} + {second_num} = {first_num + second_num}')
    elif '.' in second_num and '.' not in first_num:
        first_num = int(first_num)
        second_num = float(second_num)
        print(f'{first_num} + {second_num} = {first_num + second_num}')
    elif '.' in first_num and second_num:
        first_num = float(first_num)
        second_num = float(second_num)
        print(f'{first_num} + {second_num} = {first_num + second_num}')
    else:
        first_num = int(first_num)
        second_num = int(second_num)
        print(f'{first_num} + {second_num} = {first_num + second_num}')
    
## subtraction
elif start_operator == 2:
    first_num = input('Enter first number. Then, press \'Enter\': ')
    second_num = input('Enter second number. Then, press \'Enter\': ')
    if '.' in first_num and '.' not in second_num:
        first_num = float(first_num)
        second_num = int(second_num)
        print(f'{first_num} - {second_num} = {first_num - second_num}')
    elif '.' in second_num and '.' not in first_num:
        first_num = int(first_num)
        second_num = float(second_num)
        print(f'{first_num} - {second_num} = {first_num - second_num}')
    elif '.' in first_num and second_num:
        first_num = float(first_num)
        second_num = float(second_num)
        print(f'{first_num} - {second_num} = {first_num - second_num}')
    else:
        first_num = int(first_num)
        second_num = int(second_num)
        print(f'{first_num} - {second_num} = {first_num - second_num}')

## multiplication
elif start_operator == 3:
    first_num = input('Enter first number. Then, press \'Enter\': ')
    second_num = input('Enter second number. Then, press \'Enter\': ')
    if '.' in first_num and '.' not in second_num:
        first_num = float(first_num)
        second_num = int(second_num)
        print(f'{first_num} x {second_num} = {first_num * second_num}')
    elif '.' in second_num and '.' not in first_num:
        first_num = int(first_num)
        second_num = float(second_num)
        print(f'{first_num} x {second_num} = {first_num * second_num}')
    elif '.' in first_num and second_num:
        first_num = float(first_num)
        second_num = float(second_num)
        print(f'{first_num} x {second_num} = {first_num * second_num}')
    else:
        first_num = int(first_num)
        second_num = int(second_num)
        print(f'{first_num} x {second_num} = {first_num * second_num}')
    
## division
elif start_operator == 4:
    first_num = input('Enter first number. Then, press \'Enter\': ')
    second_num = input('Enter second number. Then, press \'Enter\': ')
    if '.' in first_num and '.' not in second_num:
        first_num = float(first_num)
        second_num = int(second_num)
        print(f'{first_num} / {second_num} = {first_num / second_num}')
    elif '.' in second_num and '.' not in first_num:
        first_num = int(first_num)
        second_num = float(second_num)
        print(f'{first_num} / {second_num} = {first_num / second_num}')
    elif '.' in first_num and second_num:
        first_num = float(first_num)
        second_num = float(second_num)
        print(f'{first_num} / {second_num} = {first_num / second_num}')
    else:
        first_num = int(first_num)
        second_num = int(second_num)
        print(f'{first_num} / {second_num} = {first_num / second_num}')

## power
elif start_operator == 5:
    first_num = input('Enter base number. Then, press \'Enter\': ')
    second_num = input('Enter exponent. Then, press \'Enter\': ')
    if '.' in first_num and '.' not in second_num:
        first_num = float(first_num)
        second_num = int(second_num)
        print(f'{first_num} * {second_num} = {first_num ** second_num}')
    elif '.' in second_num and '.' not in first_num:
        first_num = int(first_num)
        second_num = float(second_num)
        print(f'{first_num} * {second_num} = {first_num ** second_num}')
    elif '.' in first_num and second_num:
        first_num = float(first_num)
        second_num = float(second_num)
        print(f'{first_num} * {second_num} = {first_num ** second_num}')
    else:
        first_num = int(first_num)
        second_num = int(second_num)
        print(f'{first_num} * {second_num} = {first_num ** second_num}')
    
## square root
elif start_operator == 6:
    root_val = input('Enter number. Then, press \'Enter\': ')
    if '.' in root_val:
        root_val = float(root_val)
        print(f'√{root_val} = {math.sqrt(root_val)}')
    else:
        root_val = int(root_val)
        print(f'√{root_val} = {math.sqrt(root_val)}')
