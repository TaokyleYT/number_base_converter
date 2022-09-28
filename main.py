import runpy
from os import system as sys, name as user
#please change the corrsponding file name if you changed them, or else error may occor
file = ['Base10.py', 'Base36.py']
while True:
    mode = input(
        'Enter 0 for max base 10(result float) method, enter 1 for max base 36(result string) method\nPlease enter method you want to use: '
    )
    try:
        int(mode)
    except:
        print('\nPlease enter a valid number\n')
    else:
        mode = int(mode)
        if mode > 1 or mode < 0:
            print('\nPlease enter a valid number\n')
        else:
            break
if user == 'nt':
    _ = sys('cls')
else:
    _ = sys('clear')
runpy.run_path(path_name=file[mode])
