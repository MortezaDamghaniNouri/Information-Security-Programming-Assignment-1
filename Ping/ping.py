import subprocess
while True:
    ping_input = input("Enter the IP address or the URL you want to ping or enter 'exit' to exit: ")
    if ping_input == "exit":
        break
    ping_result = subprocess.run("ping " + ping_input)
    print(str(ping_result) + "\n")













