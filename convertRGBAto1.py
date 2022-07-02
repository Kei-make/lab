from PIL import Image
import glob
# Pillow でカラー画像を読み込む

filename = glob.glob("C: / Users/kei83/Pictures/2022-06-28/*.png")

for i in filename:
    pil_image_color = Image.open(i).convert("P")
    pil_image_color.save("005.png")


# for i in filename:
 #   pil_image_color = Image.open(i)
 #   print("■■ カラー画像 ■■")
 #   print("モード:\t\t", pil_image_color.mode)
 #   print("バンド:\t\t", pil_image_color.getbands())
 #   print("チャンネル数:\t", len(pil_image_color.getbands()))
