from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup
import time
import keyboard
import os
from termcolor import cprint
from selenium.webdriver.chrome.options import Options
#def start(url):
import os



def fun(urls,dir_name):
    k=1    
    for element in urls:
        name_of_ss=k  ############################### COMPLETE THIS
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')        
        driver=webdriver.Chrome(executable_path=(os.getcwd()+"\\..\\chromedriver.exe"),chrome_options=chrome_options)
        time.sleep(2)

        try:
            driver.get(element)
            driver.maximize_window()
            print(os.getcwd(),"%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%_dynamic_website _____")
            driver.save_screenshot(os.getcwd() + "/Screen-Shots/" + str(name_of_ss) + "_ss.png")
            driver.close()
        except:
            driver.close()
        if(k%10==0):
            ans=input("take more ss?(y/n):")
            if( ans =="Y" or ans =="y"):
                continue
            else:
                break
        k+=1

def get(url,lst,depth,tag,attribute,c,name_file,k):
    print(c)
    strngs=[]
    if( (lst==[] or lst == None) and k==1):
        f=open(f"./{name_file}/{name_file}_{k}.txt","w")
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        print(os.getcwd()+"\\..\\app\\chromedriver.exe")        
        driver=webdriver.Chrome(executable_path=os.getcwd()+"\\..\\chromedriver.exe",chrome_options=chrome_options)
        driver.get(url)
        elem = driver.find_elements_by_tag_name(tag)
        for lnk in elem:
            if(lnk.get_attribute(attribute) != None and lnk.get_attribute(attribute)  != ""):
                if(lnk.get_attribute(attribute) not in lst):
                    f.write(lnk.get_attribute(attribute)+"\n")
                    lst.append(lnk.get_attribute(attribute))
        f.close()
        driver.close()
        if(tag=="a"):
            fun(lst,c)
        return(lst)
    elif(k<=depth):
        k+=1
        for element in lst:
            f=open(f"./{file_name}/{file_name}_{k}.txt","w")
            chrome_options = Options()
            chrome_options.add_argument('--headless')
            chrome_options.add_argument('--no-sandbox')
            chrome_options.add_argument('--disable-dev-shm-usage')        
            driver=webdriver.Chrome(executable_path=os.getcwd()+"\\..\\chromedriver.exe",chrome_options=chrome_options)
            driver.get(element)
            elem = driver.find_elements_by_tag_name(tag)
            for lnk in elem:
                if(lnk.get_attribut(attribute) not in lst):
                    f.write(lnk.get_attribute(attribute)+"\n")
                    lst.append(lnk.get_attribute(attribute))
            driver.close()
            f.close()
            return(lst)

