import os
def start_antivirus_win():
    print('┌Types scanning:\n│\n├ 1 = Quick scann│\n└ 2 = Full scan')
    type = input('┌ Type scan \n└ ')
    if type != '1' and type != '2' and type != '3' and type != 'back' and type != 'back':
        print('Type not found')
    else:
        if type == '1' and type == '2':
            os.system(f'cmd /c \'"%ProgramFiles%\Windows Defender\MpCmdRun.exe" -Scan -ScanType {type}\'')
        else:
            print('Scan canceled')