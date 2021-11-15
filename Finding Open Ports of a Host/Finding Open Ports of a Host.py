import nmap

host_ip = input("Enter the host IP you want to scan its ports: ")
start_port_number = input("Enter the start port number: ")
last_port_number = input("Enter the last port number: ")
print("Processing...")
nm = nmap.PortScanner()
nm.scan(host_ip, start_port_number + "-" + last_port_number)
for host in nm.all_hosts():
    print('----------------------------------------------------')
    for proto in nm[host].all_protocols():
        print('----------')
        print("Protocol: " + str(proto))
        ports_list = nm[host][proto].keys()
        for port in ports_list:
            print('Port : %s\tState : %s' % (port, nm[host][proto][port]['state']))
print("Ports scanning completed")

























