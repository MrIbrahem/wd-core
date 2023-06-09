#!/usr/bin/python

"""

إضافة تسميات مواضيع طبية

"""
#
# (C) Ibrahem Qasim, 2022
#
#


import re
import time
import pywikibot
# ---
from API import printe
import sys
# ---
import urllib
import urllib.request
import urllib.parse

# ---
from API import himoBOT2
# ---
from wd_API import himoAPI_test as himoAPI
# ---


def dec(xx):
    xx = xx.replace(" ", "_")
    fao = xx
    try:
        fao = urllib.parse.quote(xx)
    except:
        printe.output('<<lightred>> except when urllib.parse.quote(%s)' % xx)
    return fao
# ---


def fixrow(row):
    en, ar = False, False
    # printe.output( "===============================" )
    row = re.sub("\n+", "", row)
    row = re.sub("\t+", "", row)
    row = re.sub("\s+", " ", row)
    row = re.sub("</strong><strong>", " ", row)
    row = re.sub("<strong>", "", row)
    row = re.sub("</strong>", "", row)
    row = re.sub(
        '<td class="views-field views-field-field-hadaf-value views-align-center" >', "<tdss>", row)
    # printe.output( row )
    # ---
    if row.find('<td class="views-field views-field-title views-align-center" >') != -1:
        row = row.split(
            '<td class="views-field views-field-title views-align-center" >')[1]
        row = row.split('</p>')[0]
        # if row.find('<tdss>') != -1:
        row = re.sub('</td><tdss><p>', "<ssss>", row)
        # printe.output( row )
    # ---
    if row.find("<ssss>") != -1:
        en = row.split('<ssss>')[0].strip()
        ar = row.split('<ssss>')[1].strip()
        # printe.output( 'en:"%s",ar:"%s"' % (en,ar) )
        if en != "" and ar != "":
            return en, ar
    # ---
    return en, ar


# ---
Labels = {}
SaveR = {1: False}
# ---


def fixo(stro):
    stro = stro.strip()
    stro = stro.split("(")[0]
    stro = stro.split("[")[0]
    stro = stro.split(":")[0]
    return stro
# ---


def Fix_List(List):
    New_List = []
    # ---
    for y in List:
        yy = y
        yy = re.sub(";", "،", yy)
        yy = re.sub("؛", "،", yy)
        yy = re.sub("\‚", "،", yy)
        yy = re.sub(",", "،", yy)
        yy = re.sub("-->", "", yy)
        New_List.append(yy)
    # ---
    New_List2 = []
    # if ar.find(" (الجمع:") != -1 :
    # ---
    FFA = "(الجمع|ج|جمعها|)(\=|\:)(.*)"
    mattes = [
        "^(.*)\(" + FFA + "\)$",
        "^(.*)\[" + FFA + "\]$",
        "^(.*)\[" + FFA + "\]$"
    ]
    # ---
    comas = ["،", ";", "؛"]
    # comas = ["، ", "; " , "؛ "]
    # ---
    for ar in New_List:
        Conn = True
        # ---
        for coma in comas:
            if ar.find(coma) != -1:
                Conn = False
                printe.output('ca "%s" , .find("%s") != -1' % (ar, coma))
                # New_List.remove(ar)
                ars = ar.split(coma)
                # ---
                printe.output('ars:"%s"' % "|".join(ars))
                for aa in ars:
                    if not aa.strip() in New_List2:
                        New_List2.append(fixo(aa))
                        # New_List.append( aa.strip() )
        # ---
        # elif re.match( mat , ar) or re.match( mat1 , ar) or re.match( mat2 , ar):
        if Conn:
            Dodo = True
            for mate in mattes:
                if re.match(mate, ar.strip()) and Dodo:
                    # New_List.remove(ar)
                    Dodo = False
                    Conn = False
                    # ---
                    ar1 = re.sub(mate, '\g<4>', ar)
                    ar2 = re.sub(mate, '\g<1>', ar)
                    printe.output('ar2:"%s",ar1:"%s" ' % (ar2, ar1))
                    # ---
                    if not ar1.strip() in New_List2:
                        New_List2.append(fixo(ar1))
                    # ---
                    if not ar2.strip() in New_List2:
                        New_List2.append(fixo(ar2))
                    # ---
        # ---
        if Conn:
            if not ar.strip() in New_List2:
                New_List2.append(fixo(ar))
        # ---
    New_List = [fixo(x) for x in New_List2]
    printe.output("New_List: " + "|".join(New_List))
    return New_List
# ---


def fixrow2(row):
    en, ar = False, False
    row = re.sub(" <", "<", row)
    row = re.sub("> ", ">", row)
    row = re.sub("\n+", "", row)
    row = re.sub("\t+", "", row)
    row = re.sub("\s+", " ", row)
    row = re.sub('\<tr bgcolor\=\"\#\w+\"\>', "", row)
    # printe.output( "===============================" )
    rowss = row.split("</td>")
    # printe.output( rowss )
    # printe.output( "===============================" )
    # ---
    # en = re.sub( '\<td class\=\"tden\"\>(.*)\<\/td\>' , '\g<1>', row )
    # ar = re.sub( '\<td class\=\"tdar\"\>(.*)\<\/td\>' , '\g<1>', row )
    # ---
    for x in rowss:
        # printe.output( x )
        if x.startswith('<td class="tdar">'):
            ar = x.split('<td class="tdar">')[1]
        elif x.startswith('<td class="tden">'):
            en = x.split('<td class="tden">')[1]
    # ---
    return en, ar
# ---


def Get_item_table(enlab):
    Item_tab = []
    so = enlab
    so = so.replace(" ", "+")
    url = "http://tbeeb.net/med/search.php?q={}".format(so)
    printe.output(url)
    # ---
    if url == "http://tbeeb.net/med/search.php?q=":
        return Item_tab
    # ---
    html = himoBOT2.getURL(url=url)
    if html.find('<table class="table">') == -1:
        return Item_tab
    # ---
    html = html.split('<table class="table">')[1]
    html = html.split("</table>")[0]
    html = re.sub("\n+", "", html)
    html = re.sub("\t+", "", html)
    html = re.sub("\s+", " ", html)
    html = re.sub("> <", "><", html)
    # printe.output( html )
    # ---
    if enlab in Labels:
        for eee in Labels[enlab]:
            if not eee in Item_tab:
                Item_tab.append(eee)
    # ---
    rows = html.split("</tr>")
    for row in rows:
        en, ar = fixrow2(row)
        if en and ar:
            if not en in Labels:
                Labels[en] = []
            Labels[en].append(ar)
            # ---
            if en == enlab:
                # ---
                if not ar in Item_tab:
                    Item_tab.append(ar)
    # ---
    Item_tab = Fix_List(Item_tab)
    # ---
    return Item_tab
# ---


def Get_item_table2(enlab):
    Item_tab = []
    # url = "http://www.alqamoos.org/?search_fulltext={}&field_magal=Medical".format( dec(enlab) )
    url = "http://www.alqamoos.org/?search_fulltext={}&field_magal=All".format(
        dec(enlab))
    printe.output(url)
    # ---
    # if url == "http://www.alqamoos.org/?search_fulltext=&field_magal=Medical" :
    if url == "http://www.alqamoos.org/?search_fulltext=&field_magal=All":
        return Item_tab
    # ---
    html = himoBOT2.getURL(url=url)
    if html.find("No results matched your search") != -1:
        return Item_tab
    # ---
    html = html.split("<tbody>")[1]
    html = html.split("</tbody>")[0]
    html = re.sub("\n+", "", html)
    html = re.sub("\t+", "", html)
    html = re.sub("\s+", " ", html)
    html = re.sub("> <", "><", html)
    # printe.output( html )
    # ---
    if enlab in Labels:
        for eee in Labels[enlab]:
            if not eee in Item_tab:
                Item_tab.append(eee)
    # ---
    rows = html.split("</tr>")
    for row in rows:
        en, ar = fixrow(row)
        if en and ar:
            if not en in Labels:
                Labels[en] = []
            Labels[en].append(ar)
            # ---
            if en == enlab:
                # ---
                if not ar in Item_tab:
                    Item_tab.append(ar)
    # ---
    Item_tab = Fix_List(Item_tab)
    # ---
    return Item_tab


# ---
Looogs = {}
# ---


def looog():
    wikidatasite = pywikibot.Site('wikidata', 'wikidata')
    EngPage = pywikibot.Page(wikidatasite, "user:Mr._Ibrahem/medstat")
    main_text = EngPage.text
    log2 = {}
    # ---
    for x in Looogs:
        if Looogs[x] != []:
            log2[x] = Looogs[x]
    # ---
    text2 = ""
    # ---
    for x in log2:
        text2 = text2 + \
            "\n|-\n| {{Q|%s}} || {{Label | %s | en }} || %s\n" % (
                x, x, ",".join(log2[x]))
    # ---
    if text2 != "":
        text2 = '''\n=={{subst:date}}==\n{| class="wikitable sortable"\n|-\n! item\n! en \n! ar\n|-''' + text2
        text2 = text2 + "|-\n|}"
        text3 = main_text + text2
    # ---
        himoAPI.page_put(text3, "update.", "user:Mr._Ibrahem/medstat")
    # ---


def WORK(item, table):
    # printe.output( item )
    printe.output(table)
    # ---
    if not item in Looogs:
        Looogs[item] = []
    # ---
    # printe.output( '<<lightgreen>> item:"%s" ' % item )
    # ---
    arlab = table["ar"]
    enlab = table["en"]
    enlab = re.sub("_", " ", enlab.lower())
    # ---
    Item_tab = Get_item_table2(enlab)
    if Item_tab == []:
        Item_tab = Get_item_table(enlab)
    # ---
    Item_tab2 = Item_tab
    # printe.output( ",".join(Item_tab) )
    for alia in Item_tab:
        if alia in table["alias"]:
            Item_tab.remove(alia)
            printe.output('alia : "%s" in alias' % alia)
        # ---
        elif alia == table["ar"]:
            Item_tab.remove(alia)
            printe.output('alia : "%s" == ar label' % alia)
    # ---
    if Item_tab != Item_tab2:
        printe.output(",".join(Item_tab))
    # ---
    NewALLi_to_add = []
    for ali in Item_tab:
        if arlab == "":
            arlab = ali
            if SaveR[1]:
                himoAPI.Labels_API(item, ali, "ar", False)
                Looogs[item].append(ali)
            else:
                sa = pywikibot.input(
                    '<<lightyellow>>add ali : "%s" as label to item :%s? ' % (ali, item))
                if sa == 'y' or sa == 'a' or sa == '':
                    himoAPI.Labels_API(item, ali, "ar", False)
                    Looogs[item].append(ali)
                else:
                    print(' himoAPI: wrong answer')
        else:
            NewALLi_to_add.append(ali)
    # ---
    if arlab in NewALLi_to_add:
        NewALLi_to_add.remove(arlab)
    # ---
    for uu in NewALLi_to_add:
        if uu in table["alias"]:
            NewALLi_to_add.remove(uu)
            printe.output('uu : "%s" in table["alias"]' % uu)
        elif SaveR[1] and uu.find("(") != -1:
            NewALLi_to_add.remove(uu)
            printe.output('uu : "%s" in table["alias"]' % uu)
    # ---
    if NewALLi_to_add != []:
        printe.output("|".join(NewALLi_to_add))
        # printe.output( 'NewALLi_to_add: "%s"'  % str("|".join(NewALLi_to_add)) )
        if SaveR[1]:
            himoAPI.Alias_API(item, NewALLi_to_add, "ar", False)
            Looogs[item].append(",".join(NewALLi_to_add))
        else:
            sa = pywikibot.input(
                '<<lightyellow>>himoAPI: Add Alias ([y]es, [N]o, [a]ll): for item %s' % item)
            if sa == 'y' or sa == 'a' or sa == '':
                himoAPI.Alias_API(item, NewALLi_to_add, "ar", False)
                Looogs[item].append(",".join(NewALLi_to_add))
            else:
                print(' himoAPI: wrong answer')

    # ---
Limit = {1: "500"}
# ---


def main():
    # python3 pwb.py wd/med
    # python3 pwb.py wd/med short
    # python3 pwb.py wd/med  ta:horror
    # python3 pwb.py wd/med qs:Q12136
    # python3 pwb.py wd/med qs:Q39546
    # python3 pwb.py wd/med qs:Q24017414
    # python3 pwb.py wd/med qs:Q27043950
    # ---
    # sat = "{?item wdt:%s  wd:%s. }" % (pp , qq)
    # sat = "{?item wdt:%s  wd:%s. }" % (pp , qq)
    # pp , qq = "P105" , "Q35409"
    pp, qq = "P31", "Q27043950"
    sat = "?item wdt:%s  wd:%s. "
    for arg in sys.argv:
        arg, sep, value = arg.partition(':')
        # ---#Depth[1]
        if arg == "p":
            pp = value
        # ---#
        if arg == "qs":
            qq = value
            pp = "P31/wdt:P279*"
        # ---#
        if arg == "q":
            qq = value
        # ---#
        if arg == 'always':
            SaveR[1] = True
            printe.output('<<lightred>> SaveR = True.')
        # ---#limit[1]
        if arg == '-limit' or arg == 'limit':
            Limit[1] = value
            printe.output('<<lightred>> Limit = %s.' % value)
        # ---#
    sat = sat % (pp, qq)
    # ?item wdt:P1343 ?P1343.
    # {?P1343 wdt:P629 wd:Q200306.} UNION {?item wdt:P1343 wd:Q19558994. }
    # sat = "{?item wdt:P31/wdt:P279* wd:Q27043950. }"#Q4936952.}
    # SERVICE wikibase:label { bd:serviceParam wikibase:language "en" . }
    Quaa = ''' SELECT ?item ?en ?ar ?alias WHERE { '''
    Quaa = Quaa + sat + '''
    ?item rdfs:label ?en. FILTER(LANG(?en) = "en").
    FILTER NOT EXISTS { ?item rdfs:label ?ar. FILTER(LANG(?ar) = "ar"). }
    FILTER NOT EXISTS  { ?item skos:altLabel ?alias FILTER (LANG (?alias) = "ar") }
    }
    LIMIT '''

    Quaa = Quaa + Limit[1]
    printe.output(Quaa)
    sparql = himoBOT2.sparql_generator_url(Quaa)
    # ---
    Table = {}
    for item in sparql:
        q = item['item'].split("/entity/")[1]
        if not q in Table:
            Table[q] = {}
        for tab in item:
            if not tab in Table[q]:
                Table[q][tab] = []
            # if item[tab] != "" :
            Table[q][tab].append(item[tab])
    # ---
    Tab_l = {}
    for it_em in Table:
        Tab_l[it_em] = {'ar': Table[it_em]["ar"][0],
                        'alias': Table[it_em]["alias"], 'en': Table[it_em]["en"][0]}
    # ---
    num = 0
    for item in Tab_l:
        num += 1
        # if num < 2:
        printe.output('<<lightgreen>> %d/%d item:"%s" ' %
                      (num, len(Tab_l.keys()), item))
        # item['item'] = item['item'].split("/entity/")[1]
        WORK(item, Tab_l[item])
    # ---
    looog()


    # ---
if __name__ == "__main__":
    main()
    # printe.output(Get_item_table("ships")  )
    # t = fixrow2('<tr bgcolor="#FCFCFC"><td class="tden"> ship | ships | </td><td class="tdar"> فلك سفينة, سفينة, قارب, زورق بخاري, نوتية المركب</td>')
    # printe.output( t )
    # Fix_List(["الفروة","الشواة (فروة الرأس)","الشواة","الفروة، الشواة، فروة الرأس","فروة"])
    # Fix_List(['صدر', 'صدر [:صدور]', 'كلاب [ج=كب]'])
    # Fix_List(["الترقوة","الناحرة","الترقوة (الجمع: التراقي)","عظم الترقوة"])
    # Fix_List(['كلاب [ج=كب]'])
    # Fix_List(['صدر', 'صدر [ج:صدور]', 'الصدر'])
    # Fix_List(['الطبلة (=غشاء الطبل)'])
    # Fix_List(["برتقالية" , "برتقال [نبات]" , "برتقالي" , "برتقالي - برتقال" , "برتقال (نبات)" , "برتقالية (مادة ملونة)"])
    # Fix_List(["لؤلوة (ج: لآلئ)", "لآلىء"])
    # Fix_List(["توت الأرض؛فراولة ;فريز"])
    # Fix_List(['الطبلة (ج=غشاء الطبل)'])
    # WORK("Q4115189" , {'en': 'orbitofrontal cortex','ar': 'يمو', "alias" :[] })
    # WORK("Q4115189" , {'en': 'orbitofrontal cortex','ar': 'يمو', "alias" :[] })
# ---
