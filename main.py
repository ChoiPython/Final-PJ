'''
2023-01-17 // gui 구성
'''
from tkinter import *
import tkinter.ttk as ttk
import tkinter.font as tkFont


# -------------배경-------------
background = 'ghost white'

# -------------메인 프레임-------------
# overrideredirect(True) 제목표시줄 사라지게함
mainframe = Tk()
mainframe.title('메인화면')
mainframe.geometry('800x400+400+300')
img = PhotoImage(file = '이미지/상점.png')
mainframe.iconphoto(mainframe, img)
mainframe.resizable(False, False)
mainframe.configure(bg = background)


# -------------폰트-------------
font1 = tkFont.Font(family = '한컴 고딕', size = 18)    # 라벨
font2 = tkFont.Font(family = '한컴 고딕', size = 14)    # 텍스트
# print(list(tkFont.families()))    # 사용가능한 폰트 종류


# -------------검색-------------

# 라벨
SearchLb = Label(mainframe, text = '물품검색', bg = background, font = font1)
SearchLb.place(x = 10, y = 10)

# 텍스트 박스
# borderwidth(bd) = 테두리 두께
SearchTB = Entry(mainframe, width = 40, bd = 2, font = font2)
SearchTB.place(x = 120, y = 15)


# 버튼
Searchimg = PhotoImage(file = '이미지/검색버튼1.png')
SearchBut = Button(mainframe, text = '검색', image = Searchimg, padx = 30, pady = 10, bd = 0, bg = background)
SearchBut.place(x = 565, y = 15)


# -------------아이템 목록-------------
# 컬럼 설정
def setcol(treeview, colname, text, width, anchor) :
    treeview.column(colname, width = width, anchor = anchor, minwidth = 50, stretch = False)
    treeview.heading(colname, text = text, anchor = anchor)

# 트리뷰 생성
itemtv = ttk.Treeview(mainframe, selectmode='browse',columns = ['name', 'price', 'quantity'], displaycolumns = ['name', 'price', 'quantity'])
itemtv.place(x = 20, y = 60)

# treeview(변수), 컬럼명, 설정이름, 가로크기, 문자정렬
setcol(itemtv, '#0', '번호', 50, 'center')
setcol(itemtv, 'name', '아이템명', 250, 'center')
setcol(itemtv, 'price', '가격', 100, 'center')
# setcol(itemtv, 'quantity',)

# 스크롤
# yscrlbar = Scrollbar(itemtv)
# yscrlbar.pack(side = RIGHT, fill= Y)
# # yscrlbar.place(x = 750, y = 60)
# itemtv.configure(yscrollcommand = yscrlbar.set)

# 값 삽입 / iid = 표의 고유값
itemtv.insert('', 'end', text = 1, values = ['test', 1200])

mainframe.mainloop()



