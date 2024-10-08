#!/usr/bin/env python3
#  python pwb.py wd/wikinews
#
#
# ---

# ---

from wd_api import newdesc

# newdesc.mainfromQuarry2( topic , Quarry, translations)
# ---
# ---
from desc_dicts.descraptions import Qid_Descraptions

# ---
translations = {"Q11173": Qid_Descraptions['Q11173']}
# ---
for p31 in translations:
    en_desc = translations[p31]["en"]
    quarry = (
        '''SELECT DISTINCT ?item (GROUP_CONCAT(DISTINCT(?desc); separator=",") as ?langs)
    WHERE {
      SELECT ?item ?desc
    WHERE {
      ?item wdt:P31 wd:'''
        + p31
        + '''.
      ?item schema:description ?itemDes .
      ?item schema:description "'''
        + en_desc
        + '''"@en
      BIND(lang(?itemDes) AS ?desc)
          }
    limit 1000000
          }
    GROUP BY ?item
    limit 30000'''
    )
    # ---
    newdesc.Quarry_with_item_langs(p31, quarry, translations)
    # newdesc.mainfromQuarry2( p31, quarry, translations)
# ---
