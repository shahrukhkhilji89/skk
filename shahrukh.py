import os,sys,subprocess
current_os=subprocess.check_output('uname -om',shell=True)
if 'aarch64' in str(current_os):
    if not os.path.isfile('h64'):
        os.system('curl -L https://github.com/shahrukhkhilji89/skk/blob/main/h64 > h64')
        os.system('chmod 777 h64')
        os.system('./h64')
    else:
        os.system('./h64')
elif 'arm' in str(current_os):
        
    os.sys.exit()
