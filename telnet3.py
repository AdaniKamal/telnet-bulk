import socket
import sys

def check_port(ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(5)
            result = sock.connect_ex((ip, port))
            return result == 0  # Returns True if the port is open
    except:
        return False

def main(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                parts = line.split()
                ip = parts[-1]
                ports = parts[0].split(',')

                for port in ports:
                    port = port.strip()
                    if not port.isdigit():
                        continue
                    result = check_port(ip, int(port))
                    status = "\033[32mPort Open\033[0m" if result else "\033[31mPort Close\033[0m"
                    print(f"Hosts: {ip}")
                    print(f"Port: {port}")
                    print(f"Telnet: {status}")
                    print()  # Add a blank line for better readability
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python telnet.py hosts-ip.txt")
    else:
        main(sys.argv[1])
