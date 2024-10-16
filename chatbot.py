import nltk
from nltk.chat.util import Chat, reflections
nltk.download('punkt')

pairs = [
    [
        r'hi|hello|hey',
        ['Hello!', 'Hi there!', 'Hey! How can I help you?']
    ],
    [
        r'how are you?',
        ['I am fine, thank you!, what about you?', 'Doing well, how about you?']
    ],
    [
        r'what is your name?',
        ['I am a basic chatbot created to assist you.']
    ],
    [
        r'quit|exit',
        ['Nice to meet you! Have a great day!']
    ],
    [
        r'(.*)',
        ['I am not sure I understand. Could you please rephrase?']
    ]
]

chatbot = Chat(pairs, reflections)

def chat():
    print("Hello! I am a chatbot. Type 'quit' to exit.")
    chatbot.converse()

if __name__ == "__main__":
    chat()