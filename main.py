import scapy.all as scapy
import argparse

""""
def get_args():
    options = argparse.ArgumentParser()
    options.add_argument(dest='target_ip')
    options.add_argument('-p', '--port', dest='port', help='Port to scan')
    opts = options.parse_args()

    if not opts.target_ip:
        options.error("No target specified, please specify the IP address of a target, use --help for more info")

    return opts


args = get_args()
"""


def scan_ip(ip):
    ans = scapy.ARP(pdst="192.168.1.1")
    print(ans)


def main():
    scan_ip(10)#args.target_ip)


if __name__ == '__main__':
    main()

# options = OptionParser(usage='%prog server [options]', description='Test and exploit TLS heartbeat vulnerability aka heartbleed (CVE-2014-0160)')
# options.add_option('-p', '--port', type='int', default=443, help='TCP port to test (default: 443)')
