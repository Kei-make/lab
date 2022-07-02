import pandas as pd
import glob
import os

csvfile = glob.glob("C:/Users/kei83/Desktop/hansin/*.csv")

col = ["c00", "C01", "c02"]

df_csv = [pd.read_csv(file, encoding="shift-jis", names=col)
          for file in csvfile]


for i, filename in enumerate(csvfile):
    a = 0
    number = [0, 0, 0, 0, 0, 0, 0, 0]
    for k in range(len(df_csv[i])-8):
        a += 0.01
        number.append(a)
    df_csv[i].insert(0, 'time', number)


with pd.ExcelWriter('C:/Users/kei83/Desktop/data.xlsx') as writer:
    for i, name in enumerate(df_csv):
        path, ext = os.path.splitext(os.path.basename(csvfile[i]))
        name.to_excel(writer, sheet_name=path, index=False)
