import argparse
import socket
import concurrent.futures
import nmap
import colorama
from colorama import Fore, Style

BANNER = """

 /$$$$$$                               /$$           /$$   /$$                        
|_  $$_/                              |__/          |__/  | $$                        
  | $$   /$$$$$$$   /$$$$$$  /$$   /$$ /$$  /$$$$$$$ /$$ /$$$$$$    /$$$$$$   /$$$$$$ 
  | $$  | $$__  $$ /$$__  $$| $$  | $$| $$ /$$_____/| $$|_  $$_/   /$$__  $$ /$$__  $$
  | $$  | $$  \ $$| $$  \ $$| $$  | $$| $$|  $$$$$$ | $$  | $$    | $$  \ $$| $$  \__/
  | $$  | $$  | $$| $$  | $$| $$  | $$| $$ \____  $$| $$  | $$ /$$| $$  | $$| $$      
 /$$$$$$| $$  | $$|  $$$$$$$|  $$$$$$/| $$ /$$$$$$$/| $$  |  $$$$/|  $$$$$$/| $$      
|______/|__/  |__/ \____  $$ \______/ |__/|_______/ |__/   \___/   \______/ |__/      
                        | $$                                                          
                        | $$                                                          
                        |__/                                                          
                                                                - v1.0 By Mr.KrYP70n :)

"""

colorama.init(autoreset=True)

def scan_port(target, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.1)
            result = s.connect_ex((target, port))
            if result == 0:
                print(f"{Fore.GREEN} Port {port} is open! [*]{Style.RESET_ALL}")
                try:
                    service = socket.getservbyport(port, 'tcp')
                    print(f"\t{Fore.YELLOW}Service: {service}{Style.RESET_ALL}")
                except:
                    print(f"\t{Fore.RED}Service not found{Style.RESET_ALL}")
    except:
        pass

def scan_ports_tcp(target, ports, num_threads):
    print(f"{Fore.BLUE}Scanning TCP ports on {target}...{Style.RESET_ALL}\n")
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        for port in ports:
            executor.submit(scan_port, target, port)


def scan_ports_udp(target, ports, num_threads):
    print(f"{Fore.BLUE}Scanning UDP ports on {target}...{Style.RESET_ALL}\n")
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        for port in ports:
            executor.submit(scan_port_udp, target, port)

def scan_port_udp(target, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.settimeout(0.1)
            s.sendto(b'', (target, port))
            print(f"{Fore.GREEN}Port {port}/UDP is open! [*]{Style.RESET_ALL}")
            try:
                service = socket.getservbyport(port, 'udp')
                print(f"\t{Fore.YELLOW}Service: {service}{Style.RESET_ALL}\n")
            except:
                print(f"\t{Fore.RED}Service not found{Style.RESET_ALL}")
    except:
        pass

def os_scan(target):
    print(f"{Fore.BLUE}Scanning OS on {target}...{Style.RESET_ALL}\n")
    nm = nmap.PortScanner()
    nm.scan(target, arguments='-O')
    if 'osmatch' in nm[target]:
        for osmatch in nm[target]['osmatch']:
            print(f"{Fore.GREEN}OS:{Style.RESET_ALL}  {Fore.YELLOW}{osmatch['name']} {Style.RESET_ALL} {Fore.RED}({osmatch['accuracy']}% accuracy){Style.RESET_ALL} ")

def main():
    print(BANNER)
    parser = argparse.ArgumentParser(description=f"{Fore.CYAN}A simple port scanner.\n")
    parser.add_argument("target", help="The IP address or hostname to scan.")
    parser.add_argument("-t", "--tcp", action="store_true", help="Scan TCP ports (default).")
    parser.add_argument("-u", "--udp", action="store_true", help="Scan UDP ports.")
    parser.add_argument("-p", "--ports", help="A comma-separated list of ports to scan (e.g., 22,80,443).")
    parser.add_argument("-r", "--range", help="A range of ports to scan (e.g., 1-1024).")
    parser.add_argument("-n", "--num-threads", type=int, default=10, help="The number of threads to use for scanning (default is 10).")
    parser.add_argument("-o", "--os", "--os-scan", action="store_true", help="Perform an OS scan on the target.")
    
    args = parser.parse_args()

    if not args.udp:
        args.tcp = True

    if args.ports:
        ports = list(map(int, args.ports.split(",")))
    elif args.range:
        start, end = map(int, args.range.split("-"))
        ports = list(range(start, end+1))
    else:
        ports = list(range(1, 65536))
    
    if args.tcp:
        scan_ports_tcp(args.target, ports, args.num_threads)
    
    if args.udp:
        scan_ports_udp(args.target, ports, args.num_threads)
    
    if args.os:
        os_scan(args.target)

if __name__ == "__main__":
    main()

