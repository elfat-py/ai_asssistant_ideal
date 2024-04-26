import whisper

# Works
class AudioToText:
    def __init__(self, sound_file):
        self.sound_file = sound_file

    def speech_to_text(self):

        model = whisper.load_model("base")
        result = model.transcribe(self.sound_file, fp16=False)
        # result = model.transcribe(r"D:\Users\User\pythonProject\aiAsistant\Recording (7).m4a", fp16=False)

        with open('transcription.txt', 'w') as f:
            f.write(result['text'])




if __name__ == '__main__':
    audio = AudioToText(r'/demo_echo.mp3')
    audio.speech_to_text()

