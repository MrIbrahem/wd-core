"""
python3 core8/pwb.py dump/claims/do_text
"""
#
# (C) Ibrahem Qasim, 2023
#
#
import sys
import time
import codecs
import json
# ---
time_start = time.time()
print(f"time_start:{str(time_start)}")
# ---
from dump.labels.do_text import main_labels  # main_labels(tabb)
# ---
Dump_Dir = "/data/project/himo/dumps"
# ---
print(f'Dump_Dir:{Dump_Dir}')
# ---
sections_done = {1: 0, 'max': 100}
sections_false = {1: 0}


def make_section(P, table, max_n=51):
    """
    Creates a section for a given property in a table.

    Args:
        P (str): The property value.
        table (dict): The table data.

    Returns:
        str: The section text.

    """
    # ---
    # if sections_done[1] >= sections_done['max']:    return ""
    # ---
    Len = table['lenth_of_usage']
    # ---
    texts = "== {{P|%s}} ==" % P
    # ---
    print(f"make_section for property:{P}")
    texts += f"\n* Total items use these property:{Len:,}"
    # ---
    lnnn = table.get("len_prop_claims")
    if lnnn:
        texts += f"\n* Total number of claims with these property:{lnnn:,}"
    # ---
    len_of_qids = table.get("len_of_qids")
    if len_of_qids:
        texts += f"\n* Number of unique qids:{len_of_qids:,}"
    # ---
    texts += "\n"
    print(texts)
    if table["qids"] == {}:
        print(f'{P} table["qids"] == empty.')
        return ""
    # ---
    if len(table["qids"]) == 1 and table["qids"].get("others"):
        print(f'{P} table["qids"] == empty.')
        return ""
    # ---
    Chart = '{| class="floatright sortable"\n|-\n|\n'
    Chart += "{{Graph:Chart|width=140|height=140|xAxisTitle=value|yAxisTitle=Number\n"
    Chart += "|type=pie|showValues1=offset:8,angle:45\n|x=%s\n|y1=%s\n|legend=value\n}}\n|-\n|}"
    # ---
    tables = """{| class="wikitable sortable plainrowheaders"\n|-\n! class="sortable" | #\n! class="sortable" | value\n! class="sortable" | Numbers\n|-\n"""
    # ---
    lists = {k: v for k, v in sorted(table["qids"].items(), key=lambda item: item[1], reverse=True)}
    # ---
    xline = ""
    yline = ""
    # ---
    num = 0
    other = 0
    # ---
    for x, ye in lists.items():
        # ---
        if x == "others":
            other += ye
            continue
        # ---
        num += 1
        if num < max_n:
            Q = x
            if x.startswith("Q"):
                Q = "{{Q|%s}}" % x
            # ---
            tables += f"\n! {num} \n| {Q} \n| {ye:,} \n|-"
            # ---
            xline += f",{x}"
            yline += f",{ye:,}"
        else:
            other += ye
    # ---
    num += 1
    # ---
    Chart = Chart % (xline, yline)
    # ---
    tables += f"\n! {num} \n! others \n! {other:,} \n|-"
    # ---
    tables += "\n|}\n{{clear}}\n"
    # ---
    # texts += Chart.replace("=,", "=") + "\n\n"
    # ---
    texts += tables
    # ---
    sections_done[1] += 1
    # ---
    return texts


def make_numbers_section(p31list):
    xline = ""
    yline = ""
    # ---
    rows = []
    # ---
    property_other = 0
    # ---
    n = 0
    # ---
    for Len, P in p31list:
        n += 1
        if n < 27:
            xline += f",{P}"
            yline += f",{Len}"
        # ---
        if len(rows) < 101:
            Len = f"{Len:,}"
            P = "{{P|%s}}" % P
            lune = f"| {n} || {P} || {Len} "
            rows.append(lune)
        else:
            property_other += int(Len)
    # ---
    Chart2 = "{| class='floatright sortable' \n|-\n|"
    Chart2 += "{{Graph:Chart|width=900|height=100|xAxisTitle=property|yAxisTitle=usage|type=rect\n"
    Chart2 += f"|x={xline}\n|y1={yline}"
    Chart2 += "\n}}"
    Chart2 += "\n|-\n|}"
    # ---
    Chart2 = Chart2.replace("=,", "=")
    # ---
    rows.append(f"! {n} \n! others \n! {property_other:,}")
    rows = "\n|-\n".join(rows)
    table = (
        "\n{| "
        + f'class="wikitable sortable"\n|-\n! #\n! property\n! usage\n|-\n{rows}\n'
        + "|}"
    )
    # ---
    text = "== Numbers ==\n" f"\n{Chart2}\n{table}"
    # ---
    return text


def make_text(tab, ty=''):
    p31list = [[y["lenth_of_usage"], x] for x, y in tab["properties"].items() if y["lenth_of_usage"] != 0]
    p31list.sort(reverse=True)
    # ---
    final = time.time()
    delta = int(final - time_start)
    # ---
    if not tab.get('file_date'):
        tab['file_date'] = 'latest'
    # ---
    text = (
        "<onlyinclude>;dump date {file_date}</onlyinclude>.\n"
        "* Total items: {All_items:,}\n"
        "* Items without P31: {items_no_P31:,} \n"
        "* Items without claims: {items_0_claims:,}\n"
        "* Items with 1 claim only: {items_1_claims:,}\n"
        "* Total number of claims: {all_claims_2020:,}\n"
        "* Number of properties of the report: {len_of_all_properties:,}\n"
    ).format_map(tab)
    # ---
    text += f"<!-- bots work done in {delta} secounds --> \n--~~~~~\n"
    chart = make_numbers_section(p31list)
    # ---
    text_p31 = ''
    # ---
    if tab["properties"].get('P31'):
        text_p31 = text + make_section('P31', tab["properties"]['P31'], max_n=501)
        # ---
    # ---
    if 'onlyp31' in sys.argv or ty == "onlyp31":
        return text, text_p31
    # ---
    sections = ""
    for _, P in p31list:
        if sections_done[1] >= sections_done['max']:
            break
        # ---
        sections += make_section(P, tab["properties"][P], max_n=51)
    # ---
    text += f"{chart}\n{sections}"
    # ---
    # text = text.replace("0 (0000)", "0")
    # text = text.replace("0 (0)", "0")
    # ---
    return text, text_p31


if __name__ == "__main__":
    faf = 'claims'
    faf = 'claims_fixed'
    # ---
    if 'claims_fixed' in sys.argv:
        filename = "claims_fixed"
    # ---
    filename = f"{Dump_Dir}/{faf}.json"
    # ---
    if 'test' in sys.argv:
        filename = f"{Dump_Dir}/{faf}_test.json"
    # ---
    data = json.load(open(filename))

    tab = {
        "done": 0,
        "len_of_all_properties": 0,
        "items_0_claims": 0,
        "items_1_claims": 0,
        "items_no_P31": 0,
        "All_items": 0,
        "all_claims_2020": 0,
        "properties": {},
        "langs": {},
    }
    # ---
    for x, g in tab.items():
        if not x in data:
            data[x] = g
    # ---
    main_labels(data)
    # ---
    text, text_p31 = make_text(data, ty='')
    # ---
    claims_new = f'{Dump_Dir}/texts/claims_new.txt'
    claims_p31 = f'{Dump_Dir}/texts/claims_p31.txt'
    # ---
    if 'test' in sys.argv:
        claims_new = f'{Dump_Dir}/texts/claims_new_test.txt'
        claims_p31 = f'{Dump_Dir}/texts/claims_p31_test.txt'
    # ---
    with codecs.open(claims_new, 'w', encoding='utf-8') as outfile:
        outfile.write(text)
    # ----
    with codecs.open(claims_p31, 'w', encoding='utf-8') as outfile:
        outfile.write(text_p31)
    # ----
    print(text_p31)
    # ---
    print("log_dump done")
