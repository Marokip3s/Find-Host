# -*- coding=utf-8 -*-

#qpy:console

from __future__ import print_function

import urllib2, socket, os, glob

def Http():

    for i in satir:

        kd=str(i)

        sira=kd.find(" ")

        host=kd[:sira]

        print(host)

        urllib2.install_opener(urllib2.build_opener(urllib2.ProxyHandler({"http":"turbohide.com:80"})))

        try:

            site="http://"+host

            urllib2.urlopen(site)

            print("OLUMLU")

        except Exception:

            print("FAILED")

def Host():

    for i in satir:

        kd=str(i)

        sira=kd.find(" ")

        host=kd[:sira]

        print(host)

        request= urllib2.Request("http://turbohide.com", headers={"Host" : host})

        try:

            urllib2.urlopen(request)

            print("OLUMLU")

        except Exception:

            print("FAILED")

def XOnlineHost():

    for i in satir:

        kd=str(i)

        sira=kd.find(" ")

        host=kd[:sira]

        print(host)

        request= urllib2.Request("http://turbohide.com", headers={"X-Online-Host" : host})

        try:

            urllib2.urlopen(request)

            print("OLUMLU")

        except Exception:

            print("FAILED")

def Referer():

    for i in satir:

        kd=str(i)

        sira=kd.find(" ")

        host=kd[:sira]

        print(host)

        request= urllib2.Request("http://turbohide.com", headers={"Referer" : host})

        try:

            urllib2.urlopen(request)

            print("OLUMLU")

        except Exception:

            print("FAILED")

def IpAddress():

    site= raw_input("pleas put your ip address:  ")

    try:

            qw= str(socket.gethostbyname(site))

            print(site+"'nin ip adresi:  "+qw)

    except Exception:

            print(site+"'nin ip adresi bulunamadi.")

            quit()



    sira= qw.rfind(".")

    ucnokta= qw[:sira+1]

    dosya="/sdcard/"+ucnokta+".txt"

    k2= open(dosya, "w")

    for i in range(256):

                    a= str(i)

                    try:

                            print(socket.gethostbyaddr(ucnokta+a)[0])

                            ip= str(socket.gethostbyaddr(ucnokta+a)[2])

                            uznlk= len(ip)

                            ip= ip[2:uznlk-2]

                            print(socket.gethostbyaddr(ucnokta+a)[0]+" "+ip, end="\n", file=k2)

                    except Exception:

                            print(ucnokta+a+" No find Host.")

    k2.close()

print ('''\033[1m\033[93m[\033[91m!\033[93m] Tools Find IP Host Python \n \>

 /$$$$$$ /$$$$$$$        /$$   /$$                       /$$

|_  $$_/| $$__  $$      | $$  | $$                      | $$

  | $$  | $$  \ $$      | $$  | $$  /$$$$$$   /$$$$$$$ /$$$$$$

  | $$  | $$$$$$$/      | $$$$$$$$ /$$__  $$ /$$_____/|_  $$_/

  | $$  | $$____/       | $$__  $$| $$  \ $$|  $$$$$$   | $$

  | $$  | $$            | $$  | $$| $$  | $$ \____  $$  | $$ /$$

 /$$$$$$| $$            | $$  | $$|  $$$$$$/ /$$$$$$$/  |  $$$$/

|______/|__/            |__/  |__/ \______/ |_______/    \___/

\033[1;34mAuthor \033[91m:\033[37m Marokip3s

 ''')
 
print(" This Script it's Trick Free Internet In Your Own Sim Card ")

secim=raw_input("Welecome To Find Host\nHttp Test Number 1:\nHost Test Number 2:\nXOnlineHost Test Number 3:\nReferer Test Number 4:\nHost ip  Number 5 Take it:    ")



if secim=="5":

                IpAddress()

if secim=="1":

                print("The file you will choose must be created with the IP Scan method.", "ve /sdcard/ must be in the directory.", end="\n")

                os.chdir("/sdcard/")

                glo=glob.glob("*.txt")

                print(glo)

                kac=raw_input("how many files?:    ")

                kac1=int(kac)

                dosya=glo[kac1-1]

                locat="/sdcard/"+file

                oku= open(locat, "r")

                satir= oku.readlines() 

                Http()

if secim=="2":

                print("The file you will choose must be created with the IP Scan method.", "ve /sdcard/ must be in the directory.", end="\n")

                os.chdir("/sdcard/")

                glo=glob.glob("*.txt")

                print(glo)

                kac=raw_input("how many files?:    ")

                kac1=int(kac)

                dosya=glo[kac1-1]

                locat="/sdcard/"+file

                oku= open(locat, "r")

                satir= oku.readlines() 

                Host()

if secim=="3":

                print("The file you will choose must be created with the IP Scan method.", "ve /sdcard/ must be in the directory.", end="\n")

                os.chdir("/sdcard/")

                glo=glob.glob("*.txt")

                print(glo)

                kac=raw_input("how many files?:    ")

                kac1=int(kac)

                dosya=glo[kac1-1]

                locat="/sdcard/"+file

                oku= open(locat, "r")

                satir= oku.readlines() 

                XOnlineHost()

if secim=="4":

                print("The file you will choose must be created with the IP Scan method.", "ve /sdcard/ must be in the directory.", end="\n")

                os.chdir("/sdcard/")

                glo=glob.glob("*.txt")

                print(glo)

                kac=raw_input("how many files?:    ")

                kac1=int(kac)

                dosya=glo[kac1-1]

                locat="/sdcard/"+file

                oku= open(locat, "r")

                satir= oku.readlines() 

                Referer() 
