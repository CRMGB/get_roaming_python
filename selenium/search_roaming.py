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

    driver.close()

def brazil_roaming(driver):

    driver.get("http://www.three.co.uk/support/roaming/brazil")

    root = lxml.html.fromstring(driver.page_source)

    uk_search = 'UK'
    re_call_search = 'calls from any number'
    re_internet = 'Using internet and data'
    count = 0
    brazil_allowances = {}
    for row in root.xpath('.//table[@class="clearfix"]//tr'):
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
            brazil_allowances[filter_header[0]] = {'With allowance remaining': cells[0], 'Outside your allowance': cells[1]  }

    print("brazil_allowances--> ",brazil_allowances)


def portugal_roaming(driver):

    driver.get("http://www.three.co.uk/support/roaming/portugal")

    root = lxml.html.fromstring(driver.page_source)

    uk_search = 'UK'
    re_call_search = 'calls from any number'
    re_internet = 'Using internet and data'
    count = 0
    portugal_allowances = {}
    for row in root.xpath('.//table[@class="clearfix"]//tr'):
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
            portugal_allowances[filter_header[0]] = {'With allowance remaining': cells[0], 'Outside your allowance': cells[1]  }

    print("portugal_allowances--> ", portugal_allowances)



def chile_roaming(driver):

    driver.get("http://www.three.co.uk/support/roaming/chile")

    root = lxml.html.fromstring(driver.page_source)

    uk_search = 'UK'
    re_call_search = 'calls from any number'
    re_internet = 'Using internet and data'
    count = 0
    chile_allowances = {}
    for row in root.xpath('.//table[@class="clearfix"]//tr'):
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
            chile_allowances[filter_header[0]] = {'With allowance remaining': cells[0], 'Outside your allowance': cells[1]  }

    print("chile_allowances--> ", chile_allowances)

#China
def china_roaming(driver):

    driver.get("http://www.three.co.uk/Support/Roaming_and_international/Mobile_roaming?content_aid=1214306373940")

    root = lxml.html.fromstring(driver.page_source)

    uk_search = 'UK'
    re_call_search = 'calls from any number'
    re_internet = 'Using internet and data'
    count = 0
    china_allowances = {}
    for row in root.xpath('.//table[@class="roaming-charges-table"]//tr'):
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
            china_allowances[filter_header[0]] = {'Cost': cells[0] }

    print("china_allowances--> ", chile_allowances)

if __name__ == '__main__':
    start_selenium()