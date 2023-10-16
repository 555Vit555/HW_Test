import pytest
import requests
from main_ya import create_folder
  
def test_create_folder():
    folder_name = "Test_folder"
    
    token = open("token").read()

    response = create_folder(folder_name, token)
    assert response.status_code == 201

    # Проверяем, что папка появилась в списке файлов
    url = "https://cloud-api.yandex.net/v1/disk/resources"
    headers = {
        "Authorization": f"OAuth {token}"
    }
    params = {
        "path": "/"
    }
    response = requests.get(url, headers=headers, params=params)
    assert response.status_code == 200
    response_json = response.json()
    assert "_embedded" in response_json
    assert "items" in response_json["_embedded"]
    