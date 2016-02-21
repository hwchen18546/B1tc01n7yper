#!/usr/bin/env python
from Tkinter import *
from PIL import ImageTk, Image
from datetime import datetime
from faucet import s0lvemedia
from faucet import m00n
from faucet import zebra
from faucet import week
from faucet import dance
from faucet import frxx
from faucet import m0ther
from solver import twocaptcha
import sys
import time
import winsound

class BitBot(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.ori_bg = Image.open('img/bg.png')
        resized = self.ori_bg.resize((1280, 1060),Image.ANTIALIAS)
        self.bg = ImageTk.PhotoImage(resized)
        background_label = Label(self, image=self.bg)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.tc = twocaptcha.TWOCAPTCHA()
        self.total = 0
        self.today = 0
        self.lock = 0
        self.run = 0
        self.runtime = 3600
        self.entry_address = StringVar()
        self.entry_frxxpass = StringVar()
        self.entry_xapo = StringVar()
        self.entry_key = StringVar()
        self.grid()
        self.createWidgets()
 
    def createWidgets(self):
        self.original = Image.open('img/logo.png')
        resized = self.original.resize((240, 120),Image.ANTIALIAS)
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

        # week
        self.weekVar = IntVar()
        self.weekVar.set(1)
        self.weekBtn = Checkbutton(self, text="Enable", variable=self.weekVar)
        self.weekBtn["bg"] = "snow3"
        self.weekBtn["font"] = ("Verdana",12)
        self.weekBtn.grid(row=1, column=2, pady=2.5)

        self.weekLogo = Label(self)
        self.weekLogo["text"] = "Weekend B1tc01n"
        self.weekLogo["font"] = ("Verdana",15)
        self.weekLogo["bg"] = "black"
        self.weekLogo["fg"] = "orange"
        self.weekLogo["width"] = 15      
        self.weekLogo.grid(row=2, column=2, pady=2.5)
        
        self.weekText = Label(self)
        self.weekText["text"] = self.get_money("week") + " satoshi"
        self.weekText["font"] = ("Verdana",12)
        self.weekText["bg"] = "snow3"
        self.weekText.grid(row=3, column=2, pady=2.5)    

        # dance
        self.danceVar = IntVar()
        self.danceVar.set(1)
        self.danceBtn = Checkbutton(self, text="Enable", variable=self.danceVar)
        self.danceBtn["bg"] = "snow3"
        self.danceBtn["font"] = ("Verdana",12)
        self.danceBtn.grid(row=1, column=3, pady=2.5)

        self.danceLogo = Label(self)
        self.danceLogo["text"] = "Dance F@uce7"
        self.danceLogo["font"] = ("Verdana",15)
        self.danceLogo["bg"] = "black"
        self.danceLogo["fg"] = "white"  
        self.danceLogo["width"] = 15
        self.danceLogo.grid(row=2, column=3, pady=2.5)

        self.danceText = Label(self)
        self.danceText["text"] = self.get_money("dance") + " satoshi"
        self.danceText["font"] = ("Verdana",12)
        self.danceText["bg"] = "snow3"
        self.danceText.grid(row=3, column=3, pady=2.5)  
        # m0ther
        self.m0therVar = IntVar()
        self.m0therVar.set(1)
        self.m0therBtn = Checkbutton(self, text="Enable", variable=self.m0therVar)
        self.m0therBtn["bg"] = "snow3"
        self.m0therBtn["font"] = ("Verdana",12)
        self.m0therBtn.grid(row=4, column=0, pady=2.5)
        
        self.m0therLogo = Label(self)
        self.m0therLogo["text"] = "M0ther F@uce7"
        self.m0therLogo["font"] = ("Verdana",15)
        self.m0therLogo["bg"] = "black"
        self.m0therLogo["fg"] = "red"
        self.m0therLogo["width"] = 15
        self.m0therLogo.grid(row=5, column=0, pady=2.5)

        self.m0therText = Label(self)
        self.m0therText["text"] = self.get_money("m0ther") + " satoshi"
        self.m0therText["font"] = ("Verdana",12)
        self.m0therText["bg"] = "snow3"
        self.m0therText.grid(row=6, column=0, pady=2.5)
        
        # frxx
        self.frxxVar = IntVar()
        self.frxxVar.set(1)
        self.frxxBtn = Checkbutton(self, text="Enable", variable=self.frxxVar)
        self.frxxBtn["bg"] = "snow3"
        self.frxxBtn["font"] = ("Verdana",12)
        self.frxxBtn.grid(row=4, column=1, pady=2.5)
        
        self.frxxLogo = Label(self)
        self.frxxLogo["text"] = "Frxxb!tco.in"
        self.frxxLogo["font"] = ("Verdana",15)
        self.frxxLogo["bg"] = "black"
        self.frxxLogo["fg"] = "magenta"
        self.frxxLogo["width"] = 15
        self.frxxLogo.grid(row=5, column=1, pady=2.5)

        self.frxxText = Label(self)
        self.frxxText["text"] = self.get_money("frxx") + " satoshi"
        self.frxxText["font"] = ("Verdana",12)
        self.frxxText["bg"] = "snow3"        
        self.frxxText.grid(row=6, column=1, pady=2.5)
        
        # today
        self.todayLogo = Label(self)
        self.todayLogo["text"] = "Today Earnings"
        self.todayLogo["font"] = ("Verdana",15)
        self.todayLogo["bg"] = "black"
        self.todayLogo["fg"] = "green"
        self.todayLogo["width"] = 15
        self.todayLogo.grid(row=5, column=2, pady=2.5)

        self.todayText = Label(self)
        self.todayText["text"] = str(self.today) + " satoshi"
        self.todayText["font"] = ("Verdana",12)
        self.todayText["bg"] = "snow3"        
        self.todayText.grid(row=6, column=2, pady=2.5)        
        # total
        self.totalLogo = Label(self)
        self.totalLogo["text"] = "Total Earnings"
        self.totalLogo["font"] = ("Verdana",15)
        self.totalLogo["bg"] = "black"
        self.totalLogo["fg"] = "orange red"
        self.totalLogo["width"] = 15
        self.totalLogo.grid(row=5, column=3, pady=2.5)

        self.totalText = Label(self)
        self.totalText["text"] = str(self.total) + " satoshi"
        self.totalText["font"] = ("Verdana",12)
        self.totalText["bg"] = "snow3"        
        self.totalText.grid(row=6, column=3, pady=2.5)
        # solver
        self.solverLogo = Label(self)
        self.solverLogo["text"] = "2Captcha Balance"
        self.solverLogo["font"] = ("Verdana",15)
        self.solverLogo["bg"] = "black"
        self.solverLogo["fg"] = "light sky blue"
        self.solverLogo["width"] = 15
        self.solverLogo.grid(row=7, column=0, pady=2.5)

        self.solverText = Label(self)
        self.solverText["text"] = "0 mUSD"
        self.solverText["font"] = ("Verdana",12)
        self.solverText["bg"] = "snow3"
        self.solverText.grid(row=8, column=0, pady=2.5)

        # countdown
        self.timeLogo = Label(self)
        self.timeLogo["text"] = "Countdown"
        self.timeLogo["font"] = ("Verdana",15)
        self.timeLogo["bg"] = "black"
        self.timeLogo["fg"] = "magenta"
        self.timeLogo["width"] = 15
        self.timeLogo.grid(row=7, column=3, pady=2.5)
        
        self.timeText = Label(self)
        self.timeText["font"] = ("Verdana",12)
        self.timeText["bg"] = "snow3"
        self.timeText["text"] = "Ready!"
        self.timeText.grid(row=8, column=3, pady=2.5)

        # address
        self.inputText = Label(self)
        self.inputText["text"] = "B1tc01n Address"
        self.inputText["font"] = ("Verdana",14)
        self.inputText["bg"] = "snow3"
        self.inputText.grid(row=7, column=1, columnspan=2, pady=2.5)

        self.inputField = Entry(self)
        self.inputField["width"] = 50
        self.inputField["textvariable"] = self.entry_address
        self.entry_address.set("14pMEwLQfbWRcrTasRSDeS2g9pdEfa7Gny")
        self.inputField.grid(row=8, column=1, columnspan=2, pady=2.5)
        
        self.inputText = Label(self)
        self.inputText["text"] = "FrxxBitco.in Password (opt)"
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

        # key
        self.inputText = Label(self)
        self.inputText["text"] = "2Captcha API KEY"
        self.inputText["font"] = ("Verdana",14)
        self.inputText["bg"] = "snow3"
        self.inputText.grid(row=15, column=1, columnspan=2, pady=2.5)

        self.inputField = Entry(self)
        self.inputField["width"] = 50
        self.inputField["textvariable"] = self.entry_key
        self.inputField.grid(row=16, column=1, columnspan=2, pady=2.5)

        self.bstart = Button(self)
        self.bstart["text"] = "Start"
        self.bstart["font"] = ("Verdana",12)
        self.bstart["borderwidth"] = 5
        self.bstart["command"] = self.start
        self.bstart.grid(row=17, column=1, pady=2.5)
        
        self.breset = Button(self)
        self.breset["text"] = "Reset"
        self.breset["font"] = ("Verdana",12)
        self.breset["borderwidth"] = 5
        self.breset["command"] = self.reset
        self.breset.grid(row=17, column=2, pady=2.5)
        
        self.loglist = Listbox(self) 
        with open("log/log.txt", "r") as f:
            for line in reversed(f.readlines()):
                self.loglist.insert(END, str(line).split("\n")[0])
        self.loglist["width"] = 110
        self.loglist["height"] = 10
        self.loglist.grid(row=18, column=0, columnspan=4, padx=5, pady=5)

        date = str(datetime.now().strftime("%Y-%m-%d"))
        add = True
        with open("log/day.txt", "r") as f:
            for line in f.readlines():
                if date in line:
                    self.today = int(line.split("%s:" %date)[1])
                    add =False
                    break
        if add == True:
            with open("log/day.txt", "w") as f:
                f.write("%s:0\n" %date)
        self.todayText["text"] = str(self.today) + " satoshi"
        
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
        elif name == 'dance':
            self.danceText["text"] = str(base) + " satoshi"
        elif name == 'week':
            self.weekText["text"] = str(base) + " satoshi"
        elif name == 'm0ther':
            self.m0therText["text"] = str(base) + " satoshi"
        elif name == 'frxx':
            self.frxxText["text"] = str(base) + " satoshi"
        # New day reset and add today record
        date = str(datetime.now().strftime("%Y-%m-%d"))
        add = True
        with open("log/day.txt", "r") as f:
            for line in f.readlines():
                if date in line:
                    add =False
                    break
        if add == True:
            self.today = 0
        self.today += money
        self.todayText["text"] = str(self.today) + " satoshi"
        with open("log/day.txt", "w") as f:
            f.write("%s:%s\n" %(date, str(self.today)))
        # Add total record
        self.total = self.total + money
        self.totalText["text"] = str(self.total) + " satoshi"
        
    def start(self):
        self.address = self.entry_address.get()
        self.tc.key = self.entry_key.get()
        coda = self.tc.get_balance(self)
        if coda == -1:
            self.write_log("Can't connect to 2captcha server.")
            if self.lock == 0:
                self.lock = 1
                self.remaining = 0
                self.countdown(self.runtime)
            return False        
        elif coda < 10:
            self.write_log("You don't have enough money on your 2captcha account.")
            return False
        if self.run % 1 == 0:
            if self.m00nVar.get() == 1:
                self.start_m00n()
            if self.m0therVar.get() == 1 and len(self.entry_xapo.get()) > 0:
                self.start_m0ther()
            if self.zebraVar.get() == 1:
                self.start_zebra()
            if self.weekVar.get() == 1:
                self.start_week()
            if self.danceVar.get() == 1:
                self.start_dance()
            if self.frxxVar.get() == 1 and len(self.entry_frxxpass.get()) > 0:
                self.start_frxx()
        self.run += 1
        self.solverText["text"] = str(self.tc.get_balance(self)) + " mUSD"
        if self.lock == 0:
            self.lock = 1
            self.remaining = 0
            self.countdown(self.runtime)

    def start_m00n(self):
        name = 'm00n'
        self.m = m00n.M00N()
        try:
            result = self.m.get_start(self, self.address)
            if result == True:
                solve = self.tc.captcha_solver(name, self)
                if solve == True:
                    money = self.m.post_summit_captcha(self, self.address, self.tc.captcha, self.m.c)
                    if money > 0:
                        self.update_money(name, money)
        except:
            self.write_log("Can't connect to M00n B1tc01n.")
    def start_week(self):
        name = 'week'
        try:
            while 1:
                self.w = week.WEEK()
                result = self.w.get_start(self, self.address)
                if result == True:
                    solve = self.tc.captcha_solver(name, self)
                    if solve == True:
                        money = self.w.post_summit_captcha(self, self.address, self.tc.captcha, self.w.c)
                        if money > 0:
                            self.update_money(name, money)
                            break
                        elif money == 0:
                            continue
                break
        except:
            self.write_log("Can't connect to Weekend B1tc01n.")
    def start_zebra(self):
        name = 'zebra'
        self.z = zebra.ZEBRA()
        try:
            result = self.z.get_start(self, self.address)
            solve = self.tc.captcha_solver(name, self)
            if solve == True:
                money = self.z.post_summit_captcha(self, self.address, self.tc.captcha, self.z.c)
                if money > 0:
                    self.update_money(name, money)
        except:
            self.write_log("Can't connect to B1tc01n Zebra.")
    def start_dance(self):
        name = 'dance'
        self.d = dance.DANCE()
        try:
            result = self.d.get_start(self, self.address)
            solve = self.tc.captcha_solver(name, self)
            if solve == True:
                money = self.d.post_summit_captcha(self, self.address, self.tc.captcha, self.d.c)
                if money > 0:
                    self.update_money(name, money)
        except:
            self.write_log("Can't connect to Dance F@uce7.")
    def start_frxx(self):
        name = 'frxx'
        self.f = frxx.FRXX()
        try:
            self.f.password = self.entry_frxxpass.get()
            result = self.f.get_start(self, self.address)
            if result == True:
                solve = self.tc.captcha_solver(name, self)
                if solve == True:
                    money = self.f.post_summit_captcha(self, self.address, self.tc.captcha)
                    if money > 0:
                        self.update_money(name, money)
        except:
            self.write_log("Can't connect to Frxxb!tco.in.")
    def start_m0ther(self):
        name = 'm0ther'
        account = self.entry_xapo.get()
        try:
            self.md = m0ther.M0THER()
            while 1:
                result = self.md.get_start(self, account)
                if result == True:
                    solve = self.tc.captcha_solver(name, self)
                    if solve == True:
                        money = self.md.post_summit_captcha(self, account, self.tc.captcha, self.md.c)
                        if money == -1:
                            continue
                        elif money > 0:
                            self.update_money(name, money)
                break
        except:
            self.write_log("Can't connect to M0ther F@uce7.")

    def reset(self):
        if self.lock == 0:
            self.lock = 1
            self.remaining = 0
            self.countdown(self.runtime)
        else:
            self.remaining = self.runtime

    def countdown(self, remaining = None):
        if remaining is not None:
            self.remaining = remaining
        if self.remaining <= 0:
            self.timeText["text"] = "Ready!"
            self.lock = 0
            self.start()           
        else:
            self.timeText["text"] = str("%d:%d" %(self.remaining/60, self.remaining%60))
            self.remaining = self.remaining - 1
            self.after(1000, self.countdown)

    def write_log(self, content):
        log = '[%s] B1tc01n 7yper: %s' %(str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")), content)
        print log
        self.loglist.insert(0, log)
        with open("log/log.txt", "a") as myfile:
            myfile.write(log + '\n')
        
if __name__ == '__main__':
    sys.stderr = sys.stdout
    root = Tk()
    root.iconbitmap(default='img/logo.ico')
    root.resizable(width=FALSE, height=FALSE)
    app = BitBot(master=root)
    app.master.title("B1tc01n 7yper Pro 2.1 - Full Auto B1tc01n F@uce7 Bot")
    app.mainloop()
