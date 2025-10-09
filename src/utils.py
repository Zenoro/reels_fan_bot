from re import match, Match
import yt_dlp
import requests
from PIL import Image
from io import BytesIO
import logging


# Настройка логгера
logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    filename="bot.log",
    encoding="utf-8",
    filemode="w",
    format="{asctime} - {levelname} - {message}",
    style="{",
    datefmt="%Y-%m-%d %H:%M",
)


def print_log(msg: str, level: str = "info") -> None:
    print(msg)
    if level == "info":
        logger.info(msg)
    elif level == "error":
        logger.error(msg)
    elif level == "exception":
        logger.exception(msg)
    else:
        logger.debug(msg)


def match_urls(urls: list[str], text: str) -> Match:
    return match(fr"(({'|'.join(urls)})\S*)\s*(.*)", text)


def get_tg_username(message: dict) -> str:
    if message.forward_from:
        return message.forward_from.username
    else:
        return message.from_user.username


def crop_to_vertical(
        image_bytes: bytes,
        save_path: str,
        aspect_ratio: tuple[int, int] = (9, 16)) -> str:
    image = Image.open(BytesIO(image_bytes))
    width, height = image.size
    target_ratio = aspect_ratio[0] / aspect_ratio[1]
    new_height = height
    new_width = int(new_height * target_ratio)

    if new_width > width:
        new_width = width
        new_height = int(new_width / target_ratio)

    left = (width - new_width) // 2
    top = (height - new_height) // 2
    right = left + new_width
    bottom = top + new_height

    cropped = image.crop((left, top, right, bottom))
    cropped.save(save_path)
    print_log(f"Thumbnail cropped to {aspect_ratio=}")
    return save_path


def dwld_YTDLP_video(url: str, ydl_opts: dict) -> tuple[str, dict] | None:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        # Получаем информацию о видео перед скачиванием
        info = ydl.extract_info(url, download=False)
        filename = ydl.prepare_filename(info)
        print_log(f"Скачивание видео: {filename}")
        ydl.download([url])
        return filename, info


def dwld_YTThumb(info: dict, save_path: str) -> None:
    # Получаем информацию о видео
    thumbnail_url = info.get('thumbnail', [])

    # Загружаем картинку
    response = requests.get(thumbnail_url)

    if response.status_code == 200:
        print_log("Thumbnail downloaded successfully.")
        crop_to_vertical(response.content, save_path)
        return save_path
    else:
        print_log("Failed to retrieve thumbnail.", "error")


if __name__ == "__main__":
    # Пример использования функции
    text = "https://youtube.com/shorts/YWkYaM3Wd6c?si=plN-okCoEXbbk4eR"
    with yt_dlp.YoutubeDL(__import__("params").YDL_OPTS) as ydl:
        info = ydl.extract_info(text, download=False)

    dwld_YTThumb(info, 'thumbnail.jpg')
