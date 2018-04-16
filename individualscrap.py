#Necessary packages

import urllib.request as request
import re
import time

#There are two sources of information

# The main page, annuaire, https://www.sous-traiter.com/annuaire/liste.php
# goes from page 1 (https://www.sous-traiter.com/annuaire/liste.php?&page=2)
# to page 95 (https://www.sous-traiter.com/annuaire/liste.php?&page=95
# It contains all the links to the pages that we are going to actually scrap
# So first objective is to put all the links into a big array
# This file is for the first objective
# The file for the individual scrap is individualscrap.py

# Take all html from a website
# We had to handle exceptions
def takeallhtml(website):
    try :
        web = request.urlopen(website)
        html = web.read().decode('latin-1')
    except urllib.error.HTTPError:
        html = []
        print("error in opening"+website)
    return html

# Find the first part with a beginning and an end
# This is similar (but not exactly the same) as scrapy base features
def findfirstlink(html,beginning,end):
    start_link=html.find(beginning)
    if start_link==-1:
        return None,0
    else:
        end_link=html[start_link:].find(end)
        if end_link==-1:
            return None,0
        real_end=start_link+end_link
        name=html[start_link+len(beginning):real_end]
        return name,real_end

# Find all info on that model
def findallinks(html,beginning,end):
    links=[]
    html2=html
    while findfirstlink(html2,beginning,end)[1]!=0:
        links.append(findfirstlink(html2,beginning,end)[0])
        html2=html2[findfirstlink(html2,beginning,end)[1]:]
    return(links)

def structureinsidelilnks(html,beginning,end,insidebeginning,insideend):
    text = str(findallinks(html,beginning,end))
    return(findallinks(text,insidebeginning,insideend))

# Now we are going to put the information structured, page
# By inspecting the HTML code we can find several infos

keywords_beginning = "<meta name=\"keywords\" content="
keywords_end = ">"
insidekeywords_beginning = ","
insidekeywords_end = ","

title_beginning = "<title>"
title_end = "- Sous-traiter.com</title>"

address_beginning = "itemprop=\"streetAddress\">"
address_end = "</span><br/><sp"

postalcode_beginning = "itemprop=\"postalCode\">"
postalcode_end = "</span> <span"

phone_beginning = "<span itemprop=\"telephone\" class=\"subtitle\">"
phone_end = "</span></div>"

fax_beginning = "<h3>Fax<span class=\"subtitle\">"
fax_end = "</span></h3>"

materials_beginning = "es</h3>"
materials_end = "</ul>"
insidematerials_beginning = "icon-caret-right\"></i>"
insidematerials_end = "</li>"

equipe_beginning = "quipe</h3>"
equipe_end = "</ul>"
insideequipe_beginning = "</i><b>"
insideequipe_end = "</li>"

knowhow_beginning = "<h3>Savoir-faire</h3>"
knowhow_end = "</div>"
insideknowhow_beginning = "x80¢"
insideknowhow_end ="<br />"

filieres_beginning = "res</h3>"
filieres_end = "</div>"
insidefilieres_beginning = "</i>"
insidefilieres_end = "</li>"

Juridic_beginning = "<li><i class=\"icon-caret-right\"></i> Forme juridique :"
Juridic_end = "</li>"

CA_beginning = "affaire HT :"
CA_end = "</li>"

NAF_beginning = "</i> Code NAF :"
NAF_end = "</li>"

email_beginning = "Email : <a href=\"mailto:"
email_end = "\">"

Effectif_beginning = "ffectif total</b> :"
Effectif_end = "</li>"

Machines_beginning = "<h4>Equipements informatiques</h4>"
Machines_end = "</article>"
insidemachines_beginning = "x80"
insidemachines_end = "x80"

Agrements_beginning = "ents et certifications</h4>"
Agrements_end = "</article>"

test_url="https://www.sous-traiter.com/annuaire/societe-galvanoplastie-53960-bonchamp-les-laval-7995.html"

def create_unit(url):
    html = takeallhtml(url)
    title = findallinks(html,title_beginning,title_end) #check
    keywords = structureinsidelilnks(html,keywords_beginning,keywords_end,insidekeywords_beginning,insidekeywords_end) #NA
    address = findallinks(html,address_beginning,address_end) #check
    phone = findallinks(html,phone_beginning,phone_end) #check
    fax = findallinks(html,fax_beginning,fax_end) #check
    CA = findallinks(html,CA_beginning,CA_end) #not really functional
    NAF = findallinks(html,NAF_beginning,NAF_end) #functional, when present
    Juridic = findallinks(html,Juridic_beginning,Juridic_end) #functional
    filieres = structureinsidelilnks(html,filieres_beginning,filieres_end,insidefilieres_beginning,insidefilieres_end) #functional
    knowhow = structureinsidelilnks(html,knowhow_beginning,knowhow_end,insideknowhow_beginning,insideknowhow_end) #functional
    equipe = structureinsidelilnks(html,equipe_beginning,equipe_end,insideequipe_beginning,insideequipe_end) #functinalo
    email = findallinks(html,email_beginning,email_end) #functional
    effectif = findallinks(html,Effectif_beginning,Effectif_end) #functional
    machine = findallinks(html,Machines_beginning,Machines_end) #somewhat functional
    agrements = findallinks(html,Agrements_beginning,Agrements_end) #somewhat functional
    return title,keywords,address,phone,fax,CA,NAF,Juridic,filieres,knowhow,equipe,email,effectif,machine,agrements

#html = takeallhtml(test_url)

#print(create_unit(test_url))
