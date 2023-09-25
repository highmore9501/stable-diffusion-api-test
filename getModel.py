import json
import requests
import io
import base64
from PIL import Image, PngImagePlugin
import datetime

url = "http://127.0.0.1:7860"

# 发送请求
response = requests.get(url=f'{url}/sdapi/v1/sd-models')
# 读取返回的json
r = response.json()

for model in r:
    model_name = model["model_name"]
    if model["hash"]:
        hash = model["hash"]
        print(model_name + " [" + hash + "]")
    else:
        print(model_name)

'''
alienLandscapes_alienLandscapes [e1df4e2e4d]
AnythingV5Ink_v32Ink [a1535d0a42]
cheeseDaddys_41
chilloutmix_Ni
chilloutmix_NiPrunedFp32Fix [fc2511737a]
disneyPixarCartoon_v10 [732d0dd2cf]
forgesagaLandscape_v10
kawaiiRealisticAsian_v01
kawaiiRealisticAsian_v03
locsChinaLandscapes_locsChinaLandscapes
majicmixRealistic_v6
pornmasterPro_fullV3New
pornmasterPro_fullV4-inpainting
sd-v1-4-full-ema
sd-v1-4
sd-v1-5-inpainting
v1-5-pruned-emaonly
v1-5-pruned
'''
