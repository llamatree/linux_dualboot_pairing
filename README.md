# linux_dualboot_pairing

詳しくは以下のwikiをご覧ください。
(https://wiki.archlinux.jp/index.php/Bluetooth#%E3%83%87%E3%83%A5%E3%82%A2%E3%83%AB%E3%83%96%E3%83%BC%E3%83%88%E3%83%9A%E3%82%A2%E3%83%AA%E3%83%B3%E3%82%B0)   
このプログラムでは上記ページの **2.1.4 Bluetooth 5.1 キーの準備** の　"他のデバイス" の仕様に基づいています。   
## 使用方法
このページの項目```2.1.2.1```を参考にlinux環境でもペアリングしたいデバイスのレジストリをregファイルに書き出してください。   
書き出したファイルを```main.py```と同じ場所に配置します。
```python main.py <regファイル>```を実行するとLTK, ERand, EDIVの3つの値が出力されます。   
wikiを参照して、Linux環境で設定してください。
