import socket
import termcolor


def scan(target, port):
	print('\n' "STARTING SCAN FOR" + str(target))
	for port in range(1, port):
		scan_port(target,port)

def scan_port(ipaddress, port):
	try:
		sock = socket.socket()
		sock.connect((ipaddress, port))
		print("[+] PORT OPENED " + str(port))
		sock.close()
	except:
		pass

targets =input("[*] ENTER TARGETS (SPLIT BY COMMA [,]) TO SCAN:")
ports =int(input("[*] ENTER HOW MANY PORTS YOU WANT TO SCAN:"))

if ',' in targets:
    print(termcolor.colored(("[*] SCANNING MULTIPLE TARGETS"),'green'))
    for ip_addr in targets.split(','):
        scan(ip_addr.strip(' '),ports)
        
else:
    scan(targets,ports)
    
    




