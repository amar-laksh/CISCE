import requests as r
import urllib as u
import re


"""
This is a simple script that is unfortunately, able to scrape the details of all the schools of CISCE board of eduction across multiple nations.
COUNTRY CODES
2 - INDIA
3 - INDONESIA
6 - SINGAPORE
7 - UNITED ARAB EMIRATES

STATE CODES FOR INDIA
5-38 - ASSAM TO WEST BENGAL
3696 - TELANGANA

STATE CODES FOR INDONESIA
2 - ALL STATES

STATE CODES FOR SINGAPORE
33 - ALL STATES

STATE CODES FOR UAE
12 - DUBAI
31 - SHARJAH
"""
def search_database(country,state):
    url = "http://www.cisce.org/locate-search.aspx?country="+str(country)+"&state="+str(state)+"&dist=0&city=0&location=&schooltype=&cve=&isc=&icse=&schoolclassi=&school=&search=locate"
    filename = "./"+str(state)+".html"
    u.urlretrieve(url,filename)
    print "--->",filename


    
    
def get_emails(startState,endState):
    from BeautifulSoup import BeautifulSoup
    import urllib2
    emails = []
    for i in range(startState,endState):
        filename = r"./"+str(i)+".html"
        #print filename
        #print i
        page = open(filename)
        soup = BeautifulSoup(page)
        x = soup.findAll("div")
        #attrs={"id":"ctl00_ctl00_Cphcontent_Cphleftcontent_rptsearch_ctl00_Div3"})
        y = re.findall(r'<div id=.*?v3.*>(\[.*?\].*?@.*?)</div>',str(x))
        for i in y:
            i = i[3:]
            emails.append(i)
    return emails

gm = 0
ym = 0
hot = 0
bsnl = 0

def statistics(this):
    global gm
    global ym
    global hot
    global bsnl
    for i in this:
        if "gmail.com" in i:
            gm = gm + 1
        elif "yahoo.com" in i:
            ym = ym + 1
        elif "hotmail.com" in i:
            hot = hot + 1
        elif "bsnl.in" in i:
            bsnl = bsnl + 1
    print "Google emails: ",gm
    print "Yahoo emails: ",ym
    print "Hotmail emails: ",hot
    print "Bsnl emails: ",bsnl
    print "Total emails: ",len(this)
    



def create_csv(result):
    for i in result:
        f = open('emails.csv','a')
        f.write(i+"\n")
        f.close()
    print "Total Mails",len(result)

for i in range(5,38):
    search_database(2,i)
    
result = get_emails(5,38)
create_csv(result)
statistics(result)
