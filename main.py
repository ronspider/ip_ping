import datetime
import ipaddress
from ping3 import ping

subnet = '10.10.61.0/24'
output_file = 'ping_results_single.txt'

def ping_sweep(subnet):
    network = ipaddress.ip_network(subnet, strict=True)

    with open(output_file, 'a') as f:
        for ip in network.hosts():
            ip_str = str(ip)
            timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            message = ""
            try:
                response_time = ping(ip_str, timeout=1)
                if response_time is not None:
                    message = f"{timestamp} - {ip_str} is reachable"
                else:
                    message = f"{timestamp} - {ip_str} is unreachable"
            except Exception:
                message = f"{timestamp} - Error pinging {ip_str}"
            print(message)
            f.write(message + '\n')

ping_sweep(subnet)



'''
https://www.packetswitch.co.uk/how-to-ping-sweep-your-network-with-python/
https://www.freecodecamp.org/news/subnet-cheat-sheet-24-subnet-mask-30-26-27-29-and-other-ip-address-cidr-network-references/
,,,