#PROJECT
import tldextract
from bs4 import BeautifulSoup
import os
import requests
from app import email_address
from app import dynamic_websites
import sys
from termcolor import cprint
from app import man_page
import shutil

#####################################################################################################################################################################
c=""
def start(url): 
    global c  #To make folder "ext.domain" and change current working directory to this folder
    ext=tldextract.extract(url)
    try:
        os.mkdir(ext.domain)
        os.chdir(ext.domain)
    except:
        os.chdir(ext.domain)
    c=ext.domain
def folder_making(sr):
        try:
            os.mkdir(f"./{sr}")
            os.chdir(f"./{sr}")
        except:
            os.chdir(f"./{sr}")
def creating_saving_files(lst,strng,l):
    folder_making(strng)
    f=open(f"{strng}_{l}.txt","a")
    for element in lst:
        if(element == None):
            continue
        elif("http" in element or "https" in element):
            f.write(element + "\n")
        else:
            f.write(url+element + "\n")
    f.close()
    os.chdir("./..")
def saving_files(lst,strng,l):
    os.chdir(f"./{strng}")
    f=open(f"{strng}_{l}.txt","a")
    #print(lst)
    for element in lst:
        #print(element)
        if(element == None):
            continue
        elif("http" in str(element) or "https" in str(element)):
            f.write(element + "\n")
        else:
            f.write(url+element + "\n")
    f.close()
    os.chdir("./..")


def link(lst,tag,attribute,file_name,l,soup):  
    global c
    global url
    a=list()
    a=[] 
    if(lst != [] and lst != None and tag != "img"):
        for element in lst:
            try:
                client1=requests.get(element)
                soup1=BeautifulSoup(client1.text)
                links = soup1.findAll(tag)
                for link in links:
                    if(link.get(attribute) not in a):
                        a.append(link.get(attribute))
            except:
                continue
        saving_files(a,file_name,l)
        return(a)               
    elif(l==1):
        links = soup.findAll(tag) 
        lst=[]      #to convert none type to empty list
        for link in links:
            if(link.get(attribute) not in lst):
                lst.append(link.get(attribute))
        creating_saving_files(lst,file_name,l)
        return(lst)
    else:
        cprint("No %s found"%(file_name),"red")





if("-help" in sys.argv ):
    cprint("A CLI tool for web crawling  and scrapping. Use following flags as needed:","red")
    print("Usage:",end=" ")
    print("WCSC.py [-l] [-d]")
    cprint("\t-url","green",end="          ")
    print("=",end=" ")
    cprint("URL of website to Scrap","cyan")
    cprint("\t-depth","green",end="          ")
    print("=",end=" ")
    cprint("for entering depth value while scrapping","cyan")
    print("Optional Flags:")
    cprint("\t-h or head","green",end="     ")
    print("=",end=" ")
    cprint("for printing headers to stdout","cyan")
    cprint("\t-img or images","green",end=" ")
    print("=",end=" ")
    cprint("for printing images to stdout","cyan")
    cprint("\t-l or link","green",end="     ")
    print("=",end=" ")
    cprint("for printing links to stdout","cyan")
    cprint("\t-m or mails","green",end="    ")
    print("=",end=" ")
    cprint("for printing mails to stdout","cyan")
    cprint("\t-help","green",end="          ")
    print("=",end=" ")
    cprint("for help","cyan")
    sys.exit()
if("man" in sys.argv):
    man_page.man_page()
    sys.exit()

if( __name__ == '__main__'):
    url=sys.argv[(sys.argv).index("-url")+1]
    if(len(sys.argv)>=3):
        depth=int(sys.argv[(sys.argv).index("-depth")+1])
    else:
        depth=1

url=""
def crawl(urll,depth,headers,images,links,mails):    
    url=urll
    start(url)
    burp0_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36","Accept-Encoding": "gzip, deflate"}
    client=requests.get(url,headers=burp0_headers)
    soup=BeautifulSoup(client.text)
    lst=list()
    lst1=list()
    strngs=list() #to store "link.string" to name screenshots
    l=0
    # cprint("Collecting Headers.....","yellow",attrs=["bold","blink"])
    if(headers != 0):
        try:
            os.mkdir("./Headers")
            os.chdir("./Headers")
        except:
            os.chdir("./Headers")
        with open("Headers.txt","w") as f:
            f.write(str(client.headers))
            f.close()
            os.chdir("./..")    


    while(depth!=l):
        l+=1
        lst=link(lst,"a","href","links",l,soup)
        lst1=link(lst1,"img","src","images",l,soup)

    cprint("Collecting Emails (if any) available on the website","yellow")
    if(mails!=0):
        email_address.mails(url)


    f=open("./links/links_1.txt","r")
    lst=[]
    cprint("#######################","red")
    if(f.read() == ''):
        f.close()
        # for i in range(1,depth+1):
            # lst=dynamic_websites.get(url,lst,depth,"a","href",c,"links",i)
            # lst1=dynamic_websites.get(url,lst1,1,"img","src",c,"images",i)
    print("--",os.getcwd())
    os.chdir(".//..")
    shutil.make_archive("report", 'zip', os.getcwd()+"//"+c)
    # os.chdir(".\\..")
    return(c)
    
