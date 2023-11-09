from moviepy.editor import VideoFileClip
import speech_recognition as sr

def extract_text_from_video(video_path):
    try:
        clip = VideoFileClip(video_path)
        clip.audio.write_audiofile("temp_audio.wav")

        recognizer = sr.Recognizer()
        with sr.AudioFile("temp_audio.wav") as source:
            audio_data = recognizer.record(source)
            try:
                text = recognizer.recognize_google(audio_data, language="pt-BR")
                print("Texto extraído do vídeo:", text)
                return text
            except sr.UnknownValueError:
                print("Não foi possível entender o áudio do vídeo.")
                return None
            except sr.RequestError as e:
                print(f"Não foi possível solicitar resultados do serviço de reconhecimento; {e}")
                return None
    except Exception as e:
        print(f"Erro ao processar o vídeo: {e}")
        return None
