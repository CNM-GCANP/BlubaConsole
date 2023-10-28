from pystyle import System, Colors, Colorate, Write
from colorama import Fore, Style
import socket
import ping3
import requests
import random
import json
import datetime
import subprocess
import os
import time
def get_time_rn():
    date = datetime.datetime.now()
    hour = date.hour
    minute = date.minute
    second = date.second
    timee = "{:02d}:{:02d}:{:02d}".format(hour, minute, second)
    return timee
common_ports = [21, 22, 25, 53, 67, 68, 69, 79, 80, 110, 113, 123, 143, 443, 465, 587, 993, 995, 2002, 3300, 3306, 4000, 4002, 5000, 5002, 5003, 14147, 25565]
red = Fore.RED
lightred = Fore.LIGHTRED_EX
yellow = Fore.YELLOW
green = Fore.GREEN
blue = Fore.BLUE
orange = Fore.RED + Fore.YELLOW
pretty = Fore.LIGHTMAGENTA_EX + Fore.LIGHTCYAN_EX
magenta = Fore.MAGENTA
lightblue = Fore.LIGHTBLUE_EX
cyan = Fore.CYAN
gray = Fore.LIGHTBLACK_EX + Fore.WHITE
reset = Fore.RESET + Style.NORMAL
pink = Fore.LIGHTGREEN_EX + Fore.LIGHTMAGENTA_EX
dark_green = Fore.GREEN + Style.BRIGHT
dark = Style.DIM
normal = Style.NORMAL
def format_date(date):
    return date.strftime('%Y-%m-%d %H:%M:%S %Z') if date else "N/A"

def checkip(adres_ip):
    czas_odpowiedzi = ping3.ping(adres_ip)
    if czas_odpowiedzi is not None:
        return True
    else:
        return False
def help(w):
    if w == "all":
        help("ip")
        help("domain")
        help("web")
        help("discord")
    elif w == "ip":
        print("""
ip set <ip address/url> - change your target ip
ip check <ip address/url> - check ip
ip pinger - pings ip
ip nmap <all/common> - nmap scan
ip lan scan <port> - scans lan network for open port
    """)
    elif w == "domain":
        print("""
domain ip <domain> - get domain ip
domain whois <domain> - whois domain
    """)
    elif w == "web":
        print("""
web file download <url> <output file> - downloads file from url
web scan <wordlist> - something like gobuster (uses your cached ip)
    """)
    elif w == "discord":
        print("""
discord webhook send <message> <webhook> - sends message to webhhok
discord webhook send <message> <webhook> - spams message to webhhok
discord check <webhook> - checks if webhook is valid
discord delete <webhook> - deletes webhook
    """)
        
def getip(domain):
    temp = socket.gethostbyname(domain)
    return temp

def stress(ip):
    while True:
        result = requests.get("http://"+ip)
        print(result.status_code)
def scan_port(ip, port):
    try:
        tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if not tcp.connect_ex((ip, port)):
            time_rn = get_time_rn()
            print(f'{reset}{dark}[ {normal}{cyan}{time_rn}{reset}{dark} ] ({normal}{green}+{reset}{dark}) {normal}{pretty}%s:%d/TCP Open' % (ip, port))
        tcp.close()
    except Exception:
        pass
def find(port):
    while True:
        ip_parts = [str(random.randint(0, 255)) for _ in range(4)]
        ip = ".".join(ip_parts)
        try:
            tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            print(ip)
            if not tcp.connect_ex((ip, port)):
                print('[+] %s:%d/TCP Open' % (ip, port))
            tcp.close()
        except Exception as e:
            pass
def loadJip():
    cache = 'Tools/cache.json'
    with open(cache, 'r') as file:
        data = json.load(file)
    return data['IP']
def setJip(ip):
    cache = 'Tools/cache.json'
    with open(cache, 'r') as file:
        data = json.load(file)
    data['IP'] = ip
    with open(cache, 'w') as file:
        json.dump(data, file, indent=4)
def scan_ip(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    result = sock.connect_ex((ip, port))
    if result == 0:
        time_rn = get_time_rn()
        print(f"{reset}{dark}[ {normal}{cyan}{time_rn}{reset}{dark} ] ({normal}{green}+{reset}{dark}) {normal}{pretty}IP Found: {cyan}{ip}")
    else:
        return 0
def info():
    print(f"""
{reset}{dark}╔════[ {normal}{cyan}BlubaConsole{reset}{dark}]
{reset}{dark}╠═{normal}{pink}Author: {pretty}gigachadaniepizda1
{reset}{dark}╠═{normal}{pink}Github: {pretty}https://github.com/CNM-GCANP
{reset}{dark}╠═{normal}{pink}Project Github: {pretty}https://github.com/CNM-GCANP/BlubaConsole
{reset}{dark}╠═{normal}{pink}BIO: {pretty}https://guns.lol/nyga
{reset}{dark}╚════[ {normal}{cyan}BlubaConsole {reset}{dark}]
""")
