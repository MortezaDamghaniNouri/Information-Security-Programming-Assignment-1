import subprocess


while True:
    print("Enter the number of one of the following commands: ")
    print("1) Ping a specific IP address")
    print("2) Scanning a range of IP addresses and finding active hosts")
    print("3) Scanning open ports of an active host")
    print("4) Exit\n")
    user_command = input()
    if user_command == "1" or user_command == "2" or user_command == "3" or user_command == "4":
        if user_command == "4":
            break
        if user_command == "1":
            ping_input = input("Enter the IP address or the URL you want to ping: ")
            ping_result = subprocess.run("ping " + ping_input)
            print(str(ping_result) + "\n")

        if user_command == "2":
            network_address = input("Enter the network address: ")
            starting_number = int(input("Enter the starting number: "))
            last_number = int(input("Enter the last number: "))
            network_address_list = list(network_address)
            while network_address_list[len(network_address_list) - 1] != ".":
                network_address_list.pop(len(network_address_list) - 1)
            network_address = ""
            for num in network_address_list:
                network_address += num
            i = starting_number
            while i <= last_number:
                popen_result = subprocess.Popen("ping -l 8 -n 2 " + network_address + str(i), stdout=subprocess.PIPE)
                popen_data = popen_result.communicate()[0]
                return_code = popen_result.returncode
                if str(return_code) == "0":
                    print(network_address + str(i) + " " + "--> " + "Live")
                i += 1
            print("Scanning completed")









    else:
        print("Invalid input\n")























