#!/usr/bin/env python3

from wd_api import newdesc

# ---
from desc_dicts.descraptions import DescraptionsTable

# ---
translations = {'Wikimedia module': DescraptionsTable.get('Wikimedia module', {})}
# ---
LIST = ["Q15145755", "Q18711811"]  # Module test cases  # map data module
# ---
topic = 'Wikimedia module'
# ---
for ll in LIST:
    quarry = 'SELECT ?item  WHERE {  ?item wdt:P31 wd:%s.}' % ll
    newdesc.mainfromQuarry2(topic, quarry, translations)
# ---
