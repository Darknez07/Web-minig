import requests
from bs4 import BeautifulSoup
import sys
import csv
import urllib
import os
# url
l = []
for pagen in range(1,9):
    url = 'https://www.flipkart.com/laptops/pr?sid=6bo,b5g&otracker=categorytree&fm=neo%2Fmerchandising&iid=M_810cfc79-58c9-4943-879c-29b77ccab275_2_372UD5BXDFYS_MC.F6KJFVU7EOGS&otracker=hp_rich_navigation_1_2.navigationCard.RICH_NAVIGATION_Electronics~Laptop%2Band%2BDesktop~All_F6KJFVU7EOGS&otracker1=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_1_L2_view-all&cid=F6KJFVU7EOGS&page={}'.format(pagen)
    # Get Page
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0"}
    page = requests.get(url,headers=headers)
    if page.status_code != 200:
        print("Website not reachable")
        sys.exit()

    # Scrape
    soup = BeautifulSoup(page.content,'html.parser')
    print(soup.title.text)
    divs = soup.find_all("div",{"class":"_3pLy-c row"})
    for tag in divs:
        lis = tag.find_all("li")
        divin = tag.find_all("div",{"class":"col col-7-12"})[0]
        info = divin.find_all("div")
        price = tag.find_all("div",{"class":"_30jeq3 _1_WHN1"})[0].text
        off = tag.find_all("div",{"class":"_3Ay6Sb"})
        try:
            off = off[0].find('span').text
        except:
            if off is []:
                off = "0% off"
        count = 0
        product = dict()
        for inf in info:
            if count == 2:
                continue
            if count == 1:
                try:
                    product["Product Rating"] = float(inf.text[:4])
                except:
                    product["Product Rating"] = 4
            elif count == 0:
                product["Product Name"] = inf.text
            count+=1
        product["Product Price in Rs"] = price[1:]
        product["Product Discount"] = off
        dis = []
        for li in lis:
            dis.append(li.text)
        product["Product Description"] = dis
        l.append(product)
# imgs = soup.find_all('img',{"class":"_396cs4 _3exPp9"})
# # print(imgs)
# count = 0
# for img in imgs:
#     imgUrl = img['src']
#     print(imgUrl)
#     urllib.request.urlretrieve(imgUrl,os.path.basename("img"+str(count)+".jpg"))
#     count+=1

keys = l[0].keys()
with open('Product.csv','w',newline='') as op:
    dict_writer = csv.DictWriter(op,keys)
    dict_writer.writeheader()
    dict_writer.writerows(l)