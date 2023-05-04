# Inquisitor

Inquisitor is a fast and user-friendly port scanner written in Python. It can scan a single IP address, and it can also scan a range of ports or a specific list of ports along with the service running on the port.

Inquisitor Screenshot
![image](https://user-images.githubusercontent.com/114393219/236293500-1a72a289-1cb6-4725-aafe-78748d52b627.png)


## Installation

1. Clone the repository: ``git clone https://github.com/MrKrYP70n/Inquisitor.git``
2. Navigate to the project directory: ``cd Inquisitor``
3. Install the requirements: ``pip install -r requirements.txt``

## Usage

````
python3 inquisitor.py [IP] [-p PORTS or -r PORT RANGE] [-t] [-u]
````

## Arguments
  
`-h`, `--help`         :  Show the help menu  <br><br>
`[IP]`    :                     The IP address to scan. <br><br>
`-p`, `--ports [PORTS]`    :                A comma-separated list of ports to scan (e.g., 22,80,443). <br><br>
`-r`, `--range [PORT RANGE]`    :           A range of ports to scan (e.g., 1-1024). <br><br>
`-t`, `--tcp`                           Scan TCP ports (default). <br><br>
`-u`, `--udp`                           Scan UDP ports. <br><br>

## Example 

````
python3 inquisitor.py 192.168.0.1 -p 22,80,443 
````

This command will scan the IP address 192.168.0.1 on ports 22, 80, and 443.

## About Me 

Hey there ! If you like this , don't forget to leave a star '⭐' . Going to add more features like IP range scanning , Port knocking , etc. :)
