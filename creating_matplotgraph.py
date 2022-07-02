import matplotlib.pyplot as plt
import pandas as pd
import os
import tkinter
import tkinter.filedialog
import tkinter.messagebox

# フォルダ選択ダイアログの表示
root = tkinter.Tk()
root.withdraw()
iDir = os.path.abspath(os.path.dirname(__file__))
dir = tkinter.filedialog.askdirectory(initialdir=iDir)
add = dir + '/'
# 作業pathの変更
os.chdir(add)

df = pd.read_csv('totalcsv.csv')


def multiLegend(df, x, y_list):
    plt.rcParams['font.family'] = "Meiryo"
    c_list = ["k", "r", "b", "g", "c", "m", "y"]
    l_list = ["-", "--", "-.", "."]
    fig, ax = plt.subplots(figsize=(5, 5))
    plt.subplots_adjust(left=0.17, bottom=0.17, top=0.95, right=0.95)
    # x,yの範囲指定
    for i in range(len(y_list)):
        y = y_list[i]
        ax.plot(df[x], df[y], linestyle=l_list[i], color=c_list[i], label=y)
    yLabel = '加速度(m/s2)'
    ax.set_ylabel(yLabel)
    ax.set_xlabel(x)
    plt.xlim(2, 3)
    plt.ylim(-6, 6)
    plt.xlabel("計測時間（SEC)", fontsize=18)
    plt.ylabel("加速度(m/s2)", fontsize=18)
    plt.legend(loc='lower left', borderaxespad=0.5,
               fontsize=12)
    plt.tick_params(labelsize=14)
    plt.show()
    return


multiLegend(df, '計測時間(SEC)', ['振幅２', '振幅４', '振幅６'])
