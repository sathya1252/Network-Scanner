# Netwrok-Scanner
This project is a simple network scanner implemented in Python using the Scapy library. It performs a network discovery scan to identify live hosts within a specified IP range by sending ARP requests. The scanner can detect devices on the local network, displaying their IP and MAC addresses.

Features:

  -> Network Discovery: Scans a given IP range to find live hosts.
  
  -> ARP Requests: Utilizes ARP to identify devices on the local network.
  
  -> MAC Address Detection: Retrieves and displays the MAC addresses of detected devices.
  
  -> Simple Output: Provides a straightforward tabular output of live hosts.
  

Requirements:

  Python 3.x
  Scapy

Installation:

Clone the repository:

    git clone https://github.com/sathya1252/network-scanner.git
    
    cd network-scanner

Install the required dependencies:

    pip install scapy

Usage:

Edit the ip_range variable in network_scanner.py to specify the network range you want to scan:

    ip_range = "192.168.1.0/24"  # Replace with your network range

Run the script with Python:

    python3 network_scanner.py

View the list of live hosts and their MAC addresses in the output.
