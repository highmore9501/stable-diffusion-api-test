import os
from PIL import Image


originalDir = "E:\SharedDirectory\PoleDriver\AI参考"


def changeImageSize(width, height):
    # 将输入的宽高，转换为最接近的 2 的幂次方
    widthScale = 1
    heightScale = 1
    while width > 2:
        width = width / 2
        widthScale = widthScale * 2
    while height > 2:
        height = height / 2
        heightScale = heightScale * 2
    minSize = widthScale if widthScale < heightScale else heightScale

    # 缩放宽高，使得最小的宽高为 512
    if minSize > 512:
        scale = int(minSize / 512)
        widthScale = int(widthScale / scale)
        heightScale = int(heightScale / scale)
        return widthScale, heightScale
    else:
        scale = int(512 / minSize)
        widthScale = int(widthScale * scale)
        heightScale = int(heightScale * scale)
        return widthScale, heightScale


# # 遍历原图文件夹里所有的图片
# for originalImag in os.listdir(originalDir):
#     # 如果不是png文件，跳过
#     if not originalImag.endswith(".png"):
#         continue

#     originalImagePath = originalDir + "/" + originalImag
#     # 读取原图，以及其大小
#     originalImage = Image.open(originalImagePath)
#     originalImageWidth = originalImage.size[0]
#     originalImageHeight = originalImage.size[1]
#     widthScale, heightScale = selectImageSize(
#         originalImageWidth, originalImageHeight)
#     print(f"原图片{originalImag},缩放后的大小是{widthScale}*{heightScale}")

width = 426
height = 240

widthScale, heightScale = changeImageSize(width, height)
print(f"原图片,缩放后的大小是{widthScale}*{heightScale}")
