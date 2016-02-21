import requests
#import time
#from datetime import datetime

class S0LVEMEDIA():
    def get_captcha_info(self, k):
        url = 'http://api.S0LVEMEDIA.com/papi/challenge.script?'
        url += 'k=' + k
        get_response = requests.get(url, timeout=20)
        parm = "".join(str(get_response.text).split())
        ACPuzzleInfo_ckey = parm.split('ckey:\'')[1].split('\'')[0];
        ACPuzzleInfo_magic = parm.split('magic:\'')[1].split('\'')[0];
        ACPuzzleInfo_stamp = parm.split('chalstamp:')[1].split(',')[0];
        return (ACPuzzleInfo_ckey, ACPuzzleInfo_magic, ACPuzzleInfo_stamp)

    def get_captcha_image(mwin, ACPuzzleInfo_ckey, ACPuzzleInfo_magic, ACPuzzleInfo_stamp, name):
        while 1:
            url = 'http://api.S0LVEMEDIA.com/papi/_challenge.js?'
            url += 'k=' + ACPuzzleInfo_ckey
            url += ';f=_ACPuzzleUtil.callbacks[0];l=en;t=img;s=standard'
            url += ';c=js,h5c,h5ct,svg,h5v,v/h264,v/ogg,v/webm,h5a,a/mp3,a/ogg,ua/chrome,ua/chrome39,os/nt,os/nt6.3,expand,swf16,swf16.0,swf,fwv/MLEOng.abcd88'
            url += ';am=' + ACPuzzleInfo_magic
            url += ';ca=script;ts=1422158587'
            url += ';ct=' + ACPuzzleInfo_stamp
            url += ';th=black;r=0.1'
            # 1
            get_response = requests.get(url, timeout=20)
            sscn_a = get_response.cookies['_sscn_a']
            sscn_b = get_response.cookies['_sscn_b']
            ssts_lr = get_response.cookies['_ssts_lr']
            # 2
            headers = {'Cookie': '_sscn_a=' + sscn_a + '; _sscn_b=' + sscn_b + '; _ssts_lr=' + ssts_lr + ';'}
            get_response = requests.get(url, headers=headers, timeout=20)
            sscn_up = get_response.cookies['_sscn_up']
            # 3 
            headers = {'Cookie': '_sscn_a=' + sscn_a + '; _sscn_b=' + sscn_b + '; _ssts_lr=' + ssts_lr + '; _sscn_up=' + sscn_up + ';', 
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:35.0) Gecko/20100101 Firefox/35.0'}
            get_response = requests.get(url, headers=headers, timeout=20)
            #Get puzzle img
            parm = "".join(str(get_response.text).split())
            ACPuzzleInfo_c = parm.split('"chid":"')[1].split('"')[0];
            ACPuzzleInfo_uid = parm.split('"uid":"')[1].split('"')[0];
            url = 'http://api.S0LVEMEDIA.com/papi/media?'
            url += 'c=' + ACPuzzleInfo_c
            headers = {'Cookie': '_sscn_a=' + sscn_a + '; _sscn_b=' + sscn_b + '; _ssts_lr=' + ssts_lr + '; _sscn_up=' + sscn_up + ';',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:35.0) Gecko/20100101 Firefox/35.0'}
            r = requests.get(url, headers=headers, stream=True, timeout=20)
            if 'text' in r.headers['content-type']:
                fname = 'captcha.htm'
            else:
                fname = 'captcha/%s_captcha.gif' %name
                with open(fname, 'wb') as f:
                    for chunk in r.iter_content():
                        f.write(chunk)
                return (ACPuzzleInfo_c, ACPuzzleInfo_uid)

