import os, sys, platform,time
 
bit = platform.architecture()[0]
if bit == '64bit':
    os.system('clear')
    os.system('git pull')
    import FILE64    
elif bit == '32bit':
    os.system('clear')
    os.system('git pull')
    import FILE32
