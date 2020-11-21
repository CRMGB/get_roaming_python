import lxml.html
import re

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def start_selenium():
    driver = webdriver.Firefox()

    brazil_roaming(driver)
    portugal_roaming(driver)
    chile_roaming(driver)
    china_roaming(driver)
    s_africa_roaming(driver)
    madagascar_roaming(driver)

    driver.close()

def brazil_roaming(driver):

    driver.get("http://www.three.co.uk/support/roaming/brazil")

    if not re.search("Mobile roaming in Brazil - Support - Three", driver.title):
        raise Exception("Unable to load google page!")
    
    root = lxml.html.fromstring(driver.page_source)

    table = './/table[@class="clearfix"]//tr'

    root = lxml.html.fromstring(driver.page_source, table)

    brazil_allowances = extract_table(root, table)

    print("brazil--> ", brazil_allowances)


def portugal_roaming(driver):

    driver.get("http://www.three.co.uk/support/roaming/portugal")

    if not re.search("Mobile roaming in Portugal - Support - Three", driver.title):
        raise Exception("Unable to load google page!")

    table = './/table[@class="clearfix"]//tr'

    root = lxml.html.fromstring(driver.page_source, table)

    portugal_allowances = extract_table(root, table)

    print("portugal--> ", portugal_allowances)


def chile_roaming(driver):

    driver.get("http://www.three.co.uk/support/roaming/chile")

    if not re.search("Mobile roaming in Chile - Support - Three", driver.title):
        raise Exception("Unable to load google page!")

    table = './/table[@class="clearfix"]//tr'

    root = lxml.html.fromstring(driver.page_source, table)

    chile_allowances = extract_table(root, table)

    print("chile--> ", chile_allowances)


def s_africa_roaming(driver):

    driver.get(
        "http://www.three.co.uk/Support/Roaming_and_international/Mobile_roaming?content_aid=1214306363715"
        )
    if not re.search("Mobile roaming - Roaming & international - Support - Three", driver.title):
        raise Exception("Unable to load google page!")

    table ='.//table[@class="roaming-charges-table"]//tr'

    root = lxml.html.fromstring(driver.page_source)

    s_africa_allowances = extract_table(root, table)

    print("s_africa--> ", s_africa_allowances)


def china_roaming(driver):

    driver.get(
        "http://www.three.co.uk/Support/Roaming_and_international/Mobile_roaming?content_aid=1214306373940"
        )

    if not re.search("Mobile roaming - Roaming & international - Support - Three", driver.title):
        raise Exception("Unable to load google page!")

    table ='.//table[@class="roaming-charges-table"]//tr'

    root = lxml.html.fromstring(driver.page_source)

    china_allowances = extract_table(root, table)

    print("china_allowances--> ", china_allowances)

def madagascar_roaming(driver):

    driver.get(
        "http://www.three.co.uk/Support/Roaming_and_international/Mobile_roaming?content_aid=1214306362583"
        )
    if not re.search("Mobile roaming - Roaming & international - Support - Three", driver.title):
        raise Exception("Unable to load google page!")

    table ='.//table[@class="roaming-charges-table"]//tr'

    root = lxml.html.fromstring(driver.page_source)

    madagascar_allowances = extract_table(root, table)

    print("madagascar_allowances--> ", madagascar_allowances)


def extract_table(root, table):
    table_allowances = {}
    uk_search = 'UK'
    re_call_search = 'calls from any number'
    re_internet = 'Using internet and data'

    for row in root.xpath(table):
        headers = row.xpath('.//th/text()')
        cells = row.xpath('.//td/text()')
        #Search for the right allowances
        filter_header = [
            header for header in headers 
            if re.search(uk_search, header) 
            or re.search(re_call_search, header)
            or re.search(re_internet, header)
            ] 

        if len(filter_header) !=0 and len(cells)>1:
            if re.search("roaming-charges-table", table):
                table_allowances[filter_header[0]] = {'Cost': cells[1].split('\n',1)[0].lstrip()}
            else:
                table_allowances[filter_header[0]] = {'With allowance remaining': cells[0], 'Outside your allowance': cells[1]}
    return table_allowances

if __name__ == '__main__':
    start_selenium()