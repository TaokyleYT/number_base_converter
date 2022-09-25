from os import system as sys, name as user
#base convertion program starts here
import math
def _base(num, Obase, Nbase):
  neg=False
  if num<0:
    neg=True
    num=num*-1
  corr=10**(len(str(num))-len(str(math.floor(num))))
  num=num*corr
  length=len(str(num))
  _return=[]
  returnNum=0
  ToBase10=0
  for Base10 in range(length):
    ToBase10=ToBase10+(num // 10**Base10%10)*(Obase**Base10)
  while ToBase10!=0:
    _return.append(ToBase10%Nbase)
    ToBase10=math.floor(ToBase10/Nbase)
  for digits in range(len(_return)):
    returnNum=returnNum+(_return[digits]*(10**digits))
  if neg:
    returnNum=returnNum/corr*-1
  else:
    returnNum=returnNum/corr
  if debug:
    numSaver.append("DEBUG MODE ON\n"+f"number={str(number)}, Obase={str(Obase)}, Nbase={str(Nbase)}, return={str(returnNum)}, _return={str(_return)}, neg={str(neg)}, ToBase10={str(ToBase10)}, corr={str(corr)}\nDEBUG MODE ON")
  return returnNum
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
  number=input('Input the number you want to convert, base above 10 is not being supported so far so please input a number: ')
  base1=int(input('Input the base of the inputted number, please input an integer: '))
  base2=int(input('Input the base you want to convert to, please input an integer: '))
  if number=='DEBUG':
    debug=True
    number=input('number?')
  if number.find('.')!=-1:
    tempNum=_base(float(number), base1, base2)
  else:
    tempNum=_base(int(number), base1, base2)
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