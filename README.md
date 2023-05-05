# Inquisitor

Inquisitor is a fast and user-friendly port scanner written in Python. It can scan a single IP address, and it can also scan a range of ports or a specific list of ports along with the service running on the port.

![image](https://user-images.githubusercontent.com/114393219/236412176-f6c9e855-6d81-490c-9af8-5a6ed041884b.png)



## Installation

1. Clone the repository: ``git clone https://github.com/MrKrYP70n/Inquisitor.git``
2. Navigate to the project directory: ``cd Inquisitor``
3. Install the requirements: ``pip install -r requirements.txt``

## Usage

````
python3 inquisitor.py [IP] [-p PORTS or -r PORT RANGE] [-t] [-u] [-n] [-o]
````

## Arguments
  
`-h`, `--help`         :  Show the help menu  <br><br>
`[Target]`    :                     The IP address or Hostname to scan. <br><br>
`-p`, `--ports [PORTS]`    :                A comma-separated list of ports to scan (e.g., 22,80,443). <br><br>
`-r`, `--range [PORT RANGE]`    :           A range of ports to scan (e.g., 1-1024). <br><br>
`-t`, `--tcp`                           Scan TCP ports (default). <br><br>
`-u`, `--udp`                           Scan UDP ports. <br><br>
`-o`, `--os`, `--os-scan`       :       Perform an OS scan on the target. <br><br>
`-n`, `--num-threads` :                The number of threads to use for scanning (default is 10).


## Example 

````
python3 inquisitor.py 192.168.0.1 -p 22,80,443 
````

This command will scan the IP address 192.168.0.1 on ports 22, 80, and 443.

## About Me 

Hey there ! If you like this , don't forget to leave a star '⭐' . Going to add more features like IP range scanning , Port knocking , etc. :)
