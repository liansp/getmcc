#!/usr/bin/python

import sys
import requests
from bs4 import BeautifulSoup

def get_mcc(items):
    mcc = items[0].string
    mnc = items[1].string
    brand = items[2].string
    status = items[4].string
    if mcc is None or mnc is None or brand is None or status is None:
        return

    try:
        if (status == 'Operational' or status == 'Unknown'):
            if len(brand) > 16:
                print "======",
            print '{ "%s%s", "%s" },' % (mcc,mnc,brand)
    except:
        return

def parse_html(src):
    soup = BeautifulSoup(open(src))
    op_nets = soup.select('table[class="wikitable"]')
    for op_net in op_nets:
        trs = op_net.select('tr')
        for i in range(1,len(trs)):
            tds = trs[i].select('td')
            get_mcc(tds)

if __name__ == "__main__":
    parse_html(sys.argv[1])
