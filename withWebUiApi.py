import webuiapi
import datetime
from PIL import Image, PngImagePlugin
import os
from pathlib import Path
import json

# 初始化api
api = webuiapi.WebUIApi()

url = "127.0.0.1"
# create API client with custom host, port
api = webuiapi.WebUIApi(host=url, port=7860)

# create API client with custom host, port and https
# api = webuiapi.WebUIApi(host='webui.example.com', port=443, use_https=True)

# create API client with default sampler, steps.
# api = webuiapi.WebUIApi(sampler='Euler a', steps=20)

# optionally set username, password when --api-auth=username:password is set on webui.
# username, password are not protected and can be derived easily if the communication channel is not encrypted.
# you can also pass username, password to the WebUIApi constructor.
# api.set_auth('username', 'password')

# api都支持异步，需要添加use_async=True
# api还支持脚本，但有点啰嗦，所以没有记录在这里，可以自己去看：https://github.com/mix1009/sdwebuiapi#scripts-support

# 文生图


def text2img(api):
    result = api.txt2img(prompt="cute squirrel",
                         negative_prompt="ugly, out of frame",
                         seed=-1,
                         styles=["anime"],
                         cfg_scale=7,
                         sampler_index='DDIM',
                         steps=30,
                         enable_hr=True,
                         hr_scale=1,
                         hr_upscaler=webuiapi.HiResUpscaler.Latent,
                         hr_second_pass_steps=20,
                         hr_resize_x=512,
                         hr_resize_y=768,
                         denoising_strength=0.4,
                         )
    return result

# 保存图片


def saveImages(result, imageDir):
    for image in result.images:
        pnginfo = PngImagePlugin.PngInfo()
        pnginfo.add_text("parameters", str(result.parameters))
        current = datetime.datetime.now().strftime("%Y-%m-%d")
        imagePath = imageDir + "/" + current + ".png"
        image.save(imagePath, pnginfo=pnginfo)

# 图生图


def img2img(api, imagePath):
    image = Image.open(imagePath)
    result = api.img2img(images=[image], prompt="cute cat",
                         seed=-1, cfg_scale=6.5, denoising_strength=0.6)
    return result

# inpaint


def imgInpaint(api, imagePath, maskPath):
    image = Image.open(imagePath)
    mask = Image.open(maskPath)
    result = api.img2img(images=[image],
                         mask_image=mask,
                         inpainting_fill=1,
                         prompt="cute cat",
                         seed=104,
                         cfg_scale=5.0,
                         denoising_strength=0.7)
    return result


def scaleImage(api, imagePath, scale):
    image = Image.open(imagePath)
    result = api.extra_single_image(image=image,
                                    upscaler_1=webuiapi.Upscaler.ESRGAN_4x,
                                    upscaling_resize=scale)
    return result


def scaleImages(api, imageDir, scale):
    images = []
    # 遍历 imageDir,读取其中的png文件，放入images列表
    for file in os.listdir(imageDir):
        if file.endswith(".png"):
            image = Image.open(imageDir + "/" + file)
            images.append(image)

    result = api.extra_batch_images(images=images,
                                    upscaler_1=webuiapi.Upscaler.ESRGAN_4x,
                                    upscaling_resize=scale)
    return result


if __name__ == "__main__":
    # mki = webuiapi.ModelKeywordInterface(api)
    # result = mki.get_keywords()
    # print(result)
    # api.controlnet_version()
    # options = api.get_loras()
    # 将options转换为json格式,保存到/apiOptions/get_loras.json
    # with open("apiOptions/get_loras.json", "w") as f:
    #     json.dump(options, f)
    options = api.get_sd_vae()
    print(options)
