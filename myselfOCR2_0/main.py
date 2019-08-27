'''

目录结构：

./image：存放切割出的单个数字
./test_result:存放切割出来的单个等式
main5：主方法


操作步骤：
1.霍夫变换  -->     HoughTransform  -->  1--HoughTransform.jpg
2.边界提取闭操作及及透视转换   --> RectangularCutting.walk   -->  2--RectangularCutting_table.jpg
3.灰度化并获取图片的边界  -->  GreyProcessing  -->  4--Close_GreyProcessing.jpg/5--Close_GreyProcessing_edgeImage_table.jpg
4.分割单元格并获取到格数  -->  ImageIncise.Incise  -->  6--ImageCutting.jpg
5.单元切割分出单个等式   -->  NumCutting.Exe  -->  ./test_result
6.单个数字分割  -->  GetNum.go  -->  ./image

'''
from myselfOCR import NumCutting,ImageIncise,GetNum,RectangularCutting
from myselfOCR.HoughTransform import HoughTransform
from myselfOCR.GreyProcessing import GreyProcessing


def start(img):

    imgSrc = img
# 霍夫变换
    imgSrc = HoughTransform(imgSrc)
# 边界提取闭操作及及透视转换
    imgSrc = RectangularCutting.walk(imgSrc)
# 灰度处理
    imgSrc, edgeImgDst= GreyProcessing(imgSrc)
# Canny边缘检测，分割单元格并获取到格数
    imgDst = "./temp/5--ImageCutting.jpg"
    count = ImageIncise.Incise(imgSrc,imgDst)
# 单元切割分出单个等式:百分比切割
    NumCutting.Exe(count)
# 单个数字和符号的分割
    GetNum.go("./test_result/","./image/",count)


if __name__ == '__main__':
    start("tmp.JPEG")
#输入查询图片
