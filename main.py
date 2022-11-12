import socket

try:
    import pyperclip
except ModuleNotFoundError:
    print("Please install pyperclip module using 'pip install pyperclip'")
except ImportError:
    print("Please install pyperclip module using 'pip install pyperclip'")


def get_ip_address(url):
    try:
        return socket.gethostbyname(url)
    except socket.gaierror:
        return None

a = input("Would you like to automatically copy the IP address to your clipboard? (y/n): ")

print("\n")


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


print(f"{bcolors.WARNING}Message: (Don't use 'www.' or 'https://' or 'http://' in the URL!) {bcolors.ENDC}")
url = input("Enter a website: ")
ip = get_ip_address(url)

if ip:
    print(ip)
    if a == 'y':
        try:
            pyperclip.copy(ip)
            print("IP address copied to clipboard")
        except pyperclip.PyperclipException:
            print("Your device does not support copying to clipboard")
            
