import descarga_video
import extraer_audio

descarga_video.download_video("https://www.youtube.com/watch?v=avv2IIdDnnk", "video")

extraer_audio.extract_audio("video.webm", "audio.mp3")
