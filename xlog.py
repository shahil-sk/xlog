
def xlog(msg,flag=None): 
    if flag == "d":
        # Color Red
        print("\033[91m {}\033[00m" .format("[#] : ")+msg)

    elif flag == "w":
        # Color Yellow
        print("\033[93m {}\033[00m" .format("[!] : ")+msg)

    elif flag == "s":
        # Color Green
        print("\033[92m {}\033[00m" .format("[^] : ")+msg)

    elif flag == "n":
        # Color Blue
        print("\033[94m {}\033[00m" .format("[*] : ")+msg)

    else:
        print("\033[97m {}\033[00m" .format("[ ] : ")+msg)
 