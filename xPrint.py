
def xPrint(msg,flag=None): 
    if flag == "danger":
        print("\033[91m {}\033[00m" .format("[!] Danger  : ")+msg)
    elif flag == "warn":
        print("\033[93m {}\033[00m" .format("[!] Warning : ")+msg)
    elif flag == "success":
        print("\033[92m {}\033[00m" .format("[!] Success : ")+msg)
    elif flag == "note":
        print("\033[94m {}\033[00m" .format("[!] Note    : ")+msg)
    else:
        print("\033[97m {}\033[00m" .format("[!] Log     : ")+msg)
 

xPrint("Testing","danger")
xPrint("Testing","warn")
xPrint("Testing","success")
xPrint("Testing","note")
xPrint("Testing")