import os
import time
from os import listdir
from pathlib import Path

import telegram
from dotenv import load_dotenv

import fetch_nasa
import fetch_spacex



def create_images_path(images_folder):
    images_path = Path(f'{Path.cwd()}/{images_folder}')
    images_path.mkdir(parents=True, exist_ok=True)
    return images_path


def load_files_to_telegram(images_folder, path):
    load_dotenv()
    bot = telegram.Bot(token=os.getenv('TELEGRAM_TOKEN'))
    files = listdir(images_folder)
    for file in files:
        with open(f'{path}/{file}', 'rb') as image:
            bot.send_document(
                chat_id=os.getenv('TELEGRAM_CHAT_ID'),
                document=image
            )
            time.sleep(86400)


def main():
    while True:
        load_dotenv()
        telegram_chat_id = os.getenv('TELEGRAM_CHAT_ID')
        telegram_token = os.getenv('TELEGRAM_TOKEN')
        nasa_api_key = os.getenv('NASA_API_KEY')
        nasa_image_folder = 'NASA images'
        spacex_image_folder = 'SpaceX images'
        create_folder_path(spacex_image_folder)


if __name__ == '__main__':
    main()
