import requests
import urllib
import json
import sys
import subprocess
import time
from datetime import datetime
from s0lvemedia import S0LVEMEDIA
from bs4 import BeautifulSoup

class M00N:
    k = 'xxmubMTi7BBM98cMxgtIcLP4k1Ga5Qxx'
    def get_session(self):
        url = 'http://m00nb!t.co.in/?ref=6d6dc04927xx'
        get_response = requests.get(url, timeout=20)
        soup = BeautifulSoup(get_response.text)
        viewstate = str(soup.select('#__VIEWSTATE')[0].get('value'))
        eventvalidation = str(soup.select('#__EVENTVALIDATION')[0].get('value'))
        cfduid = get_response.cookies['__cfduid']
        sessionid = get_response.cookies['ASP.NET_SessionId']
        return (viewstate, eventvalidation, cfduid, sessionid)

    def post_login(self, address, viewstate, eventvalidation, cfduid, sessionid):
        url = 'http://m00nb!t.co.in/?ref=6d6dc04927xx'
        headers = {'Cookie': '__cfduid=' + cfduid + '; ASP.NET_SessionId=' + sessionid + ';', 'Content-Type': 'application/x-www-form-urlencoded'}
        session = requests.Session()
        post_data = {'__VIEWSTATE': viewstate, '__EVENTVALIDATION': eventvalidation, 'ctl00$BodyPlaceholder$PaymentAddressTextbox': address, 'ctl00$BodyPlaceholder$SignInButton': 'sign+in'}
        post_response = session.post(url, data=urllib.urlencode(post_data), headers=headers, timeout=20)
        if "You did not enter a valid b!tcoin or email address" in post_response.content:
            return False
        return True
        
    def get_account_info(self, mwin, address, viewstate, eventvalidation, cfduid, sessionid):
        url = 'http://m00nb!t.co.in/'+'api/claimsummary/?paymentAddress='+address
        headers = {'Cookie': '__cfduid=' + cfduid + '; ASP.NET_SessionId=' + sessionid + '; user=PaymentAddress=' + address}
        get_response = requests.get(url, headers=headers, timeout=20)
        money = json.loads(get_response.text)
        #print 'ClaimAmount: ' + str(money['ClaimAmount']) + ' satoshi\n'
        #print 'CanClaim: ' + str(money['CanClaim']) + '\n'
        if money['CanClaim'] == False:
            try:
                self.write_log(mwin, 'Not yet - please try again in %s sec.' %(str(300 - money['TimeSinceLastClaimSeconds'])))
            except:
                self.write_log(mwin, 'Please go to m00n b!tcoin website do the first chaim.')
            #time.sleep(300 - money['TimeSinceLastClaimSeconds'])
            return False
        #self.write_log(mwin, 'Can get %s satoshi.' %str(money['ClaimAmount']))
        return True

    def update_session(self, address, cfduid, sessionid):
        url = 'http://m00nb!t.co.in/?ref=6d6dc0492726'
        headers = {'Cookie': '__cfduid=' + cfduid + '; ASP.NET_SessionId=' + sessionid + '; user=PaymentAddress=' + address}
        get_response = requests.get(url, headers=headers, timeout=20)
        soup = BeautifulSoup(get_response.text)
        viewstate = str(soup.select('#__VIEWSTATE')[0].get('value'))
        eventvalidation = str(soup.select('#__EVENTVALIDATION')[0].get('value'))
        return (viewstate, eventvalidation)

    def get_start(self, mwin, account):
        (self.viewstate, self.eventvalidation, self.cfduid, self.sessionid) = self.get_session()
        login = self.post_login(account, self.viewstate, self.eventvalidation, self.cfduid, self.sessionid)
        if login == False:
            self.write_log(mwin, "You did not enter a valid b!tcoin or email address.")
            return False
        claim = self.get_account_info(mwin, account, self.viewstate, self.eventvalidation, self.cfduid, self.sessionid)
        if claim == True:
            sm = S0LVEMEDIA()
            (ckey, magic, stamp) = sm.get_captcha_info(self.k)
            (self.c, uid) = sm.get_captcha_image(ckey, magic, stamp, "m00n")
            (self.viewstate, self.eventvalidation) = self.update_session(account, self.cfduid, self.sessionid)
            return True
        return False

    def post_summit_captcha(self, mwin, address, captcha, ACPuzzleInfo_c):
        url = 'http://m00nb!t.co.in/?ref=6d6dc0492726'
        headers = {'Cookie': '__cfduid=' + self.cfduid + '; ASP.NET_SessionId=' + self.sessionid + '; user=PaymentAddress=' + address + ';',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:35.0) Gecko/20100101 Firefox/35.0',
        'Content-Type': 'application/x-www-form-urlencoded'}
        post_data = {'__VIEWSTATE': self.viewstate, '__EVENTVALIDATION': self.eventvalidation, 
        'adcopy_response': captcha, 'adcopy_challenge': ACPuzzleInfo_c,
        'ctl00$PagePopupPlaceholder$ClaimButton': 'submit'}
        session = requests.Session()
        post_response = session.post(url, data=urllib.urlencode(post_data), headers=headers, timeout=20)
        if "failure-message" in post_response.text:
            self.write_log(mwin, "Incorrect captcha solution.")
            return -1
        elif "success-message" in post_response.text:
            money = post_response.content.split('"success-message">')[1].split(' ')[0]
            money = "".join(money.split())
            self.write_log(mwin, "Congratulations, %s satoshi has been added to your M00n B!tcoin account." %money)
            return int(money)

    def write_log(self, mwin, content):
        log = '[%s] M00n B!tcoin: %s' %(str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")), content)
        print log
        mwin.loglist.insert(0, log)
        with open("log/log.txt", "a") as myfile:
            myfile.write(log + '\n')
