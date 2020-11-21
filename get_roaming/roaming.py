
import lxml.html
import re

import os
import sys
scriptpath = "../selenium/search_roaming.py"
sys.path.append(os.path.abspath(scriptpath))
import MyModule

from selenium import rearch_roaming

def brazil_roaming():

    MyModule.start_selenium()
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

if __name__ == '__main__':
    brazil_roaming()