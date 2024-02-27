import yt_dlp
from yt_dlp.utils import download_range_func
import os

print("1 - Áudio")
print("2 - Vídeo")
select_format = int(input("Selecione o formato: "))


def format_selector(select_format):
    if select_format == 1:
        return 'mp3/bestaudio/best'
    elif select_format == 2:
        return "bv*[ext=mp4]+ba[ext=m4a]/b[ext=mp4] / bv*+ba/b"
    else:
        raise ValueError("Tipo de mídia inválido. Por favor, selecione 1 para áudio ou 2 para vídeo.")


url = input("url: ")

download_path = input("Pasta (vazio para diretório atual): ")
path = os.path.abspath(download_path)

ydl_opts = {
    'format': format_selector(select_format),
    'outtmpl': os.path.join(path, '%(title)s.%(ext)s'),
}

if select_format == 1:
    ydl_opts['postprocessors'] = [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
    }]
elif select_format == 2:
    duration = input("Deseja salvar uma parte específica? OBS: Somente vídeo\n(Ex: baixar até 06:23)\nS/N\n")

    if duration == "n":
        pass
    else:
        initial_time_input = input("Em que minuto iniciar? (Padrão: 0)\n")
        initial_time = int(initial_time_input) if initial_time_input else 0
        final_time = int(input("Digite a duração final: (Formato XX:XX)\n"))
        ydl_opts = {
            'download_ranges': download_range_func(None, [(initial_time, final_time)])
        }


with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    error_code = ydl.download(url)
