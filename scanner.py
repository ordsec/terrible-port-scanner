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

USAGE = "Usage: python3 scanner.py <target_ip OR hostname>, no CIDR"

######## DO THE WORK ########

# grab IP/hostname from argv
def define_target():
    # this translates hostname to IPv4
    try:
        addr = socket.gethostbyname(sys.argv[1])
        return addr
    # handle invalid hostnames
    except socket.gaierror:
        print("\nERRNO_0x00042069 (PEBKAC): The hostname doesn't seem to resolve.")
        sys.exit(1)

def scan_ports(target):
    try:
        # TODO: come up with a more flexible way to assign port ranges
        for port in range(50, 150):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # if no response, only wait for a second
            socket.setdefaulttimeout(1)
            # closed port returns 0, open port returns 1
            result = s.connect_ex((target, port))

            if result == 0:
                print(f"Port {port} is open!")
            s.close()

    # handle Ctrl+C
    except KeyboardInterrupt:
        print("\nScan aborted - an excellent decision.")
        sys.exit(0)

    # handle everything else
    except socket.error:
        print("\nERROR: there's been an error of some sort. Thanks for trying. Go use nmap.")
        sys.exit(1)

######## MAIN FUNCTION ########

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(USAGE)
        sys.exit(1)
    
    target = define_target()

    print_splash(target)

    scan_ports(target)
    