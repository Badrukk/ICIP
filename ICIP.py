import subprocess
import re
import sys

#Input
if len(sys.argv) !=2:
    print("Usage:\npython ICIP.py /path/binary\npython ICIP.py /dev/mem\npython ICIP.py /path/*")
    sys.exit(1)
file_to_run = sys.argv[1]
command = f"strings {file_to_run}"
output = subprocess.check_output(command, shell=True, text=True)


#Regex expressions
ipv4 = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
ipv4_addresses = re.findall(ipv4, output)
website = r'[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b(?:[-a-zA-Z0-9@():%_\+.~#?&\/=]*)'
website_addresses = re.findall(website, output)
mac = r'\b([0-9A-Fa-f]{2}[:-][0-9A-Fa-f]{2}[:-][0-9A-Fa-f]{2}[:-][0-9A-Fa-f]{2}[:-][0-9A-Fa-f]{2}[:-][0-9A-Fa-f]{2})\b'
mac_addresses = re.findall(mac, output)
email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
email_addresses = re.findall(email, output)

website_addresses = list(set(website_addresses) - set(ipv4_addresses))   #removes IP addresses caught by website regex
website_addresses = list(set(website_addresses) - set(email_addresses))  #removes Email addresses caught by website regex

#Output
print("IPv4 Addresses:")
for ip in ipv4_addresses:
    print(ip)
print("\nWebsites:")
for web in website_addresses:
    print(web)
print("\nMAC Addresses:")
for MAC in mac_addresses:
    print(MAC)
print("\nEmail Addresses:")
for email in email_addresses:
    print(email)
