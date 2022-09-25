import runpy
from os import system as sys, name as user
base=['Base10.py', 'Base36.py']
while True:
  mode=input('Enter 0 for max base 10(result float) method, enter 1 for max base 36(result string and buggy) method\nHighly recommend using max base 10 for base number below 10, as value for max base 36 is likely to be wrong\nPlease enter method you want to use: ')
  try:
    int(mode)
  except:
    print('\nPlease enter a valid number\n')
  else:
    mode=int(mode)
    if mode > 1 or mode < 0:
      print('\nPlease enter a valid number\n')
    else:
      if mode == 1:
        sure=''
        while sure !='Y' or sure !='N':
          sure=input("\nAre you sure to use max base 36 method?\nThis method uses a look alike program as max base 10 method, but how it works is mostly different from the base 10 method\nSince the creator of this program doesn't have a high IQ he cannot successfully comvert the max base 10 program to max base 36, using max base 36 method will mostly result your input into a wrong convertion output\nDo you wish to continue? please enter Y or N: ")
          if sure =='Y' or sure =='N':
            if sure=='Y':
              del sure
            break
          else:
            print('\nPlease enter a valid response.')
      try:
        test=sure
      except:
        break
      else:
        pass
if user == 'nt':
  _=sys('cls')
else:
  _=sys('clear')
runpy.run_path(path_name=base[mode])