#!/usr/bin/env python3
#  python pwb.py wd/wikinews
#
#
"""


python pwb.py des/galaxy

"""
# ---

from wd_api import newdesc
from desc_dicts.descraptions import DescraptionsTable, Qid_Descraptions

# newdesc.mainfromQuarry2( topic , Quarry, translations)
# ---
translations = {"Q318": DescraptionsTable.get("galaxy") or Qid_Descraptions.get("Q318") or {}}
# ---
for q in translations:
    quarry = "SELECT ?item WHERE { ?item wdt:P31 wd:%s.} limit 50000" % q
    newdesc.mainfromQuarry2(q, quarry, translations)
# ---
