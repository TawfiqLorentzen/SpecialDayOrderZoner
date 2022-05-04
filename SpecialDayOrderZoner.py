"""
Makes a big ol' csv for a special day like valentines or Dia de madres
Ideally this csv should be split by shop, and then I can do the rest from there.
"""

import re
import mechanicalsoup
import csv

chermside = [4035, 4010, 4051, 4054, 4007, 4060, 4034, 4066, 4036, 4014, 4065, 4034, 4006,
             4017, 4500, 4008, 4000, 4069, 4008, 4055, 4034, 4500, 4069, 4032, 4011, 4017,
             4009, 4037, 4051, 4053, 4055, 4018, 4006, 4051, 4034, 4031, 4051, 4007, 4011,
             4006, 4068, 4031, 4059, 4069, 4054, 4030, 4053, 4064, 4053, 4066, 4005, 4051,
             4006, 4013, 4014, 4012, 4064, 4000, 4008, 4069, 4059, 4017, 4067, 4053,
             4052, 4018, 4068, 4005, 4061, 4066, 4055, 4014, 4012, 4032, 4051, 5030, 4030,
             4034]

carindale = [4161, 4171, 4153, 4103, 4159, 4171, 5152, 4170, 4157, 4152, 4155, 4163, 4151,
             4102, 4169, 4103, 4120, 4154, 4171, 4174, 4101, 4169, 4179, 4178, 4179, 4105,
             4170, 4165, 4172, 4170, 4160, 4154, 4165, 4170, 4157, 4101, 4158, 4164, 4173,
             4165, 4154, 4160, 4101, 4152, 4102, 4207, 4178, 417]

northlakes = [4510, 4035, 4017, 4505, 4510, 4019, 4503, 4521, 4508, 4520, 4503, 4500, 4503,
              4021, 4503, 4501, 4509, 4510, 4506, 4503, 4504, 4020, 4509, 4502, 4022,
              4020, 4510, 4500, 4510, 4500, 4509, 4503, 4019]

garden = [4110, 4115, 4108, 4300, 4207, 4117, 4205, 4124, 4118, 4207, 4156, 4116,
          4130, 4133, 4068, 4075, 4130, 4132, 4127, 4076, 4007, 4116, 4077, 4207, 4207,
          4113, 4078, 4069, 4078, 4124, 4122, 4208, 4075, 4124, 4110, 4118, 4121, 4207,
          4077, 4074, 4117, 4112, 4110, 4114, 4207, 4129, 4131, 4109, 4156, 4122, 4132,
          4131, 4074, 4122, 4074, 4125, 4111, 4208, 4075, 4110, 4125, 4115, 4069, 4127,
          4301, 4020, 4118, 4077, 4074, 4109, 4123, 4106, 4113, 4017, 4073, 4128, 4075,
          4073, 4127, 4127, 4280, 4116, 4074, 4109, 4128, 4121, 4105, 4119, 4122, 4076,
          4133, 4122, 4074, 4110, 4207, 4122, 4113, 4105]

goldcoast = [4211, 4207, 4214, 4214, 4213, 4217, 4216, 4225, 4213, 4218, 4217, 4220, 4211,
             4226, 4225, 4216, 4209, 4223, 4221, 4211, 4211, 4210, 4212, 4211, 4216, 4212,
             4217, 4208, 4225, 4215, 4211, 4207, 4217, 4210, 4128, 4218, 4226, 4220, 4214,
             4214, 4212, 4213, 4211, 4218, 4208, 4211, 4210, 4211, 4221, 4216, 4217, 4209,
             4225, 4227, 4226, 4216, 4212, 4217, 4215, 4216, 4213, 4207, 4210, 4217, 4213,
             4228, 4211, 4217, 4224, 4209, 4227, 4209, 4210, 4213, 4207]

cherm_orders = []
garden_orders = []
carindale_orders = []
northlakes_orders = []
goldcoast_orders = []

all_orders = [carindale_orders, garden_orders, cherm_orders, northlakes_orders, goldcoast_orders]

def get_order_info():
    """
    adds order tuples to the appropriate lists. (see above to know what lists)
    required fields for each tuple are (full name, delivery address, postcode, client tel, product, delivery info)
    :return: Null
    """
    browser = mechanicalsoup.StatefulBrowser()
    browser.open("http://www.myweblogin.com/cgi-bin/newsbcms/admin.cgi")
    browser.select_form('form[action="https://www.myweblogin.com/cgi-bin/newsbcms/admin.cgi"]')
    browser["email"] = "rositaflowersmarketing@gmail.com"
    browser["pw"] = "subazuku"
    browser.submit_selected()
    sunday = "https://www.myweblogin.com/cgi-bin/newsbcms/shop/orders.cgi?siteid=mlg19q54gl&runsheet=1&from=2022-05-08&runsheet=1"
    saturday = "https://www.myweblogin.com/cgi-bin/newsbcms/shop/orders.cgi?siteid=mlg19q54gl&runsheet=1&from=2022-05-07&runsheet=1"
    browser.open(saturday)
    #browser.open("https://www.myweblogin.com/cgi-bin/newsbcms/shop/orders.cgi?runsheet=1&siteid=mlg19q54gl")
    page = browser.get_current_page()
    todays_links = page.find_all(href=re.compile("display"))
    proper_links = []
    for link in todays_links:
        print(link)
        link_string = str(link)
        print(link_string)
        link_string = str(link_string).split(' ')[2]
        link_string = link_string.split("?")[1]
        link_string = link_string[:19] + link_string[23:-1]
        link_string = "https://www.myweblogin.com/cgi-bin/newsbcms/shop/orders.cgi?" + link_string
        proper_links.append(link_string)
        browser.open(link_string)
        order_page = browser.get_current_page()
        # postcode = order_page.find(text=re.compile('Australia'))
        # if postcode is None:
        # postcode = order_page.find(text=re.compile('QLD'))
        # if postcode is None:
        # postcode = order_page.find(text=re.compile('Queensland'))
        postcodestr = order_page.find_all("td")
        postcode = postcodestr[5].find("p")
        # print(postcode)
        postlist = str(postcode).split('<br/>')
        print(postlist)
        z = postlist[-2]
        z = z.strip()
        postcode = z.split(' ')[-1]
        # state_info = postcode
        # postcode = str(postcode).strip()
        # postcode = postcode.split(" ")[2]
        date_str = order_page.find('h2')
        date_str = str(date_str).split('<h2>')[1]
        date_str = date_str.split('</h2>')[0]
        date = date_str.split(' ')[6]
        tr1 = order_page.find_all("tbody")[0]
        tr2 = tr1.find_all('p')[0]
        recip_name = str(tr2).split('<p>')[1]
        recip_name = recip_name.split('<br/>')[0]
        print(recip_name)
        recip_add1 = str(tr2).split('<br/>')[1].strip()
        recip_add2 = str(tr2).split('<br/>')[2].strip()
        suburb = str(tr2).split('<br/>')[3].strip()
        if suburb == "":
            suburb = str(tr2).split('<br/>')[4].strip()
        tel = str(tr2).split('<b>')[1]
        tel = tel.split('</b>')[0]
        tr3 = tr1.find_all('p')[2]
        order_id = str(tr3).split('</b>')[1]
        order_id = order_id.split('<br/>')[0]
        tr4 = order_page.find_all("p")[3]
        deliv_instructions = ""
        card_msg = ""
        product = None
        if str(tr4).startswith("<p><strong>Special Delivery Instructions"):
            deliv_instructions = str(tr4).split('<br/>')[1]
            deliv_instructions = deliv_instructions.split("</p>")[0]
        elif str(tr4).startswith("<p><strong>Card Text"):
            card_msg = str(tr4).split('<br/>')[1]
            card_msg = card_msg.split("</p>")[0]
        try:
            tr5 = str(order_page.find_all("p")[4])
        except IndexError:
            tr5 = ''
        if tr5.startswith("<p><strong>Card Text"):
            card_msg = tr5.split("<p><strong>Card Text</strong><br/>")[1]
            card_msg = card_msg.split("</p>")[0]
        try:
            tr6 = order_page.find_all('td')
            productloc = 17
            products = []
            images = []
            while True:
                product = str(tr6[productloc]).split("<p>")[1]
                product = product.replace("</p></td>", "")
                product = product.replace("<br/>", " ")
                product = product.replace("\n", "")
                products.append(product)
                imagefound = str(tr6[productloc - 1]).split("src=")[1]
                imagefound = imagefound.replace("/></td>'", '')
                imagefound = imagefound.replace("/></td>", '')
                images.append(imagefound)
                productloc += 5

                if str(tr6[productloc]).startswith("<td align"):
                    break
        except IndexError:
            products = []
        order_tuple = (
            recip_name, recip_add1 + " " + recip_add2 + " " + suburb, postcode,
            tel, products, deliv_instructions)
        if int(postcode) in chermside:
            cherm_orders.append(order_tuple)
        elif int(postcode) in northlakes:
            northlakes_orders.append(order_tuple)
        elif int(postcode) in carindale:
            carindale_orders.append(order_tuple)
        elif int(postcode) in garden:
            garden_orders.append(order_tuple)
        elif int(postcode) in goldcoast:
            goldcoast_orders.append(order_tuple)

def generate_csv():
    """
    writes the order infos to a csv
    :return: null
    """
    carindale_csv = r'C:\Users\Office\PycharmProjects\SpecialDayOrderZoner\csv_files\Carindale.csv'
    garden_csv = r'C:\Users\Office\PycharmProjects\SpecialDayOrderZoner\csv_files\Garden.csv'
    northlakes_csv = r'C:\Users\Office\PycharmProjects\SpecialDayOrderZoner\csv_files\Northlakes.csv'
    goldcoast_csv = r'C:\Users\Office\PycharmProjects\SpecialDayOrderZoner\csv_files\Goldcoast.csv'
    chermside_csv = r'C:\Users\Office\PycharmProjects\SpecialDayOrderZoner\csv_files\Chermside.csv'
    csvfiles = [carindale_csv, garden_csv, chermside_csv, northlakes_csv, goldcoast_csv]
    i = 0
    for file in csvfiles:
        with open(file, 'w', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(all_orders[i])
        i += 1

get_order_info()
generate_csv()
