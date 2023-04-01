import sys
import socket
from datetime import datetime

######## UI ########

def print_splash(target):
    print("\n")
    print("~" * 50)
    print("Welcome to the terrible port scanner!")
    print("(Really, this is embarrassing, just use nmap.)")
    print("\n")
    print("The time is: " + str(datetime.now()))
    print("Scanning target: " + target)
    print("~" * 50)

USAGE = "Usage: python3 scanner.py <target_ip>, no CIDR"

######## DO THE WORK ########

# grab target IP from argv
def define_target():
    # this translates hostname to IPv4
    target = socket.gethostname(sys.argv[1])
    return target

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(USAGE)
        sys.exit(1)
    
    # target = define_target()
    print_splash(sys.argv[1])
    