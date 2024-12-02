
def xPrint(msg,flag=None): 
    if flag == "danger":
        # Color Red
        print("\033[91m {}\033[00m" .format("[!] Danger  : ")+msg)

    elif flag == "warn":
        # Color Yellow
        print("\033[93m {}\033[00m" .format("[!] Warning : ")+msg)

    elif flag == "success":
        # Color Green
        print("\033[92m {}\033[00m" .format("[!] Success : ")+msg)

    elif flag == "note":
        # Color Blue
        print("\033[94m {}\033[00m" .format("[!] Note    : ")+msg)

    else:
        print("\033[97m {}\033[00m" .format("[!] Log     : ")+msg)
 