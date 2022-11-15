
from bs4 import BeautifulSoup
from Utils import *

def parserForInformation(page_source):
    # HTML string we are going to scrap to print 
    # the discography of an artist/band
    soup = BeautifulSoup(page_source,"html.parser")
    #We get all the elements in the page that are of type table
    tables = BeautifulSoup.find_all(soup, "table")
    #We find all elements inside the second table in the HTML that are of type tr (rows)
    trs = BeautifulSoup.find_all(tables[0], "tr")
    data = "Year,name,Label\n"
    # print(tables)
    # print(tables)
    #We go through the different rows (each row is and album) of the table and for each row
    #(each album) we get the columns that contain the information we want to print
    #and we add the columns with the right information to our string "s" where we will
    #keep the information and print it
    for i in range(1,len(trs)):
        # print("k")
        tds = BeautifulSoup.find_all(trs[i], "td")
        print(tds)
        # print()
        for j in range(2,len(tds)-1):

            if (j == 2):
                s = deleteSpaces(tds[j].text)
                print("Year: "+s)
                data += s + ","
            elif(j !=5 and j!=6):
                s = deleteIntroTabs(tds[j].text)
                if(j == 4):
                    s = "Label: "+s
                print(s)
                data += s + ","
        data = data[:-1]
        data += "\n"
        print("\n")
        with open("data.csv","w") as f:
            f.write(data)
