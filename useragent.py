import random
import os
from colorama import Fore, Style, init

init(autoreset=True)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def logo():
    print(Fore.CYAN + """
██╗   ██╗ █████╗
██║   ██║██╔══██╗
██║   ██║███████║
██║   ██║██╔══██║
╚██████╔╝██║  ██║
 ╚═════╝ ╚═╝  ╚═╝
                                                           
            🚀 Ultimate User-Agent Generator v2.0          
                📱 Multi-Platform UA Tool                
                                                           

""")
    print(Fore.YELLOW + "=" * 60)
    print(Fore.GREEN + "👑 Owner: Forid | 🛡️  Professional UA Generator")
    print(Fore.MAGENTA + "💡 Use for testing, development & research purposes")
    print(Fore.YELLOW + "=" * 60 + "\n")

android_versions = ['8.1.0', '9', '10', '11', '12', '13', '14', '15']
devices = ['Samsung Galaxy S24', 'iPhone 15 Pro Max', 'Google Pixel 8', 'OnePlus 12', 
           'Xiaomi 14', 'Vivo X100', 'Oppo Find X7', 'Realme GT 5']
chrome_versions = ['122.0.6261.112', '123.0.6312.58', '124.0.6367.82', '125.0.6412.0']
fb_versions = ['465.0.0.50.120', '470.1.0.52.132', '475.0.0.60.145', '480.0.0.65.160']
ios_versions = ['17.4.1', '17.5', '18.0', '18.1']
windows_versions = ['Windows 10', 'Windows 11', 'Windows Server 2022']
mac_versions = ['macOS 14.4', 'macOS 14.5', 'macOS 15.0']

def fban_ua():
    return f"Dalvik/2.1.0 (Linux; U; Android {random.choice(android_versions)}; {random.choice(devices)} Build/{random.randint(1000, 9999)}; wv) [FBAN/FB4A;FBAV/{random.choice(fb_versions)};FBBV/{random.randint(100000000, 999999999)};FBDM/{{density=3.0,width=1080,height=2400}};FBLC/en_US;FBRV/0;FBCR/AT&T;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/{random.choice(devices).replace(' ', '')};FBSV/{random.choice(android_versions)};FBOP/1;FBCA/x86:armeabi-v7a;]"

def dalvik_ua():
    return f"Dalvik/2.1.0 (Linux; U; Android {random.choice(android_versions)}; {random.choice(devices)} Build/{random.randint(1000, 9999)}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{random.choice(chrome_versions)} Mobile Safari/537.36"

def mozilla_ua():
    device = random.choice(devices)
    if 'iPhone' in device:
        return f"Mozilla/5.0 (iPhone; CPU iPhone OS {random.choice(ios_versions).replace('.', '_')} like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/{random.choice(['17.0', '17.1', '17.2'])} Mobile/15E148 Safari/604.1"
    else:
        return f"Mozilla/5.0 (Linux; Android {random.choice(android_versions)}; {device}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.choice(chrome_versions)} Mobile Safari/537.36"

def desktop_ua():
    os_type = random.choice(['windows', 'mac', 'linux'])
    if os_type == 'windows':
        return f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.choice(chrome_versions)} Safari/537.36"
    elif os_type == 'mac':
        return f"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.choice(chrome_versions)} Safari/537.36"
    else:
        return f"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.choice(chrome_versions)} Safari/537.36"

def custom_ua():
    templates = [
        f"Instagram {random.randint(200, 300)}.0.0.{random.randint(10, 50)}.{random.randint(100, 150)} Android ({random.choice(android_versions)}/{random.randint(20, 30)}; {random.randint(240, 480)}dpi; {random.randint(1080, 1440)}x{random.randint(1920, 2560)}; {random.choice(['samsung', 'google', 'oneplus'])}; {random.choice(devices)}; {random.choice(['qcom', 'exynos'])}; en_US)",
        f"TwitterAndroid/{random.randint(9, 12)}.{random.randint(20, 90)}.{random.randint(100, 500)}-{random.choice(['release', 'debug'])} (Linux; U; Android {random.choice(android_versions)}; {random.choice(devices)} Build/{random.randint(1000, 9999)}; en_US)",
        f"Facebook/{random.choice(fb_versions)} (Linux; U; Android {random.choice(android_versions)}; {random.choice(devices)} Build/{random.randint(1000, 9999)}; Scale/{random.choice(['2.0', '2.5', '3.0'])}; {random.randint(64, 256)}dpi)",
        f"WhatsApp/{random.randint(2, 3)}.{random.randint(20, 50)}.{random.randint(1, 99)} Android/{random.choice(android_versions)} (Device: {random.choice(devices)})",
    ]
    return random.choice(templates)

def menu():
    print(Fore.CYAN + "╔" + "═" * 58 + "╗")
    print(Fore.CYAN + "║" + Fore.YELLOW + "                    MENU OPTIONS                    " + Fore.CYAN + "║")
    print(Fore.CYAN + "╠" + "═" * 58 + "╣")
    print(Fore.CYAN + "║ " + Fore.GREEN + "[1] " + Fore.WHITE + "📱 Generate FBAN User-Agent (Facebook)      " + Fore.CYAN + "║")
    print(Fore.CYAN + "║ " + Fore.GREEN + "[2] " + Fore.WHITE + "🤖 Generate Dalvik User-Agent (Android)     " + Fore.CYAN + "║")
    print(Fore.CYAN + "║ " + Fore.GREEN + "[3] " + Fore.WHITE + "🌐 Generate Mozilla User-Agent (Mobile)     " + Fore.CYAN + "║")
    print(Fore.CYAN + "║ " + Fore.GREEN + "[4] " + Fore.WHITE + "💻 Generate Desktop User-Agent              " + Fore.CYAN + "║")
    print(Fore.CYAN + "║ " + Fore.GREEN + "[5] " + Fore.WHITE + "🎯 Generate Custom App User-Agent           " + Fore.CYAN + "║")
    print(Fore.CYAN + "║ " + Fore.GREEN + "[6] " + Fore.WHITE + "♾️  Unlimited Generate (All Types)          " + Fore.CYAN + "║")
    print(Fore.CYAN + "║ " + Fore.GREEN + "[7] " + Fore.WHITE + "📊 Show Statistics & Info                  " + Fore.CYAN + "║")
    print(Fore.CYAN + "║ " + Fore.RED + "[0] " + Fore.WHITE + "🚪 Exit Program                          " + Fore.CYAN + "║")
    print(Fore.CYAN + "╚" + "═" * 58 + "╝")

def show_statistics():
    print(Fore.CYAN + "\n" + "═" * 60)
    print(Fore.YELLOW + "📊 USER-AGENT GENERATOR STATISTICS")
    print(Fore.CYAN + "═" * 60)
    print(Fore.GREEN + f"📱 Android Versions: {len(android_versions)} available")
    print(Fore.GREEN + f"📱 Devices: {len(devices)} different models")
    print(Fore.GREEN + f"🌐 Chrome Versions: {len(chrome_versions)} variations")
    print(Fore.GREEN + f"📘 Facebook Versions: {len(fb_versions)} releases")
    print(Fore.GREEN + f"🍎 iOS Versions: {len(ios_versions)} versions")
    print(Fore.MAGENTA + "\n🔄 Generation Types Available: 5")
    print(Fore.MAGENTA + "1. Facebook App Navigator (FBAN)")
    print(Fore.MAGENTA + "2. Android Dalvik Runtime")
    print(Fore.MAGENTA + "3. Mobile Mozilla Browser")
    print(Fore.MAGENTA + "4. Desktop Browsers")
    print(Fore.MAGENTA + "5. Custom App User-Agents")
    print(Fore.CYAN + "═" * 60)

def main():
    generated_count = 0
    
    while True:
        clear()
        logo()
        menu()
        
        print(Fore.YELLOW + "\n" + "─" * 60)
        choice = input(Fore.CYAN + "🎯 " + Fore.WHITE + "Select Option (0-7): " + Fore.GREEN)
        
        if choice == '1':
            print(Fore.CYAN + "\n" + "─" * 40)
            print(Fore.YELLOW + "📱 FBAN USER-AGENT GENERATED:")
            print(Fore.CYAN + "─" * 40)
            ua = fban_ua()
            print(Fore.GREEN + ua)
            generated_count += 1
            input(Fore.MAGENTA + "\n📥 Press Enter to continue...")
        
        elif choice == '2':
            print(Fore.CYAN + "\n" + "─" * 40)
            print(Fore.YELLOW + "🤖 DALVIK USER-AGENT GENERATED:")
            print(Fore.CYAN + "─" * 40)
            ua = dalvik_ua()
            print(Fore.GREEN + ua)
            generated_count += 1
            input(Fore.MAGENTA + "\n📥 Press Enter to continue...")
        
        elif choice == '3':
            print(Fore.CYAN + "\n" + "─" * 40)
            print(Fore.YELLOW + "🌐 MOZILLA USER-AGENT GENERATED:")
            print(Fore.CYAN + "─" * 40)
            ua = mozilla_ua()
            print(Fore.GREEN + ua)
            generated_count += 1
            input(Fore.MAGENTA + "\n📥 Press Enter to continue...")
        
        elif choice == '4':
            print(Fore.CYAN + "\n" + "─" * 40)
            print(Fore.YELLOW + "💻 DESKTOP USER-AGENT GENERATED:")
            print(Fore.CYAN + "─" * 40)
            ua = desktop_ua()
            print(Fore.GREEN + ua)
            generated_count += 1
            input(Fore.MAGENTA + "\n📥 Press Enter to continue...")
        
        elif choice == '5':
            print(Fore.CYAN + "\n" + "─" * 40)
            print(Fore.YELLOW + "🎯 CUSTOM APP USER-AGENT GENERATED:")
            print(Fore.CYAN + "─" * 40)
            ua = custom_ua()
            print(Fore.GREEN + ua)
            generated_count += 1
            input(Fore.MAGENTA + "\n📥 Press Enter to continue...")
        
        elif choice == '6':
            try:
                count = int(input(Fore.CYAN + "\n🎯 " + Fore.WHITE + "How many User-Agents to generate? " + Fore.GREEN))
                print(Fore.CYAN + "\n" + "═" * 60)
                print(Fore.YELLOW + f"♾️  GENERATING {count} USER-AGENTS:")
                print(Fore.CYAN + "═" * 60)
                
                for i in range(count):
                    ua_generator = random.choice([fban_ua, dalvik_ua, mozilla_ua, desktop_ua, custom_ua])
                    ua = ua_generator()
                    type_name = ua_generator.__name__.replace('_', ' ').title()
                    print(Fore.YELLOW + f"\n[{i+1}/{count}] " + Fore.CYAN + f"{type_name}:")
                    print(Fore.GREEN + ua)
                    generated_count += 1
                
                print(Fore.CYAN + "\n" + "═" * 60)
                print(Fore.GREEN + f"✅ Successfully generated {count} User-Agents!")
                print(Fore.MAGENTA + f"📈 Total generated in session: {generated_count}")
                input(Fore.CYAN + "\n📥 Press Enter to continue...")
            
            except ValueError:
                print(Fore.RED + "\n❌ Invalid input! Please enter a number.")
                input(Fore.YELLOW + "\n📥 Press Enter to continue...")
        
        elif choice == '7':
            show_statistics()
            print(Fore.MAGENTA + f"\n📊 Total User-Agents generated this session: {generated_count}")
            input(Fore.CYAN + "\n📥 Press Enter to continue...")
        
        elif choice == '0':
            clear()
            logo()
            print(Fore.RED + "\n" + "═" * 60)
            print(Fore.YELLOW + "🚪 EXITING USER-AGENT GENERATOR")
            print(Fore.CYAN + "═" * 60)
            print(Fore.GREEN + f"📊 Total User-Agents generated: {generated_count}")
            print(Fore.MAGENTA + "👑 Thank you for using Forid's UA Generator!")
            print(Fore.YELLOW + "🔒 Remember to use responsibly for legal purposes only")
            print(Fore.RED + "═" * 60 + "\n")
            break
        
        else:
            print(Fore.RED + "\n❌ Invalid option! Please select 0-7.")
            input(Fore.YELLOW + "\n📥 Press Enter to continue...")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(Fore.RED + "\n\n⚠️  Program interrupted by user. Exiting...")
    except Exception as e:
        print(Fore.RED + f"\n❌ An error occurred: {e}")