import os
from pystyle import System, Colors, Colorate, Write
from colorama import Fore, Style
import datetime
from Tools.utils import *
import threading
import whois
import json
import subprocess
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
user = os.getlogin()
ipset = loadJip()
def clear():
    system = os.name
    if system == 'nt':
        os.system("cls")
    else:
        os.system("clear")
    return
def main():
    global ipset
    clear()
    print(Colorate.Horizontal(Colors.blue_to_purple, """
                    ██████╗ ██╗     ██╗   ██╗██████╗  █████╗ 
                    ██╔══██╗██║     ██║   ██║██╔══██╗██╔══██╗
                    ██████╔╝██║     ██║   ██║██████╔╝███████║
                    ██╔══██╗██║     ██║   ██║██╔══██╗██╔══██║
                    ██████╔╝███████╗╚██████╔╝██████╔╝██║  ██║
                    ╚═════╝ ╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝    
                    [!] Info         1.0.0         [TM] Bluba
""", 1))
    while True:
        time_rn = get_time_rn()
        print("")
        print(f"{reset}{dark}╔═[ {normal}{cyan}{time_rn} {reset}{dark}]═[ {normal}{red}BlubaConsole{reset}{dark}({reset}{lightred}{user}{reset}{dark}) ]")
        command = input(f"╚═[ {normal}{blue}{ipset} {reset}{dark}] $ ")
        print("")
        split_text = command.split(' ', 7)  # Dzieli wprowadzony tekst na 5 części
        command = split_text[0] if len(split_text) >= 1 else ''
        arg1 = split_text[1] if len(split_text) >= 2 else ''
        arg2 = split_text[2] if len(split_text) >= 3 else ''
        arg3 = split_text[3] if len(split_text) >= 4 else ''
        arg4 = split_text[4] if len(split_text) >= 5 else ''
        arg5 = split_text[5] if len(split_text) >= 6 else ''
        arg6 = split_text[6] if len(split_text) >= 7 else ''
        arg7 = split_text[7] if len(split_text) >= 8 else ''
        arg8 = split_text[8] if len(split_text) >= 9 else ''
        if command == "exit":
            print(normal)
            print(reset)
            exit()
        elif command == "!":
            info()
        elif command == "ls":
            with os.scandir() as entries:
                for entry in entries:
                    if entry.is_file():
                        print(f"File: {entry.name}")
                    elif entry.is_dir():
                        print(f"Directory: {entry.name}")
        elif command == "bat":
            if arg1 != "":
                try:
                    subprocess.run(arg1, shell=True, check=True)
                except FileNotFoundError:
                    time_rn = get_time_rn()
                    print(f"{reset}{dark}[ {normal}{cyan}{time_rn}{reset}{dark} ] ({normal}{red}-{reset}{dark}) {normal}{pretty}File not found")
        elif command == "view" or  command == "cat":
            if arg1 != "":
                with open(arg1, "r") as file:
                    temp = [line.strip() for line in file]
                for i in temp:
                    print(i)
                temp = ""
            else:
                time_rn = get_time_rn()
                print(f"{reset}{dark}[ {normal}{cyan}{time_rn}{reset}{dark} ] ({normal}{red}-{reset}{dark}) {normal}{pretty}Usage: {cyan}view <file>")
        elif command == "clear":
            if arg1 == "cache":
                ipset = "0.0.0.0"
                cache = 'Tools/cache.json'
                with open(cache, 'r') as file:
                    data = json.load(file)
                data['IP'] = "0.0.0.0"
                with open(cache, 'w') as file:
                    json.dump(data, file, indent=4)
                time_rn = get_time_rn()
                print(f"{reset}{dark}[ {normal}{cyan}{time_rn}{reset}{dark} ] ({normal}{green}+{reset}{dark}) {normal}{pretty}Cache Cleared!")
            else:
                print(normal)
                clear()
                print(Colorate.Horizontal(Colors.blue_to_purple, """
                    ██████╗ ██╗     ██╗   ██╗██████╗  █████╗ 
                    ██╔══██╗██║     ██║   ██║██╔══██╗██╔══██╗
                    ██████╔╝██║     ██║   ██║██████╔╝███████║
                    ██╔══██╗██║     ██║   ██║██╔══██╗██╔══██║
                    ██████╔╝███████╗╚██████╔╝██████╔╝██║  ██║
                    ╚═════╝ ╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝    
                    [!] Info         1.0.0         [TM] Bluba
""", 1))
        elif command == "help":
            help("all")

        #  _____ _____  
        # |_   _|  __ \ 
        #   | | | |__) |
        #   | | |  ___/ 
        #  _| |_| |     
        # |_____|_|

        elif command == "ip":

            #  ___ ___ _____ 
            #/ __| __|_   _|
            #\__ \ _|  | |  
            #|___/___| |_|  
         
            if arg1 == "set":
                if arg2 != "":
                    arg2
                    time_rn = get_time_rn()
                    print(f"{reset}{dark}[ {normal}{cyan}{time_rn}{reset}{dark} ] ({normal}{lightblue}~{reset}{dark}) {normal}{pink}Checking IP... {gray}| {green}{arg2}")
                    result = checkip(arg2)
                    if result == True:
                        time_rn = get_time_rn()
                        setJip(arg2)
                        print(f"{reset}{dark}[ {normal}{cyan}{time_rn}{reset}{dark} ] ({normal}{green}+{reset}{dark}) {normal}{pretty}New IP: {arg2}")
                        ipset = arg2
                    else: 
                        time_rn = get_time_rn()
                        print(f"{reset}{dark}[ {normal}{cyan}{time_rn}{reset}{dark} ] ({normal}{red}-{reset}{dark}) {normal}{pretty}Wrong IP")
                else:
                    time_rn = get_time_rn()
                    print(f"{reset}{dark}[ {normal}{cyan}{time_rn}{reset}{dark} ] ({normal}{red}-{reset}{dark}) {normal}{pretty}Usage: {cyan}ip set <IP Address>")
            
            #   ___ _  _ ___ ___ _  __
            #/ __| || | __/ __| |/ /
            #| (__| __ | _| (__| ' < 
            #\___|_||_|___\___|_|\_\
                         
            elif arg1 == "check":
                if arg2 != "":
                    time_rn = get_time_rn()
                    print(f"{reset}{dark}[ {normal}{cyan}{time_rn}{reset}{dark} ] ({normal}{lightblue}~{reset}{dark}) {normal}{pink}Checking IP... {gray}| {green}{arg2}")
                    result = checkip(arg2)
                    if result == True:
                        time_rn = get_time_rn()
                        print(f"{reset}{dark}[ {normal}{cyan}{time_rn}{reset}{dark} ] ({normal}{green}+{reset}{dark}) {normal}{pretty}IP {arg2} Is Working")
                    else: 
                        time_rn = get_time_rn()
                        print(f"{reset}{dark}[ {normal}{cyan}{time_rn}{reset}{dark} ] ({normal}{red}-{reset}{dark}) {normal}{pretty}IP {arg2} Is Not Working")
                else:
                    time_rn = get_time_rn()
                    print(f"{reset}{dark}[ {normal}{cyan}{time_rn}{reset}{dark} ] ({normal}{red}-{reset}{dark}) {normal}{pretty}Usage: {cyan}ip check <IP Address>")
            
            #  ___ ___ _  _  ___ ___ ___ 
            # | _ \_ _| \| |/ __| __| _ \
            # |  _/| || .` | (_ | _||   /
            # |_| |___|_|\_|\___|___|_|_\

            elif arg1 == "pinger":
                time_rn = get_time_rn()
                print(f"{reset}{dark}[ {normal}{cyan}{time_rn}{reset}{dark} ] ({normal}{lightblue}~{reset}{dark}) {normal}{pink}Pinging IP{gray}| {green}{ipset}")
                try:
                    while True:
                        result = checkip(ipset)
                        if result == True:
                            time_rn = get_time_rn()
                            print(f"{reset}{dark}[ {normal}{cyan}{time_rn}{reset}{dark} ] ({normal}{green}+{reset}{dark}) {normal}{pretty}IP {ipset} Is Working")
                        else: 
                            time_rn = get_time_rn()
                            print(f"{reset}{dark}[ {normal}{cyan}{time_rn}{reset}{dark} ] ({normal}{red}-{reset}{dark}) {normal}{pretty}IP {ipset} Is Not Working")
                        time.sleep(0.1)
                except KeyboardInterrupt:
                    print(f"{reset}{dark}[ {normal}{cyan}{time_rn}{reset}{dark} ] ({normal}{red}-{reset}{dark}) {normal}{pretty}Interrupt")

            #  _  _ __  __   _   ___ 
            # | \| |  \/  | /_\ | _ \
            # | .` | |\/| |/ _ \|  _/
            # |_|\_|_|  |_/_/ \_\_|  

            elif arg1 == "nmap":
                if arg2 == "all":
                    threads = []
                    try:
                        for port in range(1,65535):
                            thread = threading.Thread(target=scan_port, args=(ipset, port))
                            thread.start()
                            threads.append(thread)
                        for thread in threads:
                            thread.join()
                    except KeyboardInterrupt:
                        time_rn = get_time_rn()
                        print(f"{reset}{dark}[ {normal}{cyan}{time_rn}{reset}{dark} ] ({normal}{red}-{reset}{dark}) {normal}{pretty}Interrupt")
                elif arg2 =="common":
                    threads = []
                    try:
                        for port in common_ports:
                            thread = threading.Thread(target=scan_port, args=(ipset, port))
                            thread.start()
                            threads.append(thread)

                        for thread in threads:
                            thread.join()
                    except KeyboardInterrupt:
                        print(f"{reset}{dark}[ {normal}{cyan}{time_rn}{reset}{dark} ] ({normal}{red}-{reset}{dark}) {normal}{pretty}Interrupt")
                else:
                    time_rn = get_time_rn()
                    print(f"{reset}{dark}[ {normal}{cyan}{time_rn}{reset}{dark} ] ({normal}{red}-{reset}{dark}) {normal}{pretty}Usage: {cyan}ip nmap <all/common>")
            
            #  _      _   _  _ 
            # | |    /_\ | \| |
            # | |__ / _ \| .` |
            # |____/_/ \_\_|\_|

            elif arg1 == "lan":
                if arg2 == "scan":
                    if arg3 != "":
                        time_rn = get_time_rn()
                        print(f"{reset}{dark}[ {normal}{cyan}{time_rn}{reset}{dark} ] ({normal}{lightblue}~{reset}{dark}) {normal}{pink}Finding lan ip...")
                        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                        s.connect(("8.8.8.8", 80))
                        lan = s.getsockname()[0]
                        splitted_ip_digits = lan.split('.')
                        dot = '.'
                        lan = splitted_ip_digits[0] + dot + splitted_ip_digits[1] + dot + splitted_ip_digits[2] + dot
                        s.close()
                        time_rn = get_time_rn()
                        print(f"{reset}{dark}[ {normal}{cyan}{time_rn}{reset}{dark} ] ({normal}{green}+{reset}{dark}) {normal}{pretty}Lan Found {gray}| {green}{lan}")
                        time_rn = get_time_rn()
                        print(f"{reset}{dark}[ {normal}{cyan}{time_rn}{reset}{dark} ] ({normal}{lightblue}~{reset}{dark}) {normal}{pink}Scaning LAN...")
                        threads = []
                        try:
                            for i in range(1, 256):
                                ip = lan + str(i)
                                thread = threading.Thread(target=scan_ip, args=(ip,int(arg3),))
                                thread.start()
                                threads.append(thread)

                            for thread in threads:
                                thread.join()
                        except KeyboardInterrupt:
                            time_rn = get_time_rn()
                            print(f"{reset}{dark}[ {normal}{cyan}{time_rn}{reset}{dark} ] ({normal}{red}-{reset}{dark}) {normal}{pretty}Interrupt")
            else:
                help("ip")
        
        #  _____   ____  __  __          _____ _   _ 
        # |  __ \ / __ \|  \/  |   /\   |_   _| \ | |
        # | |  | | |  | | \  / |  /  \    | | |  \| |
        # | |  | | |  | | |\/| | / /\ \   | | | . ` |
        # | |__| | |__| | |  | |/ ____ \ _| |_| |\  |
        # |_____/ \____/|_|  |_/_/    \_\_____|_| \_|

        elif command == "domain":

            #  ___ ___ 
            # |_ _| _ \
            #  | ||  _/
            # |___|_|  

            if arg1 == "ip":
                if arg2 != "":
                    time_rn = get_time_rn()
                    print(f"{reset}{dark}[ {normal}{cyan}{time_rn}{reset}{dark} ] ({normal}{lightblue}~{reset}{dark}) {normal}{pink}Checking Domain {gray}| {green}{arg2}")
                    result = checkip(arg2)
                    if result == True:
                        time_rn = get_time_rn()
                        print(f"{reset}{dark}[ {normal}{cyan}{time_rn}{reset}{dark} ] ({normal}{green}+{reset}{dark}) {normal}{pretty}Domain {arg2} Is Working")
                        print(f"{reset}{dark}[ {normal}{cyan}{time_rn}{reset}{dark} ] ({normal}{lightblue}~{reset}{dark}) {normal}{pink}Checking IP {gray}| {green}{arg2}")
                        domainIp = getip(arg2)
                        print(f"{reset}{dark}[ {normal}{cyan}{time_rn}{reset}{dark} ] ({normal}{green}+{reset}{dark}) {normal}{pretty}Domain IP: {domainIp}")
                    else: 
                        time_rn = get_time_rn()
                        print(f"{reset}{dark}[ {normal}{cyan}{time_rn}{reset}{dark} ] ({normal}{red}-{reset}{dark}) {normal}{pretty}Domain {arg2} Is Invalid")
                else:
                    time_rn = get_time_rn()
                    print(f"{reset}{dark}[ {normal}{cyan}{time_rn}{reset}{dark} ] ({normal}{red}-{reset}{dark}) {normal}{pretty}Usage: {cyan}domain ip <domain>")
            
            # __      ___  _  ___ ___ ___ 
            # \ \    / / || |/ _ \_ _/ __|
            #  \ \/\/ /| __ | (_) | |\__ \
            #   \_/\_/ |_||_|\___/___|___/
                             
            elif arg1 == "whois":
                if arg2 != "":
                    time_rn = get_time_rn()
                    print(f"{reset}{dark}[ {normal}{cyan}{time_rn}{reset}{dark} ] ({normal}{lightblue}~{reset}{dark}) {normal}{pink}Checking Domain {gray}| {green}{arg2}")
                    result = checkip(arg2)
                    if result == True:
                        time_rn = get_time_rn()
                        print(f"{reset}{dark}[ {normal}{cyan}{time_rn}{reset}{dark} ] ({normal}{green}+{reset}{dark}) {normal}{pretty}Domain {arg2} Is Valid")
                        w = whois.whois(arg2)
                        c_date = format_date(w.creation_date)
                        e_date = format_date(w.expiration_date)
                        u_date = format_date(w.updated_date)
                        print(f"""
{reset}{dark}╔════[ {normal}{cyan}{arg2} {reset}{dark}]
{reset}{dark}╠═{normal}{pink}Registrar: {pretty}{w.registrar}
{reset}{dark}╠═{normal}{pink}Registrar Url: {pretty}{w.registrar_url}
{reset}{dark}╠═{normal}{pink}Registrant Name: {pretty}{w.registrant_name}
{reset}{dark}║
{reset}{dark}╠═{normal}{pink}Creation Date: {pretty}{c_date}
{reset}{dark}╠═{normal}{pink}Expiration Date: {pretty}{e_date}
{reset}{dark}╠═{normal}{pink}Updated Date: {pretty}{u_date}
{reset}{dark}╚════[ {normal}{cyan}{arg2} {reset}{dark}]
""")
                    else: 
                        time_rn = get_time_rn()
                        print(f"{reset}{dark}[ {normal}{cyan}{time_rn}{reset}{dark} ] ({normal}{red}-{reset}{dark}) {normal}{pretty}Domain {arg2} Is Invalid")
                else:
                    time_rn = get_time_rn()
                    print(f"{reset}{dark}[ {normal}{cyan}{time_rn}{reset}{dark} ] ({normal}{red}-{reset}{dark}) {normal}{pretty}Usage: {cyan}domain whois <domain>")
            else:
                help("domain")
        
        # __          ________ ____  
        # \ \        / /  ____|  _ \ 
        #  \ \  /\  / /| |__  | |_) |
        #   \ \/  \/ / |  __| |  _ < 
        #    \  /\  /  | |____| |_) |
        #     \/  \/   |______|____/ 

        elif command == "web":

            #  ___ ___ _    ___ 
            # | __|_ _| |  | __|
            # | _| | || |__| _| 
            # |_| |___|____|___|

            if arg1 == "file":
                if arg2 == "download":
                    if arg3 != "":
                        if arg4 != "":
                            time_rn = get_time_rn()
                            print(f"{reset}{dark}[ {normal}{cyan}{time_rn}{reset}{dark} ] ({normal}{lightblue}~{reset}{dark}) {normal}{pink}Checking URL {gray}| {green}{arg3}")
                            result = checkip(arg3)
                            if result == True:
                                time_rn = get_time_rn()
                                print(f"{reset}{dark}[ {normal}{cyan}{time_rn}{reset}{dark} ] ({normal}{green}+{reset}{dark}) {normal}{pretty}URL {arg3} Is Valid")
                                print(f"{reset}{dark}[ {normal}{cyan}{time_rn}{reset}{dark} ] ({normal}{lightblue}~{reset}{dark}) {normal}{pink}Downloading.. {gray}| {green}{arg3}")
                                response = requests.get(arg3)
                                open(arg4, "wb").write(response.content)
                            else: 
                                time_rn = get_time_rn()
                                print(f"{reset}{dark}[ {normal}{cyan}{time_rn}{reset}{dark} ] ({normal}{red}-{reset}{dark}) {normal}{pretty}URL {arg3} Is Invalid")
                        else:
                            time_rn = get_time_rn()
                            print(f"{reset}{dark}[ {normal}{cyan}{time_rn}{reset}{dark} ] ({normal}{red}-{reset}{dark}) {normal}{pretty}Usage: {cyan}web file download <url> <output file>")
                    else:
                        time_rn = get_time_rn()
                        print(f"{reset}{dark}[ {normal}{cyan}{time_rn}{reset}{dark} ] ({normal}{red}-{reset}{dark}) {normal}{pretty}Usage: {cyan}web file download <url> <output file>")
                else:
                    help("web")
            
            #  ___  ___   _   _  _ 
            # / __|/ __| /_\ | \| |
            # \__ \ (__ / _ \| .` |
            # |___/\___/_/ \_\_|\_|
                      
            elif arg1 == "scan":
                if arg2 != "":
                    wordlist = arg2
                    time_rn = get_time_rn()
                    print(f"{reset}{dark}[ {normal}{cyan}{time_rn}{reset}{dark} ] ({normal}{green}+{reset}{dark}) {normal}{pretty}URL {ipset} Is Valid")
                    print(f"{reset}{dark}[ {normal}{cyan}{time_rn}{reset}{dark} ] ({normal}{lightblue}~{reset}{dark}) {normal}{pink}Scaning.. {gray}| {green}{ipset}")
                    with open(wordlist) as file:
                        words = [line.strip() for line in file]
                    try:
                        for i in words:
                            response = requests.get("https://" + ipset + "/" + i)
                            if response.status_code == 200:
                                time_rn = get_time_rn()
                                print(f"{reset}{dark}[ {normal}{cyan}{time_rn}{reset}{dark} ] ({normal}{green}+{reset}{dark}) {normal}{pretty}https://{ipset}/{i} {gray}| {green}{response.status_code}")
                    except KeyboardInterrupt:
                        print(f"{reset}{dark}[ {normal}{cyan}{time_rn}{reset}{dark} ] ({normal}{red}-{reset}{dark}) {normal}{pretty}Interrupt")
            else:
                help("web")
        
        #  _____ _____  _____  _____ ____  _____  _____  
        # |  __ \_   _|/ ____|/ ____/ __ \|  __ \|  __ \ 
        # | |  | || | | (___ | |   | |  | | |__) | |  | |
        # | |  | || |  \___ \| |   | |  | |  _  /| |  | |
        # | |__| || |_ ____) | |___| |__| | | \ \| |__| |
        # |_____/_____|_____/ \_____\____/|_|  \_\_____/ 
                                                
        elif command == "discord":

            # __      _____ ___ _  _  ___   ___  _  __
            # \ \    / / __| _ ) || |/ _ \ / _ \| |/ /
            #  \ \/\/ /| _|| _ \ __ | (_) | (_) | ' < 
            #   \_/\_/ |___|___/_||_|\___/ \___/|_|\_\
            
            if arg1 == "webhook":
                if arg2 == "send":
                    if arg3 != "":
                        message = arg3
                        if arg4 != "":
                            webhook = arg4
                            respone = requests.get(webhook)
                            if respone.status_code == 200:
                                time_rn = get_time_rn()
                                print(f"{reset}{dark}[ {normal}{cyan}{time_rn}{reset}{dark} ] ({normal}{green}+{reset}{dark}) {normal}{pretty}Webhook Valid")
                                data = {
                                    "content" : message,
                                }
                                respone = requests.post(webhook, json = data)
                                if respone.status_code == 204:
                                    time_rn = get_time_rn()
                                    print(f"{reset}{dark}[ {normal}{cyan}{time_rn}{reset}{dark} ] ({normal}{green}+{reset}{dark}) {normal}{pretty}Message Sended")
                            else:
                                time_rn = get_time_rn()
                                print(f"{reset}{dark}[ {normal}{cyan}{time_rn}{reset}{dark} ] ({normal}{red}-{reset}{dark}) {normal}{pretty}Webhook Invalid")
                        else:
                            time_rn = get_time_rn()
                            print(f"{reset}{dark}[ {normal}{cyan}{time_rn}{reset}{dark} ] ({normal}{red}-{reset}{dark}) {normal}{pretty}Usage: {cyan}discord send <message> <webhook>")
                    else:
                        time_rn = get_time_rn()
                        print(f"{reset}{dark}[ {normal}{cyan}{time_rn}{reset}{dark} ] ({normal}{red}-{reset}{dark}) {normal}{pretty}Usage: {cyan}discord send <message> <webhook>")
                elif arg2 == "spam":
                    if arg3 != "":
                        message = arg3
                        if arg4 != "":
                            webhook = arg4
                            respone = requests.get(webhook)
                            if respone.status_code == 200:
                                time_rn = get_time_rn()
                                print(f"{reset}{dark}[ {normal}{cyan}{time_rn}{reset}{dark} ] ({normal}{green}+{reset}{dark}) {normal}{pretty}Webhook Valid")
                                data = {
                                    "content" : message,
                                }
                                try:
                                    while True:
                                        respone = requests.post(webhook, json = data)
                                        if respone.status_code == 204:
                                            time_rn = get_time_rn()
                                            print(f"{reset}{dark}[ {normal}{cyan}{time_rn}{reset}{dark} ] ({normal}{green}+{reset}{dark}) {normal}{pretty}Message Sended")
                                        elif respone.status_code == 429:
                                            time_rn = get_time_rn()
                                            print(f"{reset}{dark}[ {normal}{cyan}{time_rn}{reset}{dark} ] ({normal}{red}-{reset}{dark}) {normal}{pretty}Rate Limit")
                                except KeyboardInterrupt:
                                    time_rn = get_time_rn()
                                    print(f"{reset}{dark}[ {normal}{cyan}{time_rn}{reset}{dark} ] ({normal}{red}-{reset}{dark}) {normal}{pretty}Interrupt")
                            else:
                                time_rn = get_time_rn()
                                print(f"{reset}{dark}[ {normal}{cyan}{time_rn}{reset}{dark} ] ({normal}{red}-{reset}{dark}) {normal}{pretty}Webhook Invalid")
                        else:
                            time_rn = get_time_rn()
                            print(f"{reset}{dark}[ {normal}{cyan}{time_rn}{reset}{dark} ] ({normal}{red}-{reset}{dark}) {normal}{pretty}Usage: {cyan}discord send <message> <webhook>")
                    else:
                        time_rn = get_time_rn()
                        print(f"{reset}{dark}[ {normal}{cyan}{time_rn}{reset}{dark} ] ({normal}{red}-{reset}{dark}) {normal}{pretty}Usage: {cyan}discord send <message> <webhook>")
                elif arg2 == "delete":
                    if arg3 != "":
                        respone = requests.delete(arg3)
                        if respone.status_code == 204:
                            time_rn = get_time_rn()
                            print(f"{reset}{dark}[ {normal}{cyan}{time_rn}{reset}{dark} ] ({normal}{green}+{reset}{dark}) {normal}{pretty}Webhook Deleted")
                        else:
                            time_rn = get_time_rn()
                            print(f"{reset}{dark}[ {normal}{cyan}{time_rn}{reset}{dark} ] ({normal}{red}-{reset}{dark}) {normal}{pretty}Invalid Webhook")
                    else:
                        time_rn = get_time_rn()
                        print(f"{reset}{dark}[ {normal}{cyan}{time_rn}{reset}{dark} ] ({normal}{red}-{reset}{dark}) {normal}{pretty}Usage: {cyan}discord delete <webhook>")
                elif arg2 == "check":
                    if arg3 != "":
                        respone = requests.get(arg3)
                        if respone.status_code == 200:
                            time_rn = get_time_rn()
                            print(f"{reset}{dark}[ {normal}{cyan}{time_rn}{reset}{dark} ] ({normal}{green}+{reset}{dark}) {normal}{pretty}Webhook Valid")
                        elif respone.status_code == 404:
                            time_rn = get_time_rn()
                            print(f"{reset}{dark}[ {normal}{cyan}{time_rn}{reset}{dark} ] ({normal}{red}-{reset}{dark}) {normal}{pretty}Invalid Webhook")
                    else:
                        time_rn = get_time_rn()
                        print(f"{reset}{dark}[ {normal}{cyan}{time_rn}{reset}{dark} ] ({normal}{red}-{reset}{dark}) {normal}{pretty}Usage: {cyan}discord check <webhook>")
                else:
                    help("discord")
            else:
                help("discord")

        else:
            help("all")

    print(normal)
main()
