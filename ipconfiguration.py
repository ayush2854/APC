server_ip = ("192.168.1.1",)  
allowed_ips = ["192.168.1.2", "192.168.1.3"]  

def update_allowed_ips(action, ip):
    if action == "add":
        if ip not in allowed_ips:
            allowed_ips.append(ip)
            print(f"IP {ip} added to allowed list.")
        else:
            print(f"IP {ip} is already allowed.")
    elif action == "remove":
        if ip in allowed_ips:
            allowed_ips.remove(ip)
            print(f"IP {ip} removed from allowed list.")
        else:
            print(f"IP {ip} not found in allowed list.")
    else:
        print("Invalid action. Use 'add' or 'remove'.")

def show_configuration():
    print("\n--- Server Configuration ---")
    print(f"Server IP (unchangeable): {server_ip[0]}")
    print(f"Allowed IPs: {allowed_ips}")

# Main program loop
while True:
    print("\n--- Web Server Configuration Menu ---")
    print("1. Add Allowed IP")
    print("2. Remove Allowed IP")
    print("3. Show Configuration")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        ip = input("Enter IP to allow: ")
        update_allowed_ips("add", ip)

    elif choice == "2":
        ip = input("Enter IP to remove: ")
        update_allowed_ips("remove", ip)

    elif choice == "3":
        show_configuration()

    elif choice == "4":
        print("Exiting...")
        break

    else:
        print("Invalid choice. Try again.")