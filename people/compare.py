import json

from pathlib import Path

Dir = Path(__file__).parent
# ---
from people.compare_files._occ import tota as tota2
from people.occupationsall import translations_all as tota1

# ---
# ---
# from people.compare_files._tra import tatonew as tota2
# from people.Nationalities import translationsNationalities as tota1
# ---
# ---
# dump tota1 to tota1.json with sorting and utf8
json.dump(tota1, open(f"{Dir}/compare_files/tota1old.json", "w", encoding="utf-8"), sort_keys=True, indent=2, ensure_ascii=False)

json.dump(tota2, open(f"{Dir}/compare_files/tota2new.json", "w", encoding="utf-8"), sort_keys=True, indent=2, ensure_ascii=False)

# keys in tota2 but not in tota1
new_keys = [x for x in tota2.keys() if x not in tota1.keys()]

# print the number of keys present in old translations file but not in the new one

print(f"{len(new_keys)} keys present in old translations file but not in the new one")

# print the keys present in old translations file but not in the new one

for key in new_keys:
    print(key)

print("compare values:")

for x, tab in tota1.items():
    if x in tota2:
        tab2 = tota2[x]
        if tab2 != tab:
            print(f"{x}: tab != tab2")
