import sys
import socket
import argparse
import threading

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

def scan_port(target, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.1)
        s.connect((target, port))
        print(f"Port {port}/TCP is open")
        try:
            service = socket.getservbyport(port, 'tcp')
            print(f"\tService: {service}")
        except:
            pass
    except:
        pass
    finally:
        s.close()

def scan_ports_tcp(target, ports):
    print(f"Scanning TCP ports on {target}...\n")
    for port in ports:
        threading.Thread(target=scan_port, args=(target, port)).start()

def scan_ports_udp(target, ports):
    print(f"Scanning UDP ports on {target}...\n")
    for port in ports:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.settimeout(0.1)
            s.sendto(b'', (target, port))
            print(f"Port {port}/UDP is open")
            try:
                service = socket.getservbyport(port, 'udp')
                print(f"\tService: {service}")
            except:
                pass
        except:
            pass
        finally:
            s.close()

def main():
    print(BANNER)
    parser = argparse.ArgumentParser(description="A simple port scanner.")
    parser.add_argument("ip", help="The IP address to scan.")
    parser.add_argument("-t", "--tcp", action="store_true", help="Scan TCP ports (default).")
    parser.add_argument("-u", "--udp", action="store_true", help="Scan UDP ports.")
    parser.add_argument("-p", "--ports", help="A comma-separated list of ports to scan (e.g., 22,80,443).")
    parser.add_argument("-r", "--range", help="A range of ports to scan (e.g., 1-1024).")
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
        scan_ports_tcp(args.ip, ports)

    if args.udp:
        scan_ports_udp(args.ip, ports)

if __name__ == "__main__":
    main()
