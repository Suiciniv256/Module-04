allowed_devices = ["00:11:22:33:44:55", "00:11:22:33:44:55"]

blocked_devices = ["aa:bb:cc:dd:ee:ff", "aa:bb:cc:dd:ee:ff"]

mac_address = input("Enter the device's MAC address: ")

if mac_address in allowed_devices:

      print("Access Granted")

elif mac_address in blocked_devices:

      print("Access Denied")

else:

      print("Further Authentication Required")