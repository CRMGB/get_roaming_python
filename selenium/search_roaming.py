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

    root_page = lxml.html.fromstring(driver.page_source)

    filter_header, cells = filter_table(root_page)

    brazil_allowances[filter_header[0]] = {'With allowance remaining': cells[0], 'Outside your allowance': cells[1] }

    print("brazil_allowances--> ",brazil_allowances)


def portugal_roaming(driver):

    driver.get("http://www.three.co.uk/support/roaming/portugal")

    root_page = lxml.html.fromstring(driver.page_source)

    filter_header, cells = filter_table(root_page)

    portugal_allowances[filter_header[0]] = {'With allowance remaining': cells[0], 'Outside your allowance': cells[1] }

    print("portugal_allowances--> ", portugal_allowances)


def chile_roaming(driver):

    driver.get("http://www.three.co.uk/support/roaming/chile")

    root_page = lxml.html.fromstring(driver.page_source)

    filter_header, cells = filter_table(root_page)

    chile_allowances[filter_header[0]] = {'With allowance remaining': cells[0], 'Outside your allowance': cells[1] }

    print("chile_allowances--> ", chile_allowances)


def s_africa_roaming(driver):

    driver.get(
        "http://www.three.co.uk/Support/Roaming_and_international/Mobile_roaming?content_aid=1214306363715"
    )

    root_page = lxml.html.fromstring(driver.page_source)

    filter_header, cells = filter_table(root_page)

    s_africa_allowances[filter_header[0]] = {'Cost': cells[1].split('\n',1)[0].lstrip() }

    print("s_africa_allowances--> ", s_africa_allowances)


def china_roaming(driver):

    driver.get(
        "http://www.three.co.uk/Support/Roaming_and_international/Mobile_roaming?content_aid=1214306373940"
    )

    root_page = lxml.html.fromstring(driver.page_source)

    filter_header, cells = filter_table(root_page)

    china_allowances[filter_header[0]] = {'Cost': cells[1].split('\n',1)[0].lstrip() }

    print("china_allowances--> ", china_allowances)

def madagascar_roaming(driver):

    driver.get(
        "http://www.three.co.uk/Support/Roaming_and_international/Mobile_roaming?content_aid=1214306362583"
    )

    root_page = lxml.html.fromstring(driver.page_source)

    filter_header, cells = filter_table(root_page)

    madagascar_allowances = {}

    madagascar_allowances[filter_header[0]] = {'Cost': cells[1].split('\n',1)[0].lstrip()}

    print("madagascar_allowances--> ", madagascar_allowances)


def filter_table(root_page):

    uk_search = 'UK'
    re_call_search = 'calls from any number'
    re_internet = 'Using internet and data'
    for row in root_page.xpath('.//table[@class="roaming-charges-table"]//tr'):
        headers = row.xpath('.//th/text()')
        cells = row.xpath('.//td/text()')
        #Search for the right allowances
        filter_header = [
            header for header in headers 
            if re.search(uk_search, header) 
            or re.search(re_call_search, header)
            or re.search(re_internet, header)
        ] 

        if len(filter_header) !=0:
            return filter_header, cells

if __name__ == '__main__':
    start_selenium()