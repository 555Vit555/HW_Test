
import requests

def create_folder(folder_name, token):
    url = "https://cloud-api.yandex.net/v1/disk/resources"
    headers = {
        "Authorization": f"OAuth {token}"
    }
    params = {
        "path": f"/{folder_name}"
    }
    response = requests.put(url, headers=headers, params=params)
    return response