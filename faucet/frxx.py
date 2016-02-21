import requests
import urllib
import json
import sys
import subprocess
import time
from datetime import datetime
from secure_s0lvemedia import S0LVEMEDIA
from bs4 import BeautifulSoup

class FRXX:
    k = 'xx5szIz9haroDwT2alQdXZvD-dgNdDxx'
    password = ''
    hash_password = ''
    def get_session(self):
        url = 'https://frxxb!tco.in/' 
        get_response = requests.get(url, verify=False, timeout=20)
        self.cfduid = get_response.cookies['__cfduid']
        self.token = get_response.cookies['csrf_token']

    def get_password(self, mwin, address):
        url = 'https://frxxb!tco.in/' 
        try:
            headers = {'Cookie': '__cfduid=' + self.cfduid + '; csrf_token=' + self.token +';',
             'Content-Type': 'application/x-www-form-urlencoded', 'x-csrf-token': self.token}
            post_data = {'op': 'login', 'btc_address': address, 'password': self.password}
            session = requests.Session()
            post_response = session.post(url, data=urllib.urlencode(post_data), headers=headers, verify=False, timeout=20)
            self.hash_password = post_response.content.split(":")[2]
            return True
        except:
            self.write_log(mwin, 'Login failed.')
            return False

    def get_login(self, mwin, address):
        url = 'https://frxxb!tco.in/'
        try:
            headers = {'Cookie': '__cfduid=' + self.cfduid + '; csrf_token=' + self.token +'; btc_address=' + address + '; password=' + self.hash_password + '; have_account=1;',
            'Content-Type': 'application/x-www-form-urlencoded'}
            get_response = requests.get(url, headers=headers, verify=False, timeout=20)
            self.token = get_response.cookies['csrf_token']
            soup = BeautifulSoup(get_response.text)
            self.seed = str(soup.select('#next_client_seed')[0].get('value'))
            self.ran1 = get_response.content.split(' op:op, ')[1].split(':')[0]
            self.ran2 = get_response.content.split('$("#%s").val("' %self.ran1)[1].split('"')[0]
            self.ran3 = get_response.content.split('adcopy_response:adcopy_response, ')[1].split(':')[0]
            if ";});title_countdown (" in get_response.content:
                time = get_response.content.split(';});title_countdown (')[1].split(')')[0]
                self.write_log(mwin, 'Not yet. Wait %s seconds before you can play for frxx again.' %time)
                return False
            return True
        except:
            self.write_log(mwin, 'Login failed.')
            return False

    def get_start(self, mwin, address):
        self.get_session()
        login = self.get_password(mwin, address)
        if login == True:
            claim = self.get_login(mwin, address)
            if claim == True:
                sm = S0LVEMEDIA()
                (ckey, magic, stamp) = sm.get_captcha_info(self.k)
                (self.c, uid) = sm.get_captcha_image(ckey, magic, stamp, "frxx")
                return True
        return False
        
    def post_summit_captcha(self, mwin, address, captcha):
        url = 'https://frxxb!tco.in/'
        headers = {'Cookie': '__cfduid=' + self.cfduid + '; csrf_token=' + self.token +'; btc_address=' + address + '; password=' + self.hash_password + '; have_account=1;',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:35.0) Gecko/20100101 Firefox/35.0',
        'Content-Type': 'application/x-www-form-urlencoded',
        'x-csrf-token': self.token}
        fingerprint = 'e9c6ef0537b47aac3ae98d576776155b'
        fingerprint2 = '1852803562'
        post_data = {'op': 'frxx_play',
        'adcopy_response': captcha, 'adcopy_challenge': self.c,
        'recaptcha_response_field': '', 'recaptcha_challenge_field': '',
        self.ran1: self.ran2, self.ran3: '2',
        'fingerprint': fingerprint, 'fingerprint2': fingerprint2, 'client_seed': self.seed}
        session = requests.Session()
        post_response = session.post(url, data=urllib.urlencode(post_data), headers=headers, verify=False, timeout=20)
        if len(post_response.content) > 20:
            total = post_response.content.split(':')[2]
            money = post_response.content.split(':')[3]
            total = str(int(float(total)*100000000))
            money = str(int(float(money)*100000000))
            self.write_log(mwin, "You get %s satoshi. Now you have %s satoshi in frxxb!tco.in" %(money, total))
            return int(money)
        else:
            self.write_log(mwin, "Incorrect captcha solution.")
            return -1

    def write_log(self, mwin, content):
        log = '[%s] Frxxb!tco.in: %s' %(str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")), content)
        print log
        mwin.loglist.insert(0, log)
        with open("log/log.txt", "a") as myfile:
            myfile.write(log + '\n')
