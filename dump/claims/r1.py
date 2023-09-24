"""
from dump.claims.read_dump import read_file
python3 wd_core/dump/claims/read_dump.py test

https://dumps.wikimedia.org/wikidatawiki/entities/latest-all.json.bz2

"""
import os
import sys
import bz2
import mmap
import json
import time
from datetime import datetime
from pathlib import Path
# ---
# ---
# split after /dump
core_dir = str(Path(__file__)).replace('\\', '/').split("/dump/", maxsplit=1)[0]
print(f'core_dir:{core_dir}')
sys.path.append(core_dir)
print(f'sys.path.append:core_dir: {core_dir}')
# ---
from dump.memory import print_memory
# ---
Dump_Dir = "/data/project/himo/dumps"
filename = "/mnt/nfs/dumps-clouddumps1002.wikimedia.org/other/wikibase/wikidatawiki/latest-all.json.bz2"
# ---
print(f'Dump_Dir:{Dump_Dir}')
# ---
test_limit = {1: 15000}


def log_dump(tab):
    jsonname = f"{Dump_Dir}/claims.json"
    if 'test' in sys.argv:
        jsonname = f"{Dump_Dir}/claims_test.json"
    # jsonname = "dumps/claims_c.json"
    with open(jsonname, "w", encoding='utf-8') as outfile:
        json.dump(tab, outfile)
    print("log_dump done")


def get_file_info(file_path):
    # Get the time of last modification
    last_modified_time = os.path.getmtime(file_path)

    # Convert the timestamp to a readable format
    readable_time = datetime.fromtimestamp(last_modified_time).strftime('%Y-%m-%d')

    return readable_time


def read_file():
    print(f"read file: {filename}")

    if not os.path.isfile(filename):
        print(f"file {filename} not found")
        return {}

    t1 = time.time()
    file_date = get_file_info(filename)
    print(f'file date: {file_date}')

    print(f"file {filename} found, read it:")
    c = 0
    done = 0
    len_of_all_properties = 0
    items_0_claims = 0
    items_1_claims = 0
    items_no_P31 = 0
    All_items = 0
    all_claims_2020 = 0
    # ---
    Main_Table = {}
    langs_Table = {}
    # ---
    print('read done..')
    # ---
    def r_line(line):
        json1 = json.loads(line)
        # ---
        tats = ['labels', 'descriptions', 'aliases']
        for x in tats:
            for code in json1.get(x, {}):
                if not code in langs_Table:
                    langs_Table[code] = {'labels': 0, 'descriptions': 0, 'aliases': 0}
                langs_Table[code][x] += 1
        # ---
        claims = json1.get("claims", {})
        # ---
        if len(claims) == 0:
            items_0_claims += 1
            del json1
            return
        # ---
        if len(claims) == 1:
            items_1_claims += 1
        # ---
        if "P31" not in claims:
            items_no_P31 += 1
        # ---
        for p in claims.keys():
            Type = claims[p][0].get("mainsnak", {}).get("datatype", '')
            if Type == "wikibase-entityid":
                if p not in Main_Table:
                    Main_Table[p] = {
                        "props": {},
                        "lenth_of_usage": 0,
                        "lenth_of_claims_for_property": 0,
                    }
                Main_Table[p]["lenth_of_usage"] += 1
                all_claims_2020 += len(claims[p])
                for claim in claims[p]:
                    Main_Table[p]["lenth_of_claims_for_property"] += 1
                    datavalue = claim.get("mainsnak", {}).get("datavalue", {})
                    ttype = datavalue.get("type")
                    if ttype == "wikibase-entityid":
                        idd = datavalue.get("value", {}).get("id")
                        if idd:
                            if not idd in Main_Table[p]["props"]:
                                Main_Table[p]["props"][idd] = 0
                            Main_Table[p]["props"][idd] += 1
                Main_Table[p]["len_of_qids"] = len(Main_Table[p]["props"])
        # ---
        del json1
        del claims
    # ---
    with bz2.open(filename, "r", encoding='utf-8') as file:
        file_map = mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ)

        start_position = 0
        while start_position < len(file_map):
            end_position = file_map.find(b'\n', start_position)
            if end_position == -1:
                break
            line = file_map[start_position:end_position]
            start_position = end_position + 1

            # ---
            print(f'type of line: {type(line)}')
            # ---
            try:
                line = line.decode("utf-8").strip("\n").strip(",")
            except:
                print("error")
                continue
            # ---
            done += 1
            # ---
            if 'pp' in sys.argv:
                print(line)
            # ---
            if line.startswith("{") and line.endswith("}"):
                All_items += 1
                c += 1
                if 'test' in sys.argv:
                    if c % 1000 == 0:
                        print(f'c:{c}')
                        print(f'done:{done}')

                    if c > test_limit[1]:
                        print('c>test_limit[1]')
                        break

                r_line(line)
            # ---
            if c % 1000 == 0 or c == 100:
                print(c, time.time()-t1)
                t1 = time.time()
                # print memory usage
                print_memory()
            # ---
        file_map.close()
        # ---
        tab = {
            "done": done,
            "file_date": file_date,
            "len_of_all_properties": len_of_all_properties,
            "items_0_claims": items_0_claims,
            "items_1_claims": items_1_claims,
            "items_no_P31": items_no_P31,
            "All_items": All_items,
            "all_claims_2020": all_claims_2020,
            "Main_Table": Main_Table,
            "langs": langs_Table,
        }
        log_dump(tab)


if __name__ == "__main__":
    read_file()