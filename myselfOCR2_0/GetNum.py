'''
字符切割
'''
from PIL import Image


def vertical(imgSrc, threashold, outDir,num):
    '''
    :param img:
    :param threashold: 阀值
    :param outDir: 保存位置
    :return:
    '''
    img = Image.open(imgSrc)
    w, h = img.size
    pixdata = img.load()

    x_array = []
    startX = 0
    endX = 0
    for x in range(w):
        b_count = 0
        for y in range(h):
            if pixdata[x, y] <= threashold:
                b_count += 1
        if b_count > 0:
            if startX == 0:
                startX = x
        elif b_count == 0:
            if startX != 0:
                endX = x
                x_array.append({'startX': startX, 'endX': endX})
                startX = 0
                endX = 0
    # for i, item in enumerate(x_array):
    #     box = (item['startX'], 0, item['endX'], h)
    #     if(i != 3 ):
    #         img.crop(box).save(outDir + str(num)+"_"+str(i) + ".png")
    #         print(i)
    m = 0
    for i, item in enumerate(x_array):
        if ( x_array[i]['endX']-x_array[i]['startX']>4):
            box = (item['startX'], 0, item['endX'], h)
            img.crop(box).save(outDir + str(num)+"_"+str(i-m) + ".png")
            print(i)
        else:
            m+=1
def go(imgSrc,imgDst,count):
    imgtemp = imgSrc
    for i in range(1,count+1):
        imgSrc = imgtemp + str(i) + "_1.jpg"
        print(imgSrc)
        vertical(imgSrc,150,imgDst,i)



if __name__ == '__main__':
    for i in range(1,11):
        imgSrc = "./test_result/"+str(i)+"_1.jpg"
        vertical(imgSrc,150,"./image/",i)