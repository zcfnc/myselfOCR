'''
将裁剪出来的数字二值化为黑底白字
'''

import os
import cv2
from PIL import Image

def NumGreyProcessing(imgDir):
    list = os.listdir(imgDir)  # 列出文件夹下所有的目录与文件
    for i in range(0, len(list)):
        path = os.path.join(imgDir, list[i])
        if os.path.isfile(path):
            img0 = cv2.imread(path, 0)
            # 读取图片
            blur = cv2.GaussianBlur(img0, (5, 5), 0)
            # (5,5)为高斯核的大小，0为标准差
            # 阀值一定要设为0
            ret3, th3 = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
            # 取得最佳阈值
            img = Image.open(path)
            Img = img.convert('L')
            # 模式L”为灰色图像，它的每个像素用8个bit表示，0表示黑，255表示白，其他数字表示不同的灰度.
            threshold = ret3
            # 根据Otsu's二值化方法取最佳阈值，大于这个值为黑色，小于这个值为白色
            table = []
            for j in range(256):
                if j > threshold:
                    table.append(0)
                else:
                    table.append(1)

            # 图片二值化
            photo = Img.point(table, '1')
            imgDst = imgDir+"/image2/"+list[i].split(".")[0]+".jpg"
            # 设置输出图片路径
            photo.save(imgDst)
            print(threshold)

if __name__ == '__main__':
    NumGreyProcessing("./image/")