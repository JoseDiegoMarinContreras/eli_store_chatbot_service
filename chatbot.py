from nltk.chat.util import Chat, reflections

pairs = [
    ['Mi nombre es (.*)', ['Hola %1', 'Un gusto conocerte %1', 'Hola, en que puedo ayudarte %1?']]
]

EliStoreChatbot = Chat(pairs, reflections)
#chat.converse()
#response_demo = chat.respond('Mi nombre es Jose Diego')

#print(response_demo)