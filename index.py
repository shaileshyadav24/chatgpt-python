from openai import OpenAI
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
apiKey =  os.environ.get('api-key')

client = OpenAI(api_key= apiKey)

class chatbot:
    def __init__(self):
        self.chatMessages = [
            {"role": "system", "content": "You are a helpful assistant."}
        ]

    def chat(self, message):
        self.chatMessages = self.chatMessages + [{ "role": "user", "content": message }]
        completion = client.chat.completions.create(
            model="gpt-4-turbo-preview",
            messages=self.chatMessages
        )
        print("Answer:", completion.choices[0].message.content)

print("Hello! Please start asking question")
inputMessage = ""

chat = chatbot()
while inputMessage != "Thank you":
    inputMessage = input("Question:")
    chat.chat(inputMessage)

print("Thank you for using chatbox!!!")






