class bcolors:
    #source for colours
    #https://stackoverflow.com/questions/287871/how-do-i-print-colored-text-to-the-terminal 
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    BLINK = '\033[6m'

def output(message, level="info"):
    #set-up the header that will be added to each message
    timestamp_now = datetime.now(UTC)
    formatted_time = timestamp_now.strftime("%H:%M:%S")
    header = f"{bcolors.ENDC}[{bcolors.HEADER}{formatted_time}{bcolors.ENDC}] "

    #different colours get used depending on level inputted
    match level:
        case "info":
            header_level = f"{bcolors.ENDC}[{bcolors.OKGREEN}INFO{bcolors.ENDC}] "
            print(f"{header}{header_level}{bcolors.ENDC}{message}")
