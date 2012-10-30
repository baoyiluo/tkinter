#coding:utf-8
import Tkinter as tk
from Tkinter import *
import threading
import time
lock=threading.Lock()
class MyWindow():
    def __init__(self):
        self.root=tk.Tk()
        self.root.title('Dcloud环境部署管理平台')
        self.root.geometry('350x250+500+250')
        labtop=Label(self.root,text="初始化本机环境")
        labelfont = ('courier', 10, 'bold')
        labtop.config(font=labelfont)
        labtop.pack(side='top',pady=10)
        
        labip=Label(self.root,text="IP:")
        labipfont = ('courier', 8,'bold')
        labip.config(font=labipfont)
        labip.pack(anchor='nw',padx=50,pady=10)
        
        rot=Frame(self.root)
        rot.pack(anchor='nw',padx=60,pady=0)
        labe0=Label(rot,text="eth0")
        labe0font = ('courier', 6,'bold')
        labe0.config(font=labe0font)
        labe0.pack(anchor='nw',side='left',padx=0,pady=0)
        self.e=StringVar()
        entry=Entry(rot,textvariable=self.e)
        #e.set('Hello World')
        entry.pack(anchor='nw',side='left',padx=0,pady=0)
        
        rot1=Frame(self.root)
        rot1.pack(anchor='nw',padx=60,pady=0)
        labe1=Label(rot1,text="eth1")
        labe1font = ('courier', 6,'bold')
        labe1.config(font=labe1font)
        labe1.pack(anchor='nw',side='left',padx=0,pady=0)
        self.e1=StringVar()
        entry=Entry(rot1,textvariable=self.e1)
        #e.set('Hello World')
        entry.pack(anchor='nw',side='left',padx=0,pady=0)
        
        roth=Frame(self.root)
        roth.pack(anchor='nw',padx=50,pady=10)
        labhost=Label(roth,text="主机名:")
        labhost.config(font=labipfont)
        labhost.pack(anchor='nw',side='left',padx=0,pady=0)
        self.eh=StringVar()
        entry=Entry(roth,textvariable=self.eh,width=18)
        entry.pack(anchor='nw',side='left',padx=0,pady=0)
        csh=Button(roth,text='初始化',command=self.OnNext)
        csh.pack(anchor='nw',padx=0,pady=40)
    def OnNext(self):
		print 'eth0:',self.e.get() 
		print 'eth1:',self.e1.get() 
		print 'host:',self.eh.get() 
		win = MyWindowsecond()
		self.root.destroy()
class MyWindowsecond():
    def __init__(self):
		self.root=Tk()
		self.root.title('Dcloud环境部署管理平台')
		self.root.geometry('350x250+500+250')
		labtops=Label(self.root,text="初始化配置环境")
		labelsfont = ('courier', 10, 'bold')
		labtops.config(font=labelsfont)
		labtops.pack(side='top',pady=0)
		self.label = Label(self.root, bd=1, relief=SUNKEN, anchor=W)
		self.label.config(width=40,height=1)
		self.label.pack(anchor='nw',padx=60,pady=10)
		self.kt=Label(self.root,bd=1,relief=SUNKEN,anchor=NW,width=40,height=8)
		self.kt.pack()
		ks=Button(self.root,text='开始',command=self.test)
		ks.pack(side='right')
    def infos(self,infos):
		self.kt.insert(INSERT,'['+str(time.time())+']'+str(infos)+'\n')
		time.sleep(1)
#    def test(self):
#		self.infos('test')
    def settext(self):
    	for i in range(58):
    		self.st(str(i))
    		time.sleep(0.1)
    def st(self,format, *args):
        self.kt.config(text=format % args)
        self.kt.update_idletasks()
    def set(self, format, *args):
        self.label.config(text=format % args)
        self.label.update_idletasks()
    def clear(self):
        self.label.config(text="")
        self.label.update_idletasks()
    def test(self):
		for i in range(58):
			self.set('|'*i)
			self.st(str(i)+'\n'+str(i))
			time.sleep(0.1)
win = MyWindow()
win.root.mainloop()
