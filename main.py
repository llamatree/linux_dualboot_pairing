import sys
import re

args = sys.argv

with open(args[1], "r", encoding="utf-16") as f:
    content = f.read()
    pattern = r'"(\w+)"=(.*)'
    result = re.findall(pattern, content)

    key_type_pattern = re.compile(r'^.+:')

    for key in result:
        match key[0]:
            case "LTK":
                ltk = key_type_pattern.sub("", key[1]).replace(",", "")
            case "ERand":
                erand = int("".join(list(reversed(key_type_pattern.sub("", key[1]).split(",")))), 16)
            case "EDIV":
                ediv = int(key_type_pattern.sub("", key[1]), 16)
            case _:
                pass
print(ltk)
print(erand)
print(ediv)
