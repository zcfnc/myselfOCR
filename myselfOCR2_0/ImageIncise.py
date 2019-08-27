'''
图片切割找子单元的边界
'''

import numpy as np
import cv2
from PIL import Image
import os
import shutil

def Incise(imgSrc, imgDst):
    '''
    :param imgSrc:闭操作及灰度处理后的图像（图4）
    :param imgDst:描边表格的图像
    :return:count:裁剪出来的单元个数
    '''
    if os.path.exists("./image"):
        shutil.rmtree("./image")
        os.mkdir("./image")
    else:
        os.mkdir("./image")
    if os.path.exists("./test_result"):
        shutil.rmtree("./test_result")
        os.mkdir("./test_result")
    else:
        os.mkdir("./test_result")
#如果输入目录已经存在的话，清空目录

    img = cv2.imread(imgSrc)
    img2 = Image.open(imgSrc)
    # 灰度图
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 阈值
    _, threshold = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY_INV)
    # 膨胀
    kernel = np.ones((3, 3), np.uint8)
    dilated = cv2.dilate(threshold, kernel, iterations=1)
    # 轮廓检测
    _, contours, hierarchy = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # 找到表格最外层轮廓
    tree = hierarchy[0]
    max_size = 0
    outer_contour_index = None
    for i, contour in enumerate(contours):
        size = cv2.contourArea(contour)
        if size > max_size:
            max_size = size
            outer_contour_index = i
    contour = contours[outer_contour_index]
    # 估算最小的单元格大小
    x, y, w, h = cv2.boundingRect(contour)
    cell_size = w * h * 0.0015
    # 遍历所有最外层轮廓的子轮廓，过滤掉面积小于cell_size的，然后全部用矩形标注起来
    contour_index = tree[outer_contour_index][2]
    count = 0

    while 1:

        contour = contours[contour_index]

        if cv2.contourArea(contour) > cell_size:
            x, y, w, h = cv2.boundingRect(contour)
            count += 1
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
            # 第一个参数：img是原图;第二个参数：（x，y）是矩阵的左上点坐标;第三个参数：（x + w，y + h）是矩阵的右下点坐标
            # 第四个参数：（0, 255, 0）是画线对应的rgb颜色;第五个参数：2是所画的线的宽度
            region = img2.crop((x+3, y+3, x + w - 3, y + h - 3))
            region.save("./test_result/%d.jpg" %count)
            print(count)
        contour_index = tree[contour_index][0]
        if contour_index < 0:
            cv2.imwrite(imgDst, img)
            break
    return count
if __name__=="__main__":

    Incise("./temp/3--Close_GreyProcessing_table.jpg","temp.jpg")
    # Incise("3--Close_table.jpg","temp.jpg")