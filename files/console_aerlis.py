import os, sys, time, random, colorama, starter_antivirus
colorama.init()
cmd_get = 'c o m m a n d '

#┌ └  \n│\n├ 

while 1:
    cm = input(f'┌ {cmd_get}\n└ @ ')
    if cm == 'exit' or cm == 'end':
        sys.exit(1)
    elif cm == 'cls' or cm == 'clear':
        os.system('cls || clear')
    elif cm == 'scan' or cm == 'start.antivirus':
        if sys.platform == 'win32':
            starter_antivirus.start_antivirus_win()
        else:
            print('This function worked only windows 10 or 11.')
    else:
        print('Error command "'+cm+'" not found\n')