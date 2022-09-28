from os import system as sys, name as user
#base convertion program starts here
import string

symbols = string.digits + string.ascii_uppercase


def intToBases(num, Nbase):
    global sign
    global ans
    global returntxt1
    sign = -1 if num < 0 else 1
    num *= sign
    ans = ''
    while num:
        ans += symbols[num % Nbase]
        num //= Nbase
    if sign == -1:
        ans += '-'
    returntxt1 = ans[::-1]
    return returntxt1


def convert(num, Obase, Nbase, corr=None):
    num=num.replace(' ', '')
    inti, pt, fra = num.strip().partition('.')
    num1 = int(inti + fra, Obase) * Obase**-len(fra)
    corr = len(fra) if corr is None else corr
    s = intToBases(int(round(num1 / Nbase**-corr)), Nbase)
    if corr:
        returntxt = s[:-corr] + '.' + s[-corr:]
    else:
        returntxt = s
    if debug:
        numSaver.append(
            f"DEBUG MODE ON\nnumber={str(num)}, Obase={str(Obase)}, Nbase={str(Nbase)}, return={str(returntxt)}, num1={str(num1)}, int={str(inti)}, corr={str(corr)}, pt={str(pt)}, fra={str(fra)}\nHelperDefVarData\nsign={str(sign)}, ans={str(ans)}, returntxt1={str(returntxt1)}\nDEBUG MODE ON"
        )
    return returntxt


numSaver = []


def Hist():
    print('History: ')
    for printxt in numSaver:
        print(printxt)
        print('-----')
def ConProg():
    global debug
    global number
    debug = False
    number = input('Input the number you want to convert: ')
    print(
        "the smallest base number this program can support is 2 and the largest base number this program can support is 36, please do not excceed base number 36 or under base number 2, or error may occor"
    )
    base1 = int(
        input(
            'Input the base of the inputted number, please input an integer: ')
    )
    base2 = int(
        input(
            'Input the base you want to convert to, please input an integer: ')
    )
    if number == 'DEBUG':
        debug = True
        number = input('number?')
    tempNum = convert(number, base1, base2)
    print(tempNum)
    if not debug:
        numSaver.append(
            f"Inputted number: {str(number)}, inputted number's base: {str(base1)}, targeted number's base: {str(base2)}, result: {str(tempNum)}"
        )
ConProg()
cont = ''
while cont != 'Y' or cont != 'N' or cont!='C':
    cont = ''
    cont = input(
        "Convert another number's base? Please input Y or N, or C to clear history and convert another number's base: "
    )
    if cont == 'N':
        break
    elif cont == 'C':
        numSaver = []
        if user == 'nt':
          _ = sys('cls')
        else:
          _ = sys('clear')
        ConProg()
    elif cont == 'Y':
        if user == 'nt':
          _ = sys('cls')
        else:
          _ = sys('clear')
        Hist()
        ConProg()
    else:
        print('\nPlease enter a valid response\n')
