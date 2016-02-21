#!/usr/bin/env python
from Tkinter import *
from PIL import ImageTk, Image
from datetime import datetime
from faucet import s0lvemedia
from faucet import m00n
from faucet import zebra
from faucet import alien
from faucet import week
from faucet import dance
from faucet import frxx
from faucet import m0ther
import sys
import time
import winsound

class b!tBot(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.ori_bg = Image.open('img/bg.png')
        resized = self.ori_bg.resize((1280, 1060),Image.ANTIALIAS)
        self.bg = ImageTk.PhotoImage(resized)
        background_label = Label(self, image=self.bg)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.total = 0
        self.today = 0
        self.last = 0
        self.lock = 0
        self.entry_address = StringVar()
        self.entry_frxxpass = StringVar()
        self.entry_xapo = StringVar()
        self.grid()
        self.createWidgets()
 
    def createWidgets(self):
        self.original = Image.open('img/logo.png')
        resized = self.original.resize((320, 160),Image.ANTIALIAS)
        self.logo = ImageTk.PhotoImage(resized)
        self.w1 = Label(self, image=self.logo)
        self.w1.grid(row=0, column=0, columnspan=4, pady=5)
        
        # m00n
        self.m00nVar = IntVar()
        self.m00nVar.set(1)
        self.m00nBtn = Checkbutton(self, text="Enable", variable=self.m00nVar)
        self.m00nBtn["bg"] = "snow3"
        self.m00nBtn["font"] = ("Verdana",12)
        self.m00nBtn.grid(row=1, column=0, pady=2.5)

        self.m00nLogo = Label(self)
        self.m00nLogo["text"] = "M00n b1tc01n"
        self.m00nLogo["font"] = ("Verdana",15)
        self.m00nLogo["bg"] = "black"
        self.m00nLogo["fg"] = "deep sky blue" 
        self.m00nLogo["width"] = 15
        self.m00nLogo.grid(row=2, column=0, pady=2.5)

        self.m00nText = Label(self)
        self.m00nText["text"] = self.get_money("m00n") + " satoshi"
        self.m00nText["font"] = ("Verdana",12)
        self.m00nText["bg"] = "snow3"
        self.m00nText.grid(row=3, column=0, pady=2.5)
        # zebra
        self.zebraVar = IntVar()
        self.zebraVar.set(1)
        self.zebraBtn = Checkbutton(self, text="Enable", variable=self.zebraVar)
        self.zebraBtn["bg"] = "snow3"
        self.zebraBtn["font"] = ("Verdana",12)
        self.zebraBtn.grid(row=1, column=1, pady=2.5)
        
        self.zebraLogo = Label(self)
        self.zebraLogo["text"] = "B1tc01n Zebra"
        self.zebraLogo["font"] = ("Verdana",15)
        self.zebraLogo["bg"] = "black"
        self.zebraLogo["fg"] = "yellow"
        self.zebraLogo["width"] = 15
        self.zebraLogo.grid(row=2, column=1, pady=2.5)

        self.zebraText = Label(self)
        self.zebraText["text"] = self.get_money("zebra") + " satoshi"
        self.zebraText["font"] = ("Verdana",12)
        self.zebraText["bg"] = "snow3"
        self.zebraText.grid(row=3, column=1, pady=2.5)        
        # alien
        self.alienVar = IntVar()
        self.alienVar.set(1)
        self.alienBtn = Checkbutton(self, text="Enable", variable=self.alienVar)
        self.alienBtn["bg"] = "snow3"
        self.alienBtn["font"] = ("Verdana",12)
        self.alienBtn.grid(row=1, column=2, pady=2.5)

        self.alienLogo = Label(self)
        self.alienLogo["text"] = "Alien F@uce7"
        self.alienLogo["font"] = ("Verdana",15)
        self.alienLogo["bg"] = "black"
        self.alienLogo["fg"] = "orange"
        self.alienLogo["width"] = 15
        self.alienLogo.grid(row=2, column=2, pady=2.5)       

        self.alienText = Label(self)
        self.alienText["text"] = self.get_money("alien") + " satoshi"
        self.alienText["font"] = ("Verdana",12)
        self.alienText["bg"] = "snow3"
        self.alienText.grid(row=3, column=2, pady=2.5)
        # week
        self.weekVar = IntVar()
        self.weekVar.set(1)
        self.weekBtn = Checkbutton(self, text="Enable", variable=self.weekVar)
        self.weekBtn["bg"] = "snow3"
        self.weekBtn["font"] = ("Verdana",12)
        self.weekBtn.grid(row=1, column=3, pady=2.5)

        self.weekLogo = Label(self)
        self.weekLogo["text"] = "Weekend B1tc01n"
        self.weekLogo["font"] = ("Verdana",15)
        self.weekLogo["bg"] = "black"
        self.weekLogo["fg"] = "white"
        self.weekLogo["width"] = 15      
        self.weekLogo.grid(row=2, column=3, pady=2.5)      

        self.weekText = Label(self)
        self.weekText["text"] = self.get_money("week") + " satoshi"
        self.weekText["font"] = ("Verdana",12)
        self.weekText["bg"] = "snow3"
        self.weekText.grid(row=3, column=3, pady=2.5)  
        
        # dance
        self.danceVar = IntVar()
        self.danceVar.set(1)
        self.danceBtn = Checkbutton(self, text="Enable", variable=self.danceVar)
        self.danceBtn["bg"] = "snow3"
        self.danceBtn["font"] = ("Verdana",12)
        self.danceBtn.grid(row=4, column=0, pady=2.5)

        self.danceLogo = Label(self)
        self.danceLogo["text"] = "Dance F@uce7"
        self.danceLogo["font"] = ("Verdana",15)
        self.danceLogo["bg"] = "black"
        self.danceLogo["fg"] = "white smoke"  
        self.danceLogo["width"] = 15     
        self.danceLogo.grid(row=5, column=0, pady=2.5)

        self.danceText = Label(self)
        self.danceText["text"] = self.get_money("dance") + " satoshi"
        self.danceText["font"] = ("Verdana",12)
        self.danceText["bg"] = "snow3"
        self.danceText.grid(row=6, column=0, pady=2.5)
        # m0ther
        self.m0therVar = IntVar()
        self.m0therVar.set(1)
        self.m0therBtn = Checkbutton(self, text="Enable", variable=self.m0therVar)
        self.m0therBtn["bg"] = "snow3"
        self.m0therBtn["font"] = ("Verdana",12)
        self.m0therBtn.grid(row=4, column=1, pady=2.5)
        
        self.m0therLogo = Label(self)
        self.m0therLogo["text"] = "Mother F@uce7"
        self.m0therLogo["font"] = ("Verdana",15)
        self.m0therLogo["bg"] = "black"
        self.m0therLogo["fg"] = "red"
        self.m0therLogo["width"] = 15
        self.m0therLogo.grid(row=5, column=1, pady=2.5)

        self.m0therText = Label(self)
        self.m0therText["text"] = self.get_money("m0ther") + " satoshi"
        self.m0therText["font"] = ("Verdana",12)
        self.m0therText["bg"] = "snow3"
        self.m0therText.grid(row=6, column=1, pady=2.5)
        # frxx
        self.frxxVar = IntVar()
        self.frxxVar.set(1)
        self.frxxBtn = Checkbutton(self, text="Enable", variable=self.frxxVar)
        self.frxxBtn["bg"] = "snow3"
        self.frxxBtn["font"] = ("Verdana",12)
        self.frxxBtn.grid(row=4, column=2, pady=2.5)
        
        self.frxxLogo = Label(self)
        self.frxxLogo["text"] = "Frxxb!tco.in"
        self.frxxLogo["font"] = ("Verdana",15)
        self.frxxLogo["bg"] = "black"
        self.frxxLogo["fg"] = "magenta"
        self.frxxLogo["width"] = 15
        self.frxxLogo.grid(row=5, column=2, pady=2.5)

        self.frxxText = Label(self)
        self.frxxText["text"] = self.get_money("frxx") + " satoshi"
        self.frxxText["font"] = ("Verdana",12)
        self.frxxText["bg"] = "snow3"        
        self.frxxText.grid(row=6, column=2, pady=2.5)

        # goldsday
        self.goldVar = IntVar()
        self.goldBtn = Checkbutton(self, text="Enable", variable=self.goldVar, state=DISABLED)
        self.goldBtn["bg"] = "snow3"
        self.goldBtn["font"] = ("Verdana",12)
        self.goldBtn.grid(row=4, column=3, pady=2.5)

        self.goldLogo = Label(self)
        self.goldLogo["text"] = "GoldsDay"
        self.goldLogo["font"] = ("Verdana",15)
        self.goldLogo["bg"] = "black"
        self.goldLogo["fg"] = "gold" 
        self.goldLogo["width"] = 15       
        self.goldLogo.grid(row=5, column=3, pady=2.5)
        
        self.goldText = Label(self)
        self.goldText["text"] = self.get_money("gold") + " satoshi"
        self.goldText["font"] = ("Verdana",12)
        self.goldText["bg"] = "snow3"
        self.goldText.grid(row=6, column=3, pady=4)

        # last
        self.lastLogo = Label(self)
        self.lastLogo["text"] = "Last Run"
        self.lastLogo["font"] = ("Verdana",15)
        self.lastLogo["bg"] = "black"
        self.lastLogo["fg"] = "cyan" 
        self.lastLogo["width"] = 15  
        self.lastLogo.grid(row=7, column=0, pady=2.5)

        self.lastText = Label(self)
        self.lastText["text"] = str(self.last) + " satoshi"
        self.lastText["font"] = ("Verdana",12)
        self.lastText["bg"] = "snow3"        
        self.lastText.grid(row=8, column=0, pady=2.5)
        # today
        self.todayLogo = Label(self)
        self.todayLogo["text"] = "Today Earnings"
        self.todayLogo["font"] = ("Verdana",15)
        self.todayLogo["bg"] = "black"
        self.todayLogo["fg"] = "orange red"
        self.todayLogo["width"] = 15
        self.todayLogo.grid(row=7, column=1, pady=2.5)

        self.todayText = Label(self)
        self.todayText["text"] = str(self.today) + " satoshi"
        self.todayText["font"] = ("Verdana",12)
        self.todayText["bg"] = "snow3"        
        self.todayText.grid(row=8, column=1, pady=2.5)
        # total
        self.totalLogo = Label(self)
        self.totalLogo["text"] = "Total Earnings"
        self.totalLogo["font"] = ("Verdana",15)
        self.totalLogo["bg"] = "black"
        self.totalLogo["fg"] = "light sky blue"
        self.totalLogo["width"] = 15   
        self.totalLogo.grid(row=7, column=2, pady=2.5)

        self.totalText = Label(self)
        self.totalText["text"] = str(self.total) + " satoshi"
        self.totalText["font"] = ("Verdana",12)
        self.totalText["bg"] = "snow3"        
        self.totalText.grid(row=8, column=2, pady=2.5)
        # countdown
        self.timeLogo = Label(self)
        self.timeLogo["text"] = "Countdown"
        self.timeLogo["font"] = ("Verdana",15)
        self.timeLogo["bg"] = "black"
        self.timeLogo["fg"] = "green"
        self.timeLogo["width"] = 15
        self.timeLogo.grid(row=7, column=3, pady=2.5)
        
        self.timeText = Label(self)
        self.timeText["font"] = ("Verdana",12)
        self.timeText["bg"] = "snow3"
        self.timeText["text"] = "Ready!"
        self.timeText.grid(row=8, column=3, pady=2.5)

        self.inputText = Label(self)
        self.inputText["text"] = "B1tc01n Address"
        self.inputText["font"] = ("Verdana",14)
        self.inputText["bg"] = "snow3"
        self.inputText.grid(row=9, column=1, columnspan=2, pady=2.5)

        self.inputField = Entry(self)
        self.inputField["width"] = 50
        self.entry_address.set("14pMEwLQfbWRcrTasRSDeS2g9pdEfa7Gny")        
        self.inputField["textvariable"] = self.entry_address
        self.inputField.grid(row=10, column=1, columnspan=2, pady=2.5)

        self.inputText = Label(self)
        self.inputText["text"] = "Frxxb!tco.in Password (opt)"
        self.inputText["font"] = ("Verdana",14)
        self.inputText["bg"] = "snow3"
        self.inputText.grid(row=11, column=1, columnspan=2, pady=2.5)

        self.inputField = Entry(self)
        self.inputField["width"] = 50    
        self.inputField["textvariable"] = self.entry_frxxpass
        self.inputField["show"] = "*"
        self.inputField.grid(row=12, column=1, columnspan=2, pady=2.5)
        self.inputText = Label(self)
        self.inputText["text"] = "Xapo Account (opt)"
        self.inputText["font"] = ("Verdana",14)
        self.inputText["bg"] = "snow3"
        self.inputText.grid(row=13, column=1, columnspan=2, pady=2.5)

        self.inputField = Entry(self)
        self.inputField["width"] = 50
        self.inputField["textvariable"] = self.entry_xapo
        self.inputField.grid(row=14, column=1, columnspan=2, pady=2.5)

        self.bstart = Button(self)
        self.bstart["text"] = "Start"
        self.bstart["font"] = ("Verdana",12)
        self.bstart["borderwidth"] = 5
        self.bstart["command"] = self.start
        self.bstart.grid(row=15, column=1, pady=2.5)
        
        self.breset = Button(self)
        self.breset["text"] = "Reset"
        self.breset["font"] = ("Verdana",12)
        self.breset["borderwidth"] = 5
        self.breset["command"] = self.reset
        self.breset.grid(row=15, column=2, pady=2.5)
        
        self.loglist = Listbox(self)
        date = str(datetime.now().strftime("%Y-%m-%d"))
        with open("log/log.txt", "r") as f:
            for line in reversed(f.readlines()):
                self.loglist.insert(END, str(line).split("\n")[0])
                if 'B1tc01n 7yper' in line and date in line and 'You get' in line:
                        self.today += int(line.split('You get ')[1].split(' ')[0])
        self.todayText["text"] = str(self.today) + " satoshi"
        self.loglist["width"] = 110
        self.loglist["height"] = 10
        self.loglist.grid(row=16, column=0, columnspan=4, padx=5, pady=5)
        
    def get_money(self, name):
        f = open('log/'+name, 'r')
        money = "".join(f.readline().split())
        self.total += int(money)
        return money

    def update_money(self, name, money):
        log = '[%s] Get %s satoshi' %(str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")), money)
        with open('log/'+name, "a") as f:
            f.write(log + '\n')
        f = open('log/'+name, 'r')
        base = int("".join(f.readline().split()))
        base += money
        data = f.read()
        f = open('log/'+name, 'w')
        f.write(str(base) + '\n' + data)
        if name == 'm00n':
            self.m00nText["text"] = str(base) + " satoshi"
        elif name == 'zebra':
            self.zebraText["text"] = str(base) + " satoshi"
        elif name == 'alien':
            self.alienText["text"] = str(base) + " satoshi"
        elif name == 'dance':
            self.danceText["text"] = str(base) + " satoshi"
        elif name == 'm0ther':
            self.m0therText["text"] = str(base) + " satoshi"
        elif name == 'coincoll':
            self.coincollText["text"] = str(base) + " satoshi"
        elif name == 'gold':
            self.goldText["text"] = str(base) + " satoshi"
        elif name == 'week':
            self.weekText["text"] = str(base) + " satoshi"            
        elif name == 'frxx':
            self.frxxText["text"] = str(base) + " satoshi"

        self.total = self.total + money
        self.totalText["text"] = str(self.total) + " satoshi"

    def start(self):
        address = self.entry_address.get()
        self.last = 0
        if len(address) > 0: 
            cwin = Toplevel(root)
            cwin.img = []
            cwin.captcha = []
            cwin.vaild = []
            no = 0
            # m00nb1tc01n
            if self.m00nVar.get() == 1:
                self.m = m00n.M00N()
                result = self.m.get_start(self, address)
                if result == True:
                    self.get_captcha_win(cwin , no, "m00n", "Captcha from M00n B1tc01n")
                    no += 1
            # b1tc01nzebra
            if self.zebraVar.get() == 1:
                self.z = zebra.ZEBRA()
                result = self.z.get_start(self, address)
                self.get_captcha_win(cwin, no, "zebra", "Captcha from B1tc01n Zebra")
                no += 1
            # Alien F@uce7
            if self.alienVar.get() == 1:
                self.a = alien.ALIEN()
                result = self.a.get_start(self, address)
                if result == True:
                    self.get_captcha_win(cwin, no, "alien", "Captcha from Alien F@uce7")
                    no += 1
            # Weekend B1tc01n
            if self.weekVar.get() == 1:
                self.w = week.WEEK()
                result = self.w.get_start(self, address)
                if result == True:
                    self.get_captcha_win(cwin, no, "week", "Captcha from Weekend B1tc01n")
                    no += 1
            # Dance F@uce7
            if self.danceVar.get() == 1:
                self.d = dance.DANCE()
                result = self.d.get_start(self, address)
                self.get_captcha_win(cwin, no, "dance", "Captcha from Dance F@uce7")
                no += 1
            # Frxx
            if self.frxxVar.get() == 1 and len(self.entry_frxxpass.get()) > 0:
                self.f = frxx.FRXX()
                self.f.password = self.entry_frxxpass.get()
                result = self.f.get_start(self, address)
                if result == True:
                    self.get_captcha_win(cwin, no, "frxx", "Captcha from Frxxb!tco.in")
                    no += 1
            # Mother
            if self.m0therVar.get() == 1 and len(self.entry_xapo.get()) > 0:
                self.md = m0ther.MOTHER()
                result = self.md.get_start(self, self.entry_xapo.get())
                if result == True:
                    self.get_captcha_win(cwin, no, "m0ther", "Captcha from Mother F@uce7")
                    no += 1

            # sumbit button
            if no > 0:
                cwin.new = Button(cwin)
                cwin.new["text"] = "Submit"
                cwin.new["command"] = lambda: self.button_submit(cwin)
                cwin.new.grid(row=10, column=0, columnspan=no/3+1)
                try:
                    winsound.PlaySound('img/wolf.wav', winsound.SND_FILENAME)
                except:
                    print "Pop!"
        else:
            self.write_log("Please enter a b1tc01n address.")

    def reset(self):
        if self.lock == 0:
            self.lock = 1
            self.remaining = 0
            self.countdown(3600)
        else:
            self.remaining = 3600

    def get_captcha_win(self, cwin, no, name, title):
        cwin.title("Chatcha List[%s]" %str(no+1))
        cwin.vaild.append(name)
        cwin.img.append(ImageTk.PhotoImage(Image.open('captcha/%s_captcha.gif' %name)))
        cwin.captcha.append(Label(cwin, image=cwin.img[no]))
        cwin.captcha[no].grid(row=(no%3)*3, column=no/3)

        cwin.inputText = Label(cwin)
        cwin.inputText["fg"] = "red"
        cwin.inputText["text"] = title
        cwin.inputText.grid(row=(no%3)*3+1, column=no/3)

        cwin.inputField = Entry(cwin)
        cwin.inputField["width"] = 35
        if name == "m00n":
            self.mcaptcha = StringVar()
            cwin.inputField["textvariable"] = self.mcaptcha
        elif name == "zebra":
            self.zcaptcha = StringVar()
            cwin.inputField["textvariable"] = self.zcaptcha
        elif name == "alien":
            self.acaptcha = StringVar()
            cwin.inputField["textvariable"] = self.acaptcha
        elif name == "week":
            self.wcaptcha = StringVar()
            cwin.inputField["textvariable"] = self.wcaptcha            
        elif name == "dance":
            self.dcaptcha = StringVar()
            cwin.inputField["textvariable"] = self.dcaptcha
        elif name == "coincoll":
            self.ccaptcha = StringVar()
            cwin.inputField["textvariable"] = self.ccaptcha
        elif name == "gold":
            self.gcaptcha = StringVar()
            cwin.inputField["textvariable"] = self.gcaptcha
        elif name == "frxx":
            self.fcaptcha = StringVar()
            cwin.inputField["textvariable"] = self.fcaptcha
        elif name == "m0ther":
            self.mdcaptcha = StringVar()
            cwin.inputField["textvariable"] = self.mdcaptcha
        cwin.inputField.grid(row=(no%3)*3+2, column=no/3)

    def button_submit(self, cwin):
        address = self.entry_address.get()
        account = self.entry_xapo.get()
        try:
            for idx, name in enumerate(cwin.vaild):
                money = 0
                if name == 'm00n' and len(self.mcaptcha.get()) > 0:
                    money = self.m.post_summit_captcha(self, address, self.mcaptcha.get(), self.m.c)
                elif name == 'zebra' and len(self.zcaptcha.get()) > 0:
                    money = self.z.post_summit_captcha(self, address, self.zcaptcha.get(), self.z.c)
                elif name == 'alien' and len(self.acaptcha.get()) > 0:
                    money = self.a.post_summit_captcha(self, address, self.acaptcha.get(), self.a.c)
                elif name == 'week' and len(self.wcaptcha.get()) > 0:
                    money = self.w.post_summit_captcha(self, address, self.wcaptcha.get(), self.w.c)
                elif name == 'dance' and len(self.dcaptcha.get()) > 0:
                    money = self.d.post_summit_captcha(self, address, self.dcaptcha.get(), self.d.c)
                elif name == 'frxx' and len(self.fcaptcha.get()) > 0:
                    money = self.f.post_summit_captcha(self, address, self.fcaptcha.get())
                elif name == 'm0ther' and len(self.mdcaptcha.get()) > 0:
                    money = self.md.post_summit_captcha(self, account, self.mdcaptcha.get(), self.md.c)
                if money > 0:
                    self.update_money(name, money)
                    self.last += money
        except:
            self.write_log("Can't connect to %s" %name)
        self.lastText["text"] = str(self.last) + " satoshi"
        self.today += self.last
        self.todayText["text"] = str(self.today) + " satoshi"
        self.write_log("Congratulations, You get %s satoshi this run!" %str(self.last))
        cwin.destroy()
        if self.lock == 0:
            self.lock = 1
            self.remaining = 0
            self.countdown(3600)
        try:
            winsound.PlaySound('img/wolf.wav', winsound.SND_FILENAME)
        except:
            print "Done!"

    def countdown(self, remaining = None):
        if remaining is not None:
            self.remaining = remaining
        if self.remaining <= 0:
            self.timeText["text"] = "Ready!"
            try:
                winsound.PlaySound('img/wolf.wav', winsound.SND_FILENAME)
            except:
                print "Ready!"
            self.lock = 0
        else:
            self.timeText["text"] = str("%d:%d" %(self.remaining/60, self.remaining%60))
            self.remaining = self.remaining - 1
            self.after(1000, self.countdown)

    def write_log(self, content):
        log = '[%s] B1tc01n 7yper: %s' %(str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")), content)
        #print log
        self.loglist.insert(0, log)
        with open("log/log.txt", "a") as myfile:
            myfile.write(log + '\n')

if __name__ == '__main__':
    sys.stderr = sys.stdout
    root = Tk()
    root.iconbitmap(default='img/logo.ico')
    root.resizable(width=FALSE, height=FALSE)
    app = BitBot(master=root)
    app.master.title("B1tc01n 7yper 2.5 - B1tc01n F@uce7 Bot")
    app.mainloop()
