import requests
import uuid
import json


def uploadMask(host, image_path) -> str:

    if image_path.startswith('http'):
        image_data = requests.get(image_path).content
        with open('../assets/temp/temp.jpg', 'wb') as f:
            f.write(image_data)
        file_uuid = uuid.uuid4()
        filename = f"{file_uuid}.png"
    else:
        image_data = open(image_path, 'rb').read()
        filename = image_path.split('/')[-1]

    data = {
        "overwrite": "true",
        "subfolder": "mask",
        "original_ref": json.dumps({
            "filename": filename,
            "type": "input",
            "subfolder": ""
        })
    }

    # post data to server
    url = f"http://{host}/upload/mask"
    response = requests.post(url, data=data, files={
                             "image": (filename, image_data),
                             })
    if response.status_code != 200:
        raise Exception(f"Upload mask failed.")
    name = response.json().get('name')

    return f'mask/{name}'


if __name__ == '__main__':
    host = "192.168.31.99:8188"
    # 注意上传的蒙版图片必须要有alpha图层才能正常保存
    image_path = '../output/00002_referenceOn the grass_chinese dress_0.png'
    # image_path = 'https://static.wikia.nocookie.net/all-worlds-alliance/images/d/da/DVa_Render.png/revision/latest?cb=20200415044652'
    upload_image = uploadMask(host, image_path)
    print(upload_image)
