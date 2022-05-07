import os
import sys
from PIL import Image

def img2pdf(path):
    if os.path.isabs(path):
        img = Image.open(path)
    else:
        img = Image.open(os.path.join(os.getcwd(), path))
    img_pdf = img.convert("RGB")
    root, ext = os.path.splitext(path)
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
        print('Arguments are too short')