import glob
import os
import tkinter
import tkinter.filedialog
import tkinter.messagebox
import cv2

# フォルダ選択ダイアログの表示
root = tkinter.Tk()
root.withdraw()
iDir = os.path.abspath(os.path.dirname(__file__))
dir = tkinter.filedialog.askdirectory(initialdir=iDir)
add = dir + '/'
# 作業pathの変更
os.chdir(add)

new_path = "2tika"  # フォルダ名
if not os.path.exists(new_path):  # ディレクトリがなかったら
    os.mkdir(new_path)

files = glob.glob('*.png')
# 読み込むファイルのリストを表示
for i in range(len(files)):
    img = cv2.imread(files[i], 0)

    # 閾値の設定
    threshold = 100
    # 二値化(閾値100を超えた画素を255にする。)
    ret, img_thresh = cv2.threshold(img, threshold, 255, cv2.THRESH_BINARY)
    newname = "{0:02d}".format(i+2) + '.png'
    cv2.imwrite('./' + new_path + "/" + newname, img_thresh)
