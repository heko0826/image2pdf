from importlib.resources import path
import os
import sys
from PIL import Image
import glob

def img2pdf(root_path):
    path_list = []
    if os.path.isabs(root_path):
        dir_path = root_path
    else:
        dir_path = os.path.join(os.getcwd(), root_path)
    path_list.extend(glob.glob(os.path.join(dir_path, "*.png")))
    path_list.extend(glob.glob(os.path.join(dir_path, "*.jpg")))
    for path in path_list:
        img = Image.open(path)
        img_pdf = img.convert("RGB")
        root, _ = os.path.splitext(path)
        img_pdf.save(root+".pdf")



if __name__ == '__main__':
    args = sys.argv

    if 2 <= len(args):
        if 2 >= len(args):
            img2pdf(args[1])
            print("Executed.")
        else:
            print('Arguments are too long')
    else:
        for i in range(1, 5):
            sure = input("Are you sure to convert images in current directory? [yes/no]")
            if sure == "yes" or "Yes" or "YES":
                img2pdf(os.getcwd())
                break
            elif sure == "no" or "No" or "NO":
                print("It's OK. Not bad.")
                break
            else:
                print("I said yes or no")
            