import openpyxl
import tkinter as tk

def createfile():
    list1 = ["W1","W2","W3","W4","W5","W6","W7","H1","H2","H3","H4","H5","H6","H7"]

    wb = openpyxl.Workbook(list1[0])

    for i in range(len(list1)):
        wb.create_sheet(title=list1[i])

    name = "./desktop/" + textbox.get() + ".xlsx"
    wb.save(name)
    
    

root = tk.Tk()
root.title("エクセルファイルの作成")
root.geometry("300x150")  # ラベル
getfile = tk.Label(text='作成するファイル名を入力')
getfile.place(x=30, y=30)
textbox = tk.Entry(width=40)
textbox.place(x=30, y=50)
button = tk.Button(text="実行", command=createfile)
button.place(x=120, y=70)
root.mainloop()




