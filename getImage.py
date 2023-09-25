import json
import requests
import io
import base64
from PIL import Image, PngImagePlugin
import datetime

url = "http://127.0.0.1:7860"

# 基本的prompt和steps设置
payload = {
    "prompt": "masterpiece, best quality, ultra high res, highres, best shadow, physics-based rendering, extremely delicate and beautiful,extremely detailed, amazing,shinning skin,look at viewer, a beautiful girl",
    "steps": 35,
    "sd_model_checkpoint": "chilloutmix_NiPrunedFp32Fix.safetensors [fc2511737a]"
}

# 一些额外的设置,override_settings是覆盖默认设置的,也就是说它是临时的,只会影响到这次请求
override_settings = {}
override_settings["CLIP_stop_at_last_layers"] = 2

override_payload = {
    "override_settings": override_settings
}
payload.update(override_payload)

# 发送请求
response = requests.post(url=f'{url}/sdapi/v1/txt2img', json=payload)
# 读取返回的json
r = response.json()

try:
    for i in r['images']:
        # 生成图片
        image = Image.open(io.BytesIO(base64.b64decode(i.split(",", 1)[0])))

        png_payload = {
            "image": "data:image/png;base64," + i
        }
        # 生成图片的信息
        response2 = requests.post(
            url=f'{url}/sdapi/v1/png-info', json=png_payload)
        # 加载图片信息
        pnginfo = PngImagePlugin.PngInfo()
        pnginfo.add_text("parameters", response2.json().get("info"))

        # 生成图片路径
        current = datetime.datetime.now().strftime("%Y-%m-%d")
        imageDir = "output"
        imagePath = imageDir + "/" + current + ".png"
        image.save(imagePath, pnginfo=pnginfo)
        print(f"image saved to {imagePath}")
except Exception as e:
    print(e)
