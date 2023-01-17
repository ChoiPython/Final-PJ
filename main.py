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
mainframe.geometry('800x400')
img = PhotoImage(file = '이미지/상점.png')
mainframe.iconphoto(mainframe, img)
mainframe.resizable(False, False)
mainframe.configure(bg = background)


# -------------폰트-------------
font1 = tkFont.Font(family = '한컴 고딕', size = 18)
font2 = tkFont.Font(family = '한컴 고딕', size = 14)
# print(list(tkFont.families()))    # 사용가능한 폰트 종류


# -------------검색-------------

# 라벨
SearchLb = Label(mainframe, text = '물품검색', padx = 20, pady = 10, bg = background, font = font1)
# SearchLb.place(x = 1, y = 1)
SearchLb.grid(row = 0, column = 1)


# 버튼
Searchimg = PhotoImage(file = '이미지/검색버튼1.png')
SearchBut = Button(mainframe, text = '검색', image = Searchimg, padx = 30, pady = 10, bd = 0, bg = background)
SearchBut.grid(row = 0, column = 3)



# 텍스트 박스
# borderwidth(bd) = 테두리 두께
SearchTB = Entry(mainframe, width = 40, bd = 2, font = font2)
SearchTB.grid(row = 0, column = 2)


# -------------아이템 목록-------------
itemtv = ttk.Treeview(mainframe, columns = ['one', 'two'], displaycolumns = ['one', 'two'])
itemtv.grid(row = 1, column = 2)



mainframe.mainloop()



