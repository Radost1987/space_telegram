import datetime
import os

import requests
import urllib.parse
from dotenv import load_dotenv
from pathlib import Path
from urllib.parse import urlsplit




def get_extension(url):
    decoded_url = urllib.parse.unquote(url)
    path_url = urlsplit(decoded_url)
    extension = os.path.splitext(path_url.path)[1]
    return extension


def fetch_nasa_apod():
    load_dotenv()
    url = 'https://api.nasa.gov/planetary/apod'
    nasa_api_key = os.getenv('NASA_API_KEY')
    payload = {
        'api_key': nasa_api_key,
        'count': 10
    }
    response = requests.get(url, params=payload)
    response.raise_for_status()
    pictures_info = response.json()
    for i, picture in enumerate(pictures_info, start=1):
        extension = get_extension(picture['url'])
        download_images(picture['url'], f'apod{i}{extension}')
def fetch_nasa_epic():
    url = 'https://api.nasa.gov/EPIC/api/natural/images'
    payload = {
        'api_key': nasa_api_key
    }
    response = requests.get(url, params=payload)
    response.raise_for_status()
    for i, image in enumerate(response.json(), start=1):
        created_date = datetime.datetime.fromisoformat(image['date']) \
            .strftime('%Y/%m/%d')
        download_images(
            f"https://epic.gsfc.nasa.gov/archive/natural/{created_date}/png/{image['image']}.png",
            main.nasa_images_folder,
            f'epic{i}.png'
        )


if __name__ == "__main__":
    fetch_nasa_apod()
    fetch_nasa_epic()
