""" This file contains parameters and configurations for the bot """
# URLs for Instagram Reels, YouTube Shorts and VK Clips
IG_URLS = ['https://www.instagram.com/reel/']
YT_URLS = ['https://youtube.com/shorts/', 'https://www.youtube.com/shorts/']
VK_URLS = ['https://vk.com/clip-', 'https://vkvideo.ru/clip-']

""" User-updatable parameters part """
# YouTube Shorts & VK Clips download options
YDL_OPTS = {
    'format': 'bestvideo+bestaudio/best',    # разрешение
    'outtmpl': '%(title)s.%(ext)s',  # Шаблон имени файла
    'merge_output_format': 'mp4',    # Формат выходного файла
    'noplaylist': True,              # Не загружать плейлисты
    'quiet': True                    # Выводить меньше информации
}

# Video thumbnails option
IS_THUMBS = True
IS_SHORTS = True
IS_REELS = True
IS_VKCLIPS = True

# TG bot administrator ID
ADMIN_USERNAME = None
