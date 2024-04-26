import configparser
import os.path
import requests
import base64
import json


class SoulutionSuggestion:
    def __init__(self, old_title):
        #self.api_key = self.get_api_key()
        self.api_key = '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'
        self.title = old_title
        self.rename_song_title()



    @staticmethod
    def get_api_key():
        config = configparser.ConfigParser()
        get_path = os.path.join(r'../../YoutubeMusicAutomation/Resources/configKeys.ini')
        config.read(get_path)
        return config['API']['OPENAI-APIKEY']

    def rename_song_title(self):
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }
        payload = {
            "model": "gpt-3.5-turbo-0125",
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": "If you are asked how the website works provide this response: 'This website is made so that people can track the status of their documents this will be a great help for people as they will be in direct touch with the services provided by gov'"

                        },
                        {
                            "type": "text",
                            "text": f"{self.title}"

                        }
                    ]
                }
            ],
            "max_tokens": 300
        }
        response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
        if response.status_code == 200:
            serialized_json = response.json()
            self.save_json_response(response=serialized_json)
            print('-----------------------')
            print('Title has been generated!')
            print('-----------------------')

    @staticmethod
    def save_json_response(response):
        with open(r'/data/response_logic.json',
                  'w', encoding='utf-8') as f:
            json.dump(response, f, ensure_ascii=False, indent=4)

    @staticmethod
    def read_json_response():
        with open(r'../../YoutubeMusicAutomation/Resources/Data/openai_response_title.json',
                  'r', encoding='utf-8') as f:
            data = json.load(f)
        content = data["choices"][0]["message"]["content"]
        return content


if __name__ == '__main__':
    rename_song = SoulutionSuggestion(r"How does the website works?")