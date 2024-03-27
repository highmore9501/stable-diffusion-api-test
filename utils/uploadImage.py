import requests
import uuid


def uploadImage(host, image_path) -> str:
    if image_path.startswith('http'):
        image_data = requests.get(image_path).content
        with open('../assets/temp/temp.jpg', 'wb') as f:
            f.write(image_data)
        file_uuid = uuid.uuid4()
        filename = f"{file_uuid}.jpg"
    else:
        image_data = open(image_path, 'rb').read()
        filename = image_path.split('/')[-1]

    data = {
        "overwrite": "true",
        "subfolder": "",
    }

    url = f"http://{host}/upload/image"
    response = requests.post(url, data=data, files={
                             "image": (filename, image_data)})

    if response.status_code != 200:
        raise Exception(f"Upload image failed.")

    return response.json().get('name')


if __name__ == '__main__':
    host = "192.168.31.99:8188"
    image_path = 'C:/Users/BigHippo78/Pictures/Donald_Trump_mug_shot.jpg'
    # image_path = 'https://static.wikia.nocookie.net/all-worlds-alliance/images/d/da/DVa_Render.png/revision/latest?cb=20200415044652'
    upload_image = uploadImage(host, image_path)
    print(upload_image)
