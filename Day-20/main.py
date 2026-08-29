import sys
import urllib.request
import urllib.parse
import re
import os
from colorama import Fore, Style, init

# Inisialisasi Colorama
init(autoreset=True)

os.system('clear')

print(Fore.GREEN + """
 █████╗ ██╗     ███████╗██╗  ██╗
██╔══██╗██║     ╚══███╔╝██║  ██║
███████║██║       ███╔╝ ███████║
██╔══██║██║      ███╔╝  ██╔══██║
██║  ██║███████╗███████╗██║  ██║
╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝

███████╗██╗   ██╗██████╗ ██╗  ██╗██╗   ██╗███╗   ██╗████████╗███████╗██████╗
██╔════╝██║   ██║██╔══██╗██║  ██║██║   ██║████╗  ██║╚══██╔══╝██╔════╝██╔══██╗
███████╗██║   ██║██████╔╝███████║██║   ██║██╔██╗ ██║   ██║   █████╗  ██████╔╝
╚════██║██║   ██║██╔══██╗██╔══██║██║   ██║██║╚██╗██║   ██║   ██╔══╝  ██╔══██╗
███████║╚██████╔╝██████╔╝██║  ██║╚██████╔╝██║ ╚████║   ██║   ███████╗██║  ██║
╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝   ╚═╝   ╚══════╝╚═╝  ╚═╝

""")

domain = input(Fore.YELLOW + "Masukkan Domain Yang Ingin Anda Periksa: ")

print(Fore.CYAN + "Scanning Subdomain For", domain)

for i, arg in enumerate(sys.argv, 1):
    domains = set()
    with urllib.request.urlopen('https://crt.sh/?q=' + urllib.parse.quote('%.' + domain)) as r:
        code = r.read().decode('utf-8')
        for cert, domain in re.findall(
                '<tr>(?:\s|\S)*?href="\?id=([0-9]+?)"(?:\s|\S)*?<td>([*_a-zA-Z0-9.-]+?\.' + re.escape(domain) + ')</td>(?:\s|\S)*?</tr>',
                code, re.IGNORECASE):
            domain = domain.split('@')[-1]
            if not domain in domains:
                domains.add(domain)
                print(Fore.GREEN + domain)

# Mengembalikan warna ke normal setelah selesai
print(Style.RESET_ALL)