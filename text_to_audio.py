from openai import OpenAI

#
# OpenAI_API_KEY = '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'
#
#
# def calculate_cost(text_string, model_id):
#     cost_tier = {
#         'tts-1': 0.015,
#         'tts-1-hd': 0.03
#     }
#
#     cost_unit = cost_tier.get(model_id, None)
#     if cost_unit is None:
#         return None
#     return (cost_unit * len(text_string)) / 1000
#
# client = OpenAI(api_key=OpenAI_API_KEY)
#
# text_input = "In a quiet village, there lived a curious boy named Leo who loved stargazing. One clear night, while looking at the moon through his telescope, Leo saw the moon wink at him. Astonished, he whispered, I wish I could visit you."
#
# model = 'tts-1'
# voice = 'echo'
#
#
# response = client.audio.speech.create(
#     model=model,
#     input=text_input,
#     voice=voice
# )
#
#
# request_cost = calculate_cost(text_input, model)
# print(f'Cost {request_cost}')
# response.write_to_file('demo_echo.mp3')
#
#




#
# class TextToSpeech:
#     def __init__(self, text_input):
#         self.text_input = text_input
#         self.client = OpenAI(api_key='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')
#         self.cost_tier = {
#             'tts-1': 0.015,
#             'tts-1-hd': 0.03
#         }
#
#     def calculate_cost(self, text_string, model_id):
#         cost_unit = self.cost_tier.get(model_id, None)
#         if cost_unit is None:
#             return None
#         return (cost_unit * len(text_string)) / 1000
#
#     def generate_audio(self, model='tts-1', voice='echo'):
#         response = self.client.audio.speech.create(
#             model=model,
#             input=self.text_input,
#             voice=voice
#         )
#         return response
#
# # Usage
#
#
#
# if __name__ == '__main__':
#     text_input = "In a quiet village, there lived a curious boy named Leo who loved stargazing. One clear night, while looking at the moon through his telescope, Leo saw the moon wink at him. Astonished, he whispered, I wish I could visit you."
#
#     tts = TextToSpeech(text_input)
#     request_cost = tts.calculate_cost(text_input, 'tts-1')
#     print(f'Cost: {request_cost}')
#
#     response = tts.generate_audio(text_input)
#     response.write_to_file('demo_echo.mp3')


class TextToSpeech:
    def __init__(self, text_input):
        self.text_input = text_input
        self.client = OpenAI(api_key='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')
        self.cost_tier = {
            'tts-1': 0.015,
            'tts-1-hd': 0.03
        }

    def calculate_cost(self, model_id):
        cost_unit = self.cost_tier.get(model_id, None)
        if cost_unit is None:
            return None
        return (cost_unit * len(self.text_input)) / 1000

    def generate_audio(self, model='tts-1', voice='echo'):
        response = self.client.audio.speech.create(
            model=model,
            input=self.text_input,
            voice=voice
        )
        return response

# Usage
if __name__ == '__main__':
    text_input = "That night, in his dreams, the moon granted Leo's wish. He found himself bouncing along its silvery surface, laughing with delight as stars twinkled around him. The moon showed Leo the beauty of the universe from its view, and they talked about the secrets of the cosmos."

    tts = TextToSpeech(text_input)
    request_cost = tts.calculate_cost('tts-1')
    print(f'Cost: {request_cost}')

    response = tts.generate_audio()
    response.write_to_file('demo_echo.mp3')

