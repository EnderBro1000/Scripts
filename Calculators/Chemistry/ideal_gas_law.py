unknownPos = 0
unknownCount = 0
gasConstant = .0821
unknownVar = 0
variables = [
    [0, ''],
    [0, ''],
    [0, ''],
    [0, '']
]


def maybe_float(i):
    try:
        return float(i)
    except (ValueError, TypeError):
        return i


variables[0][0] = input('Value of Pressure: ')
variables[0][1] = input('Unit (atm, torr, mmHg, Pa, kPa, bar): ')
variables[1][0] = input('Value of Volume: ')
variables[1][1] = input('Unit (L, mL): ')
variables[2][0] = input('Value of Particles: ')
variables[2][1] = input('Unit(moles, particles): ')
variables[3][0] = input('Value of Temperature: ')
variables[3][1] = input('Unit(C, K, F): ')

for var in variables:
    var[0] = maybe_float(var[0])

for var in variables:
    unknownPos += 1
    if not isinstance(var[0], float):  # finds the unknown's position
        unknownVar = unknownPos
        unknownCount += 1
        if unknownCount != 1:  # checks for more or less than 1 unknown
            raise Exception('there can only be 1 unknown variable')
if unknownVar is None:
    raise Exception('there must be an unknown variable')

# unit converter
if variables[0][0] != '?':  # pressure
    if variables[0][1] == 'atm':
        pass
    elif variables[0][1] == 'torr':
        variables[0][0] /= 760
    elif variables[0][1] == 'mmHg':
        variables[0][0] /= 760
    elif variables[0][1] == 'Pa':
        variables[0][0] /= 101325
    elif variables[0][1] == 'kPa':
        variables[0][0] /= 101.325
    elif variables[0][1] == 'bar':
        variables[0][0] /= 1.013
    else:
        raise Exception('Improper unit for Pressure')
variables[0][1] = 'atm'

if variables[1][0] != '?':  # volume
    if variables[1][1] == 'L':
        pass
    elif variables[1][1] == 'mL':
        variables[1][0] /= 1000
    else:
        raise Exception('Improper unit for Volume')
variables[1][1] = 'L'

if variables[2][0] != '?':  # molecules
    if variables[2][1] == 'moles':
        pass
    elif variables[2][1] == 'molecules':
        variables[2][0] /= (6.02 * 10 ^ 23)
    else:
        raise Exception('Improper unit for molecules')
variables[2][1] = 'moles'

if variables[3][0] != '?':  # temperature
    if variables[3][1] == 'K':
        pass
    elif variables[3][1] == 'C':
        variables[3][0] += 273.15
    elif variables[3][1] == 'F':
        variables[3][0] = (variables[3][0] - 32) * 5 / 9 + 273.15
    else:
        raise Exception('Improper unit for Temperature')
variables[3][1] = 'K'

print(variables)

if unknownVar == 1:  # equation for Pressure
    solution = str(variables[2][0] * gasConstant * variables[3][0] / variables[1][0]) + ' Atmospheres'
elif unknownVar == 2:  # equation for Volume
    solution = str(variables[2][0] * gasConstant * variables[3][0] / variables[0][0]) + ' Liters'
elif unknownVar == 3:  # equation for Moles
    solution = str(variables[0][0] * variables[1][0] / gasConstant / variables[3][0]) + ' Moles'
else:  # equation for Temperature
    solution = str(variables[0][0] * variables[1][0] / gasConstant / variables[2][0]) + ' Kelvin'

print(solution + ' (solution not rounded)')












