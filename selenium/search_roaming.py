import lxml.html
import re
import enum

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

websites_target_table_1 = {
    "Brazil" : "http://www.three.co.uk/support/roaming/brazil",
    "Portugal": "http://www.three.co.uk/support/roaming/portugal",
    "Chile" : "http://www.three.co.uk/support/roaming/chile",
    "Iceland" : "http://www.three.co.uk/support/roaming/iceland",
}

websites_target_table_2 = {
    "South Africa": "http://www.three.co.uk/Support/Roaming_and_international/Mobile_roaming?content_aid=1214306363715",
    "China" : "http://www.three.co.uk/Support/Roaming_and_international/Mobile_roaming?content_aid=1214306373940",
    "Madagascar" : "http://www.three.co.uk/Support/Roaming_and_international/Mobile_roaming?content_aid=1214306362583",
}

def countries_table_1():
    driver = webdriver.Firefox()
    table = './/table[@class="clearfix"]//tr'
    for country, website in websites_target_table_1.items():
        print(website, "\n")
        driver.get(website)
        root = lxml.html.fromstring(driver.page_source, table)
        allowances = extract_table(root, table)
        print(country, "--> ", allowances)
    return driver

def countries_table_2(driver):
    table = './/table[@class="roaming-charges-table"]//tr'
    for country, website in websites_target_table_2.items():
        print(website, "\n")
        driver.get(website)
        root = lxml.html.fromstring(driver.page_source, table)
        allowances = extract_table(root, table)
        print(country, "--> ", allowances)
    driver.close()

def extract_table(root, table):
    table_allowances = {}

    for row in root.xpath(table):
        headers = row.xpath('.//th/text()')
        cells = row.xpath('.//td/text()')
        #Search for the right allowances
        filter_header = [
            header for header in headers 
            if re.search('UK', header) 
            or re.search('calls from any number', header)
            or re.search('Using internet and data', header)
        ] 

        if len(filter_header) !=0 and len(cells)>1:
            if re.search("roaming-charges-table", table):
                table_allowances[filter_header[0]] = {'Cost': cells[1].split('\n',1)[0].lstrip()}
            else:
                table_allowances[filter_header[0]] = {'With allowance remaining': cells[0], 'Outside your allowance': cells[1]}
    return table_allowances

if __name__ == '__main__':
    driver = countries_table_1()
    countries_table_2(driver)