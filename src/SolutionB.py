import sys
import decimal

def asterix(rest, result):
    for index, y in enumerate(rest):

        if (y == 'L'):
            result = result * decimal.Decimal('2')
        elif (y == 'R'):
            result = result * decimal.Decimal('2') + decimal.Decimal('1')
        elif (y == '*'):
            temp = ""

            if (index + 1 <= len(rest)):
                temp = rest [(index + 1):]
                result = asterix(temp, result * decimal.Decimal('2')) + asterix(temp, result * decimal.Decimal('2') + decimal.Decimal('1')) + asterix(temp, result)
            else:
                result = decimal.Decimal('5') * result + decimal.Decimal('1')
            break
    return result
    
for lin in sys.stdin:
    print (asterix(lin, decimal.Decimal('1')))


