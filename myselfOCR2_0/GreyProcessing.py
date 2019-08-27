'''
灰度化处理
'''

import cv2
from PIL import Image
from scipy import misc

def GreyProcessing(imgSrc):
    #根据Otsu's方法取最佳阈值对图片进行二值化处理

    #获取到闭操作处理的图片
    img0 = cv2.imread(imgSrc, 0)
    #读取旋转过后的图片
    blur = cv2.GaussianBlur(img0, (5, 5), 0)
    # (5,5)为高斯核的大小，0为标准差
    # 阀值一定要设为0
    ret3, th3 = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    #取得最佳阈值
    img = Image.open(imgSrc)
    Img = img.convert('L')
    # 模式L”为灰色图像，它的每个像素用8个bit表示，0表示黑，255表示白，其他数字表示不同的灰度.
    # threshold = ret3-20
    threshold = ret3-20
    # 根据Otsu's二值化方法取最佳阈值，大于这个值为黑色，小于这个值为白色
    table = []
    for j in range(256):
        if j < threshold:
            table.append(0)
        else:
            table.append(1)

    # 图片二值化
    photo = Img.point(table, '1')
    imgDst = "./temp/3--Close_GreyProcessing_table.jpg"
    # 设置输出图片路径
    photo.save(imgDst)
    print(threshold)

    # 边界检测并生成中间图片
    img = cv2.imread(imgDst, 0)
    edges = cv2.Canny(img, 100, 200)
    edgeImgDst = "./temp/4--Close_GreyProcessing_edgeImage_table.jpg"
    misc.imsave(edgeImgDst, edges)
    return imgDst,edgeImgDst

if __name__ == '__main__':
    GreyProcessing("./temp/2--RectangularCutting_table.jpg")