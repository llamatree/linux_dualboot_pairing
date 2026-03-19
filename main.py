import sys
import re

# コマンドライン引数でレジストリファイルのパスを取得
args = sys.argv

# 第1引数のレジストリファイルパスを開く. レジストリファイルはUTF-16
with open(args[1], "r", encoding="utf-16") as f:
    content = f.read()
    pattern = r'"(\w+)"=(.*)'   # "KEY"=VALUEの部分だけを取り出す
    result = re.findall(pattern, content)

    # キーからdword:などの形式部分の正規表現
    key_type_pattern = re.compile(r'^.+:')

    # 各レジストリの名前ごとにLinux用の形式への変換を行う
    for key in result:
        match key[0]:
            case "LTK":
                # "dword:" を取り除きコンマを削除する
                ltk = key_type_pattern.sub("", key[1]).replace(",", "")
            case "ERand":
                # "dword:"を取り除く
                # コンマで分割する
                # リストに変換して逆順にする
                # リストを結合する
                # 10進数に変換する
                erand = int("".join(list(reversed(key_type_pattern.sub("", key[1]).split(",")))), 16)
            case "EDIV":
                # "hex(b)"を取り除く。10進数に変換する。
                ediv = int(key_type_pattern.sub("", key[1]), 16)
            case _:
                pass
# 結果を表示
print(ltk)
print(erand)
print(ediv)
