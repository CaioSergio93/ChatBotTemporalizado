import pywhatkit
import keyboard
import time
from datetime import datetime

contato=['+55'] #colocar codigo do pais, ddd e numero com o 9 na frente (brasi)


while len(contato)>=1:
    pywhatkit.sendwhatmsg(contato[0], 'Esta mensagem é automatizada, ChatBot', datetime.now().hour,datetime.now().minute+1)
    del contato[0]
    time.sleep(20)
    keyboard.press_and_release('ctrl + w')
    
    