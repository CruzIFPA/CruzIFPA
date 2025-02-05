from pytube import YouTube

# URL do vídeo do YouTube
url = 'https://www.youtube.com/watch?v=NQ6zNXX4qCo'

# Criar o objeto YouTube
yt = YouTube(url)

# Melhor resolução
#video = yt.streams.get_highest_resolution()

#Resolução ajusatáve
video = yt.streams.filter(res="360p", file_extension="mp4").first()

# Fazer o download
video.download(output_path='caminho/do/diretorio', filename='nome_do_video.mp4')

print("Download concluído!")
    
