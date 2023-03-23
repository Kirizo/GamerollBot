import random

gry = ["Liga","TF2","Overwatch"]


    
def handle_response(message) -> str:
    p_message = message.lower()
    
    if p_message == '!gra':
        return random.choice(gry)

    #  return 'Yeah, I don\'t know. Try typing "!help".'