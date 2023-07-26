# -*- coding: utf-8 -*-
import tkinter as tk
import threading
from time import sleep
from random import randint
from tkinter import messagebox
window = tk.Tk()
window.minsize(1000,625)
name_list = ['水泥 \n 1109 \n 信大',#1
             '食品 \n 1702 \n 南僑',#2
             '塑膠 \n 1312 \n 國喬',#3
             '紡織 \n 1413 \n 宏洲',#4
             '電機 \n 1503 \n 士電',#5
             '電器電纜 \n 1617 \n 榮星',#6
             '化學 \n 4764 \n 雙鍵',#7
             '生技醫療 \n 4108 \n 懷特',#8
             'etf \n 0050 \n 元大臺灣',#9
             '造紙 \n 1903 \n 士紙',#10
             '鋼鐵 \n 9958 \n 世紀鋼',#11
             '橡膠 \n 6582 \n 申豐',#12
             '汽車 \n 1568 \n 倉佑',#13
             '半導體 \n 2338 \n 光罩',#14
             '電腦周邊 \n 3494 \n 誠研',#15
             '光電 \n 6706 \n 惠特',#16
             '通信網路 \n 6285 \n 啟碁',#17
             '電子零組件 \n 1582 \n 信錦',#18
             '電子通路 \n 3010 \n 華立',#19
             '資訊服務 \n 6183 \n 關茂',#20
             '其他電子 \n 6409 \n 旭隼',#21
             '營建 \n 5533 \n 皇鼎',#22
             '航運 \n 2607 \n 榮運',#23
             '觀光 \n 2702 \n 華園',#24
             '金融 \n 2820 \n 華票',#25
             '貿易百貨 \n 2910 \n 統領',#26
             '油電燃氣 \n 2616 \n 山隆',#27
             '存託憑證 \n 9188 \n 精熙',#28
             '受益證券 \n 01010T \n 京城樂富',#29
             '其他 \n 6655 \n 科定'#30
             ]
btn_list = []
# 用 for loop 遍歷類股
for i in range(len(name_list)):
    button = tk.Button(window,text=name_list[i],font=('微軟正黑體', 12),bg='#0052cc',fg='#ffffff')
    btn_list.append(button)
    y, x = divmod(i, 6)
    button.place(x=100+x*100, y=100+y*100, width=80, height=80)
def round():
    # 點擊開始按鈕後，判斷按鈕顯示的開始文本，然後換成相反的暫停
    if btn_start['text'] == 'random choose':
        btn_start['text'] = 'stop'
    else:
        btn_start['text'] = 'random choose'
        return
    i = randint(0, (len(btn_list))-1)
    while True:
        for x in btn_list:
            x['bg'] = '#0052cc'
        btn_list[i]['bg'] = '#F11523'
        if btn_start['text'] == 'random choose':
            window.option_add('*Dialog.msg.font', 'Helvetica 16')
            tk.messagebox.showinfo(message='{}'.format(btn_list[i]['text']))
            '''
            沒有 break 語法就會一直抽籤，停也停不下來！
            '''
            break
        i = randint(0, (len(btn_list))-1)
        sleep(0.03)
def newtask():
    t = threading.Thread(target=round)
    t.start()
btn_start = tk.Button(window, text='random choose', command=newtask)
btn_start.place(width=200, height=80)
window.mainloop()