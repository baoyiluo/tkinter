#coding:utf-8
import Tkinter as tk
from Tkinter import *
import threading
import time
import os
lock=threading.Lock()
class MyWindow():
    def __init__(self,ethdata=[],bonddata={}):
        if ethdata==[]:
	    ethdata=os.popen('/sbin/ifconfig -a|/bin/grep eth').read().split('\n')
            ethdata.pop()
            for i in range(len(ethdata)):
                ethdata[i]=ethdata[i].split()[0]
        self.ethdata=ethdata
        self.bonddata=bonddata
        self.root=tk.Tk()
        self.te={}
        self.root.title('Dcloud环境部署管理平台')
        self.root.geometry('450x'+str(280+len(self.ethdata)*20)+'+500+250')
        labtop=Label(self.root,text="初始化本机环境")
        labelfont = ('courier', 10, 'bold')
        labtop.config(font=labelfont)
        labtop.pack(side='top',pady=10)
        
        labip=Label(self.root,text="IP:")
        labipfont = ('courier', 8,'bold')
        labip.config(font=labipfont)
        labip.pack(anchor='nw',padx=70,pady=10)
        rot={} 
        self.chs={}
        for i in range(len(self.ethdata)):
            rot[i]=Frame(self.root)
            rot[i].pack(anchor='nw',padx=80,pady=0)
            self.chs[i]=IntVar()
            labe0=Checkbutton(rot[i],variable=self.chs[i],text=self.ethdata[i])
            labe0font = ('courier', 6,'bold')
            labe0.config(font=labe0font)
            labe0.pack(anchor='nw',side='left',padx=0,pady=0)
            self.te[i]=StringVar()
            entry=Entry(rot[i],textvariable=self.te[i])
            entry.pack(anchor='nw',side='left',padx=0,pady=0)
        csh=Button(self.root,text='绑定指定网卡',command=self.OnBond)
        csh.pack(anchor='ne',padx=160,pady=20)
        roth=Frame(self.root)
        roth.pack(anchor='nw',padx=70,pady=10)
        labhost=Label(roth,text="主机名:")
        labhost.config(font=labipfont)
        labhost.pack(anchor='nw',side='left',padx=0,pady=0)
        self.eh=StringVar()
        entry=Entry(roth,textvariable=self.eh,width=18)
        entry.pack(anchor='nw',side='left',padx=0,pady=0)
        csh=Button(roth,text='初始化',command=self.OnNext)
        csh.pack(anchor='nw',padx=0,pady=40)
    def OnBond(self):
        bondlist=[]
        for i in range(len(self.ethdata)):
            if self.chs[i].get()==1:  
                bondlist.append(self.ethdata[i])
        self.root.destroy()
        win = MyWindowbond(bondlist,self.ethdata,self.bonddata)
    def OnNext(self):
        for i in range(len(self.ethdata)):
            os.system("/bin/echo DEVICE="+self.ethdata[i]+">/etc/sysconfig/network-scripts/ifcfg-"+self.ethdata[i])
            install="""
/bin/sed -i '$a ONBOOT=yes' /etc/sysconfig/network-scripts/ifcfg-"""+self.ethdata[i]+""" 
/bin/sed -i '$a BOOTPROTO=static' /etc/sysconfig/network-scripts/ifcfg-"""+self.ethdata[i]+""" 
/bin/sed -i '$a IPADDR="""+self.te[i].get()+"""' /etc/sysconfig/network-scripts/ifcfg-"""+self.ethdata[i] 
            os.system(install)
            hostn=os.popen("/bin/cat /etc/sysconfig/network|/bin/grep HOSTNAME").read().split("=")[-1][0:-1]
            installh="""
/bin/sed -i '/HOSTNAME=/ s/"""+hostn+"""/"""+self.eh.get()+"""/' /etc/sysconfig/network
/bin/hostname """+self.eh.get()
            os.system(installh)
            print self.ethdata[i]+':',self.te[i].get()
        win = MyWindowsecond()
        self.root.destroy()
class MyWindowbond():
    def __init__(self,bondlist,ethdata,bonddata={}):
        self.ethnb=list(set(ethdata)-set(bondlist))
        self.root=Tk()  
        self.bondlist=bondlist
        self.bonddata=bonddata
        self.ethdata=ethdata
        self.root.title('Dcloud环境部署管理平台')
        self.root.geometry('400x250+500+250')
        labtops=Label(self.root,text="绑定指定网卡")
        labelsfont = ('courier', 10, 'bold')
        labtops.config(font=labelsfont)
        labtops.pack(side='top',pady=0)

        labbond=Label(self.root,text="bond"+str(len(bonddata))+" "+str(bondlist))
        labbondfont = ('courier', 6, 'bold')
        labbond.config(font=labelsfont)
        labbond.pack(side='top',pady=0)

        frameip=Frame(self.root) 
        frameip.pack(anchor='nw',padx=80,pady=0)
        labip=Label(frameip,text="IP:      ")
        labeipfont = ('courier', 8,'bold')
        labip.config(font=labeipfont)
        labip.pack(anchor='nw',side='left',padx=0,pady=0)
        self.ip=StringVar()
        entryip=Entry(frameip,textvariable=self.ip)
        entryip.pack(anchor='nw',side='left',padx=0,pady=0)

        self.framegateway=Frame(self.root) 
        self.framegateway.pack(anchor='nw',padx=80,pady=0)
        labgateway=Label(self.framegateway,text="网关:    ")
        labgateway.config(font=labeipfont)
        labgateway.pack(anchor='nw',side='left',padx=0,pady=0)
        self.gateway=StringVar()
        entrygateway=Entry(self.framegateway,textvariable=self.gateway)
        entrygateway.pack(anchor='nw',side='left',padx=0,pady=0)

        self.framedns=Frame(self.root) 
        self.framedns.pack(anchor='nw',padx=80,pady=0)
        labdns=Label(self.framedns,text="DNS:     ")
        labdns.config(font=labeipfont)
        labdns.pack(anchor='nw',side='left',padx=0,pady=0)
        self.dns=StringVar()
        entrydns=Entry(self.framedns,textvariable=self.dns)
        entrydns.pack(anchor='nw',side='left',padx=0,pady=0)

        self.framenetmask=Frame(self.root) 
        self.framenetmask.pack(anchor='nw',padx=80,pady=0)
        labnetmask=Label(self.framenetmask,text="子网掩码:")
        labnetmask.config(font=labeipfont)
        labnetmask.pack(anchor='nw',side='left',padx=0,pady=0)
        self.netmask=StringVar()
        entrynetmask=Entry(self.framenetmask,textvariable=self.netmask)
        entrynetmask.pack(anchor='nw',side='left',padx=0,pady=0)

        subb=Button(self.root,text='绑定',command=self.subOnBond)
        subb.pack(anchor='ne',padx=160,pady=20)
    def subOnBond(self):
        os.system("/etc/init.d/NetworkManager stop")
        for i in range(len(self.bondlist)):
            install="""
/bin/echo DEVICE="""+self.bondlist[i]+""">/etc/sysconfig/network-scripts/ifcfg-"""+self.bondlist[i]+"""
/bin/sed -i '$a ONBOOT=yes' /etc/sysconfig/network-scripts/ifcfg-"""+self.bondlist[i]+""" 
/bin/sed -i '$a BOOTPROTO=none' /etc/sysconfig/network-scripts/ifcfg-"""+self.bondlist[i]+""" 
/bin/sed -i '$a MASTER=bond"""+str(len(self.bonddata))+"""' /etc/sysconfig/network-scripts/ifcfg-"""+self.bondlist[i]+""" 
/bin/sed -i '$a SLAVE=yes' /etc/sysconfig/network-scripts/ifcfg-"""+self.bondlist[i] 
            os.system(install)
        installbond="""
/bin/echo DEVICE=bond"""+str(len(self.bonddata))+""">/etc/sysconfig/network-scripts/ifcfg-bond"""+str(len(self.bonddata))+"""
/bin/sed -i '$a ONBOOT=yes' /etc/sysconfig/network-scripts/ifcfg-bond"""+str(len(self.bonddata))+""" 
/bin/sed -i '$a BOOTPROTO=static' /etc/sysconfig/network-scripts/ifcfg-bond"""+str(len(self.bonddata))+""" 
/bin/sed -i '$a IPADDR="""+self.ip.get()+"""' /etc/sysconfig/network-scripts/ifcfg-bond"""+str(len(self.bonddata))+""" 
/bin/sed -i '$a GATEWAY="""+self.gateway.get()+"""' /etc/sysconfig/network-scripts/ifcfg-bond"""+str(len(self.bonddata))+""" 
/bin/sed -i '$a DNS1="""+self.dns.get()+"""' /etc/sysconfig/network-scripts/ifcfg-bond"""+str(len(self.bonddata))+""" 
/bin/sed -i '$a NETMASK="""+self.netmask.get()+"""' /etc/sysconfig/network-scripts/ifcfg-bond"""+str(len(self.bonddata))
        os.system(installbond)
        ethbond=''
        for j in self.bondlist:
            ethbond+=' '+j
        os.system("/bin/sed -i '$a ifenslave bond"+str(len(self.bonddata))+ethbond+"' /etc/rc.d/rc.local")
        installconfig="""
/bin/sed -i '$a alias bond"""+str(len(self.bonddata))+""" bonding' /etc/modprobe.d/dist.conf
/bin/sed -i '$a options bond"""+str(len(self.bonddata))+""" miimon=100 mode=0' /etc/modprobe.d/dist.conf
        """
        os.system(installconfig)
        os.system("/etc/init.d/network restart")
        self.bonddata['bond'+str(len(self.bonddata))]=self.bondlist
        win = MyWindow(ethdata=self.ethnb,bonddata=self.bonddata)
        self.root.destroy()
        
class MyWindowsecond():
    def __init__(self):
        self.root=Tk()
        self.root.title('Dcloud环境部署管理平台')
        self.root.geometry('400x250+500+250')
        labtops=Label(self.root,text="初始化配置环境")
        labelsfont = ('courier', 10, 'bold')
        labtops.config(font=labelsfont)
        labtops.pack(side='top',pady=0)
        self.label = Label(self.root, bd=1, relief=SUNKEN, anchor=W)
        self.label.config(width=40,height=1)
        self.label.pack()
        self.kt=Label(self.root,bd=1,relief=SUNKEN,anchor=NW,width=40,height=8)
        self.kt.pack(side='top',pady=10)
        ks=Button(self.root,text='开始',command=self.test)
        ks.pack(side='right')
    def infos(self,infos):
        self.kt.insert(INSERT,'['+str(time.time())+']'+str(infos)+'\n')
        time.sleep(1)
# def test(self):
# self.infos('test')
    def settext(self):
        for i in range(81):
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
        for i in range(81):
            self.set('|'*i)
            self.st(str(i)+'\n'+str(i))
            time.sleep(0.1)
win = MyWindow()
win.root.mainloop()
