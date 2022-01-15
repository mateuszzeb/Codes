import ipaddress
import socket

ports = [
    80, 
    443,
]

ip_address = '127.0.0.0'



def is_port_open(ip: int, port: int) -> bool:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(2)
    result = sock.connect_ex((ip, port))
    sock.close()
    return result == 0



for ip in ipaddress.ip_network(f'{ip_address}/24'):
    print(f'IP: {ip}')
    for port in ports:
        if is_port_open(str(ip), port):
            print(f" >>> {ip}:{port} is open")
