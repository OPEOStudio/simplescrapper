#Necessary packages

import urllib.request as request
import re
import time
import csv

baseurl2 = "https://www.sous-traiter.com/annuaire/liste.php?&page="
number_loop2 = 93
beginning2 = "societe-"
end2 = ".html"
timing2 = 1

#There are two sources of information

# The main page, annuaire, https://www.sous-traiter.com/annuaire/liste.php
# goes from page 1 (https://www.sous-traiter.com/annuaire/liste.php?&page=2)
# to page 95 (https://www.sous-traiter.com/annuaire/liste.php?&page=95
# It contains all the links to the pages that we are going to actually scrap
# So first objective is to put all the links into a big array
# This file is for the first objective
# The file for the individual scrap is individualscrap.py

# Take all html from a website
def takeallhtml(website):
    web = request.urlopen(website)
    html = web.read().decode('latin-1')
    return html

# Find the first link with a beginning and an end
def findfirstlink(html,beginning,end):
    start_link=html.find(beginning)
    if start_link==-1:
        return None,0
    else:
        end_link=html[start_link:].find(end)
        real_end=start_link+end_link
        name=html[start_link:real_end]
        return name,real_end

# Find all links on that model
def findalllinks(html,beginning,end):
    links=[]
    html2=html
    while findfirstlink(html2,beginning,end)[1]!=0:
        links.append(findfirstlink(html2,beginning,end)[0])
        html2=html2[findfirstlink(html2,beginning,end)[1]:]
    return(links)

#loop urls based on the same principle
def url_looping(baseurl,number_loop):
    urls=[]
    for i in range(number_loop):      # Number of pages plus one
        url = baseurl +format(i)
        urls.append(url)
    return urls

#create one big array

def foo(baseurl,number_loop,beginning,end,timing):
    urls = url_looping(baseurl,number_loop)
    htmls = []
    for i in urls:
        htmls.append(takeallhtml(i))
        time.sleep(timing)
    links = []
    for j in htmls:
        links.append(findalllinks(j,beginning,end))
    finalink = []
    for i in links :
        for j in i :
            k="https://www.sous-traiter.com/annuaire/"+j+".html"
            finalink.append(k)
    return finalink

#note : 27 (30) seconds to run for 3. So probably 950 seconds for the

urllist = foo(baseurl2,number_loop2,beginning2,end2,timing2)
