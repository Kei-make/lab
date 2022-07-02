import glob

filename = glob.glob("C:/Users/kei83/Desktop/*.png")
newname = []
for i in filename:
    print(i)
    if "Roi" in i:
        newname.append(i)

print(newname)
