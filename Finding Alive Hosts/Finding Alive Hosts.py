import subprocess

while True:
    network_address = input("Enter the network address or enter 'exit' to exit: ")
    if network_address == "exit":
        break
    starting_number = int(input("Enter the starting number: "))
    last_number = int(input("Enter the last number: "))
    print("Processing...")
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










