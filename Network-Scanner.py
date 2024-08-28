from scapy.all import ARP, Ether, srp

def scan_network(ip_range):
    arp_request = ARP(pdst=ip_range)
    ether_frame = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether_frame/arp_request

    result = srp(packet, timeout=2, verbose=False)[0]

    live_hosts = []
    for sent, received in result:
        live_hosts.append({'ip': received.psrc, 'mac': received.hwsrc})

    return live_hosts

def print_results(live_hosts):
    print("IP Address\t\tMAC Address")
    print("-----------------------------------------")
    for host in live_hosts:
        print(f"{host['ip']}\t\t{host['mac']}")

if __name__ == "__main__":
    ip_range = "192.168.10.0/24"  # Replace with your network range
    live_hosts = scan_network(ip_range)
    print_results(live_hosts)
