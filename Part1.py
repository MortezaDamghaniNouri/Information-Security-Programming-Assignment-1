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










    else:
        print("Invalid input\n")























