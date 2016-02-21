import requests
import urllib
import json
import sys
import subprocess
import time
from datetime import datetime
from bs4 import BeautifulSoup
from requests_toolbelt import MultipartEncoder

class TW0CAPTCHA:
    key = ''
    def get_balance(self, mwin):
        url = 'http://2captcha.com/res.php'
        url += '?key=%s&action=getbalance' %self.key
        try:
            get_response = requests.get(url)
            try:
                balance = int(float(get_response.content)*1000)
            except:
                return -1
            return balance
        except requests.exceptions.ConnectionError:
            self.write_log(mwin, "Can't connect to 2captcha server.")
            return -1

    def update_img(self, name, mwin):
        url = 'http://2captcha.com/in.php'
        if name == 'usd':
            m = MultipartEncoder(
                fields={'method': 'post', 'key': self.key,
                        'file': ('%s_captcha.png' %name, open('captcha/%s_captcha.png' %name, 'rb'), 'image/png')}
                )
        else:
            m = MultipartEncoder(
                fields={'method': 'post', 'key': self.key,
                        'file': ('%s_captcha.gif' %name, open('captcha/%s_captcha.gif' %name, 'rb'), 'image/gif')}
                )
        session = requests.Session()
        try:
            post_response = session.post(url, data=m, headers={'Content-Type': m.content_type})
            if "OK" in post_response.content:
                self.id = post_response.content.split('|')[1]
                return True
            else:
                self.write_log(mwin, post_response.content)
                return False
        except requests.exceptions.ConnectionError:
            self.write_log(mwin, "Can't connect to 2captcha server.")
            return False

    def get_captcha(self, name, mwin):
        url = 'http://2captcha.com/res.php?key=%s&action=get&id=%s' %(self.key, self.id)
        while 1:
            try:
                get_response = requests.get(url)
            except:
                self.write_log(mwin, "Can't connect to 2captcha server.")
                return -1
            if "OK" in get_response.content:
                self.captcha = get_response.content.split('|')[1]
                msg = "solve %s captcha: %s" %(name, self.captcha)
                #self.write_log(mwin, msg)
                return 1
            else:
                if "CAPCHA_NOT_READY" in get_response.content:
                    time.sleep(10)
                    continue
                elif "ERROR_CAPTCHA_UNSOLVABLE" in get_response.content:
                    self.write_log(mwin, "CAPTCHA_UNSOLVABLE")
                    return 0
                else:
                    self.write_log(mwin, "Can't connect to 2captcha server.")
                    print get_response.content
                    return -1

    def captcha_solver(self, name, mwin):
        self.id = ''
        update = self.update_img(name, mwin)
        if update == True:
            time.sleep(30)
            solve = self.get_captcha(name, mwin)
            if solve == 1:
                return True
        return False

    def write_log(self, mwin, content):
        log = '[%s] Captcha Solver: %s' %(str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")), content)
        print log
        mwin.loglist.insert(0, log)
        with open("log/log.txt", "a") as myfile:
            myfile.write(log + '\n')
