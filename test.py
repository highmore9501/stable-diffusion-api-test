import os
from PIL import Image


originalDir = "E:\SharedDirectory\PoleDriver\AI参考"


def changeImageSize(width, height):
    minSize = min(width, height)

    # 缩放宽高，使得最小的宽高为 512
    if minSize > 512:
        scale = minSize / 512
        widthScale = int(width / scale)
        heightScale = int(height / scale)
    else:
        scale = 512 / minSize
        widthScale = int(width * scale)
        heightScale = int(height * scale)

    # 将两个值都除以128，然后取整
    widthScale = int(widthScale/128) * 128
    heightScale = int(heightScale/128)*128

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


width = 312
height = 486

widthScale, heightScale = changeImageSize(width, height)
print(f"原图片,缩放后的大小是{widthScale}*{heightScale}")
