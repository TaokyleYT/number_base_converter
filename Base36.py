from os import system as sys, name as user
#base convertion program starts here
import math
string = string = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
def _base(NotlistNum, Obase, Nbase):
  neg = False
  num = []
  NotlistNum = NotlistNum.upper()
  for digits in NotlistNum:
    corr=1
    if digits == '.':
      corr = len(num)
    else:
      num.append(string.index(digits))
  _return = []
  returnNum = 0
  ToBase10 = 0
  for Base10 in range(len(num)):
    ToBase10 = ToBase10 + num[Base10] * (Obase**Base10)
  while ToBase10 != 0:
    _return.insert(0, int((ToBase10 % Nbase) / corr))
    ToBase10 = math.floor(ToBase10 / Nbase)
  if neg:
    _return.insert(0, '-')
  for digits in _return:
    _return[_return.index(digits)]=string[string.index(str(digits))]
  if debug:
    numSaver.append("DEBUG MODE ON\n"+f"number={str(number)}, Obase={str(Obase)}, Nbase={str(Nbase)}, return={str(_return)}, neg={str(neg)}, ToBase10={str(ToBase10)}, corr={str(corr)}\nDEBUG MODE ON")
  return _return
#base convertion program ends here. Code below is the interactive section, using but not continuing the base convertion program.
numSaver=[]
def Hist():
  print('History: ')
  for printxt in numSaver:
    print(printxt)
    print('-----')
def Convert():
  global debug
  global number
  debug=False
  number=input('Input the number you want to convert: ')
  print("the largest base number this program can support is 36, please do not excceed this base number or error may occor")
  base1=int(input('Input the base of the inputted number, please input an integer: '))
  base2=int(input('Input the base you want to convert to, please input an integer: '))
  if number=='DEBUG':
    debug=True
    number=input('number?')
  tempNum=_base(number, base1, base2)
  print(tempNum)
  if not debug:
    numSaver.append(f"Inputted number: {str(number)}, inputted number's base: {str(base1)}, targeted number's base: {str(base2)}, result: {str(tempNum)}")
Convert()
cont=''
while cont!='Y' or cont!='N':
  cont=''
  cont=input("Convert another number's base? Please input Y or N, or C to clear history and convert another number's base: ")
  if user == 'nt':
    _=sys('cls')
  else:
    _=sys('clear')
  if cont=='N':
    break
  elif cont=='C':
    numSaver=[]
  elif cont=='Y':
    Hist()
  Convert()