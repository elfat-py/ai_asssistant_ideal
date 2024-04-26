from ai_asssistant_ideal.audio_to_text import AudioToText
from ai_asssistant_ideal.logic import SoulutionSuggestion
import json
from text_to_audio import TextToSpeech

def read_txt(filePath):
    with open(filePath, 'r') as file:
        # Read the entire content of the file as a string
        return file.read()

def get_content_json(filePath):
        # Open the JSON file
    with open(filePath, 'r') as file:
        # Parse the JSON data
        data = json.load(file)
        # Get the content as a string
        content_string = data['choices'][0]['message']['content']
        return content_string


def main():
    # Converted Audio to text
    audio = AudioToText(r'/how_website.m4a')
    audio.speech_to_text()


    path_file = r'/transcription.txt'
    user_request = read_txt(path_file)

    # Give response to audio
    solution_suggestion = SoulutionSuggestion(user_request)

    # Get AI response
    content_string = get_content_json(r'/data/response_logic.json')


    # Pass it as voice
    tts  = TextToSpeech(content_string)
    response_assistant_speech = tts.generate_audio()
    response_assistant_speech.write_to_file('demo_echo.mp3')

if __name__ == '__main__':
    main()
