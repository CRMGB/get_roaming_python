import lxml.html
import re
import json

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

tables = {
    './/table[@class="clearfix"]//tr': {
        "Brazil" : "http://www.three.co.uk/support/roaming/brazil",
        "Portugal": "http://www.three.co.uk/support/roaming/portugal",
        "Chile" : "http://www.three.co.uk/support/roaming/chile",
        "Iceland" : "http://www.three.co.uk/support/roaming/iceland",
    }, 
    './/table[@class="roaming-charges-table"]//tr' : {
        "South Africa": "http://www.three.co.uk/Support/Roaming_and_international/Mobile_roaming?content_aid=1214306363715",
        "China" : "http://www.three.co.uk/Support/Roaming_and_international/Mobile_roaming?content_aid=1214306373940",
        "Madagascar" : "http://www.three.co.uk/Support/Roaming_and_international/Mobile_roaming?content_aid=1214306362583",
    }
}

def initialize_selenium():
    results_dict = {}
    driver = webdriver.Firefox()
    for table, targets in tables.items():
        results = loop_countries_tables(driver, table, targets, results_dict)
    with open("output/sample.json", "w") as outfile: 
        json.dump(results, outfile) 
    driver.close()

def loop_countries_tables(driver, table, targets, results_dict):
    for country, website in targets.items():
        driver.get(website)
        root = lxml.html.fromstring(driver.page_source, table)
        allowances = extract_table(root, table)
        allowances['website'] = website
        results_dict[country] = allowances
    return results_dict


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
    initialize_selenium()