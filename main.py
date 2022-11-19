import scapy.all as scapy
import argparse


def get_args():
    options = argparse.ArgumentParser()
    options.add_argument(dest='target_ip')
    opts = options.parse_args()

    if not opts.target_ip:
        options.error("No target specified, please specify the IP address of a target, use --help for more info")

    return opts


def scan_ip(ip):
    arp_req_frame = scapy.ARP(pdst=ip)
    broadcast_frame = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    broadcast_arp_req_frame = broadcast_frame / arp_req_frame
    hosts_list = scapy.srp(broadcast_arp_req_frame, timeout=2, verbose=False)[0]
    table_with_ip = []
    for i in range(0, len(hosts_list)):
        client_dict = {"ip": hosts_list[i][1].psrc, "mac": hosts_list[i][1].hwsrc}
        table_with_ip.append(client_dict)

    print(table_with_ip)


def main():
    args = get_args()
    scan_ip(args.target_ip)


if __name__ == '__main__':
    main()
