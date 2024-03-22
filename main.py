stdform = input('Enter a number in scientific notation: ')
stdform = stdform.strip()

error_msg = 'Error converting to scientific E notation.'
valid_chars = '0123456789Ex-.^'
valid = True

pow10pos = stdform.find('x10^')
if pow10pos == -1:
    valid = False
    # raise ValueError('pow10 missing!!')
else:
    mantissa, exponent = stdform.split('x10^')
    # print(mantissa, exponent)

    for ch in stdform:
        if not ch in valid_chars:
            valid = False
            # raise ValueError('Invalid Chars')

    if valid:
        # check for valid symbol count
        symbols = '.x^'
        for symbol in symbols:
            if stdform.count(symbol) > 1:
                valid = False

    if valid:
        if not float(exponent).is_integer():
            valid = False

if not valid:
    print(error_msg)
else:
    result = mantissa + 'E' + exponent
    print(f'This number in E notation is {result}.')