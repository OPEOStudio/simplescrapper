#Necessary packages

import Headscrap
import individualscrap
import json
import time

#Parameters

baseurl2 = "https://www.sous-traiter.com/annuaire/liste.php?&page="
number_loop2 = 91 #number of pages in the adress book
beginning2 = "societe-" #beginning of the URLs
end2 = ".html" #end of the URLs
timing2 = 1 #number of seconds between each URL call, headscrap
timing3 = 1 #number of seconds between each URL call, individual scrap

#Configuration for headscrap

def createunits(list,timing):
    result=[]
    for i in list:
        result.append(individualscrap.create_unit(str(i)))
        time.sleep(timing)
    return result

#Creation of the final database using the headscrap to create the list of url
#and using the individualscrap to create, inside the big list, units

def createfulldatabase(baseurl,number_loop,beginning,end,timing_principal,timing_secondary):
    urllist = Headscrap.foo(baseurl,number_loop,beginning,end,timing_principal)
    units = createunits(urllist,timing_secondary)
    return units

#Output is fulldb

fulldb = createfulldatabase(baseurl2,number_loop2,beginning2,end2,timing2,timing3)

#Dumping the final db into an ordered json

print(fulldb)

with open('output.json', 'w') as outfile:
    json.dump(fulldb, outfile)
