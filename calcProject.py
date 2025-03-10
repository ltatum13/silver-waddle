import math

start_operator = str(input('Enter any of the following operations (addition, '
    'subtraction, multiplication, division, power, square root). Then, press \"Enter\".\n'
    'If you want to close calculator, type \"q\": '))
print()

operations = ['addition', 'subtraction', 'multiplication', 'division', 'power', 'square root']

while True:
    ## cancel calculator
    if start_operator == 'q':
        print('Calculator closed.')
        break
    
    ## if operation is not available
    elif start_operator not in operations:
        print('Invalid input.')
        break
        
    ## if the operation is available
    elif start_operator in operations:
        ## addition
        if start_operator == 'addition':
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
        elif start_operator == 'subtraction':
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
        elif start_operator == 'multiplication':
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
        elif start_operator == 'division':
            first_num = input('Enter first number. Then, press \'Enter\': ')
            second_num = input('Enter second number. Then, press \'Enter\': ')
            if '.' in first_num and '.' not in second_num:
                first_num = float(first_num)
                second_num = int(second_num)
                print(f'{first_num} / {second_num} = {first_num // second_num}')
            elif '.' in second_num and '.' not in first_num:
                first_num = int(first_num)
                second_num = float(second_num)
                print(f'{first_num} / {second_num} = {first_num // second_num}')
            elif '.' in first_num and second_num:
                first_num = float(first_num)
                second_num = float(second_num)
                print(f'{first_num} / {second_num} = {first_num // second_num}')
            else:
                first_num = int(first_num)
                second_num = int(second_num)
                print(f'{first_num} / {second_num} = {first_num // second_num}')
    
        ## power
        elif start_operator == 'power':
            first_num = input('Enter first number. Then, press \'Enter\': ')
            second_num = input('Enter second number. Then, press \'Enter\': ')
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
        elif start_operator == 'square root':
            root_val = input('Enter number. Then, press \'Enter\': ')
            if '.' in root_val:
                root_val = float(root_val)
                print(f'√{root_val} = {math.sqrt(root_val)}')
            else:
                root_val = int(root_val)
                print(f'√{root_val} = {math.sqrt(root_val)}')

