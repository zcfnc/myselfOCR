from skimage import io,data,color
from skimage import img_as_float
import os
import numpy as np
from PIL import Image

def clearEdge(img,width):
    img[0:width-1,:]=1
    img[1-width:-1,:]=1
    img[:,0:width-1]=1
    img[:,1-width:-1]=1
    return img


def focusImg(imgPath,imgCount):
    img=io.imread(imgPath)
    img2=Image.open(imgPath)
    img=color.rgb2gray(img)
    img=img_as_float(img)
    img=clearEdge(img,3)

    # 求各列的和
    col_sum=img.sum(axis=0)
    # 求各行的和
    row_sum=img.sum(axis=1)

    idx_col_sum=np.argwhere(col_sum<col_sum.max())
    if len(idx_col_sum)==0:
        os.remove(imgPath)
        return
    col_start,col_end=idx_col_sum[0,0]-1,idx_col_sum[-1,0]+10

    idx_row_sum=np.argwhere(row_sum<row_sum.max())
    if len(idx_row_sum)==0:
        os.remove(imgPath)
        return
    row_start,row_end=idx_row_sum[0,0]-1,idx_row_sum[-1,0]+10

    print("x1:", col_start)
    print("y1:", row_start)
    print("x2:", col_end)
    print("y2:", row_end)

    w = col_end - col_start
    h = row_end - row_start

    region = img2.crop((col_start+w/100, row_start+h/10, col_end-w/10, row_end-h/10))

    # region = img2.crop((col_start+w/55, row_start+h/7, col_end-w/10, row_end-h/5))
    # row 行号  col 列号
    region.save("./test_result/"+str(imgCount)+"_1.jpg")
    print("./test_result/"+str(imgCount)+"_1.jpg")

def Exe(count):
    for i in range(1,count+1):
        imgSrc="./test_result/"+str(i)+".jpg"
        print(imgSrc)
        focusImg(imgSrc,i)

if __name__ == '__main__':
    Exe(10)