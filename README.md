# ChatBotTemporalizadoBibliotecas Utilizadas
O código faz uso das seguintes bibliotecas:

pywhatkit: Uma biblioteca do Python que fornece uma interface para enviar mensagens pelo WhatsApp utilizando a API Web do WhatsApp.
keyboard: Uma biblioteca do Python que permite a simulação de teclas pressionadas e liberadas no teclado.
time: Uma biblioteca do Python que fornece funções relacionadas ao tempo, como pausas.
datetime: Uma biblioteca do Python que fornece classes para manipular datas e horários.
Variáveis
contato: Uma lista que armazena os números de telefone dos contatos para os quais as mensagens serão enviadas. Os números devem ser inseridos no formato "+CÓDIGO_PAÍS DDD NÚMERO" (por exemplo, "+5511987654321" para um número no Brasil).
Loop Principal
O código possui um loop while que executa enquanto o tamanho da lista contato for maior ou igual a 1. Isso significa que o código continuará a enviar mensagens até que todos os contatos tenham sido processados.

Dentro do loop, as seguintes ações são realizadas:

pywhatkit.sendwhatmsg(contato[0], 'Esta mensagem é automatizada, ChatBot', datetime.now().hour,datetime.now().minute+1): Esta linha envia uma mensagem para o primeiro contato da lista contato. A mensagem enviada é "Esta mensagem é automatizada, ChatBot". O horário de envio é obtido utilizando a função datetime.now(), que retorna a data e hora atual, e são passados apenas a hora e o minuto para a função sendwhatmsg.

del contato[0]: Após o envio da mensagem, o primeiro contato da lista contato é removido, para que o próximo contato seja processado na próxima iteração do loop.

time.sleep(20): O código pausa a execução por 20 segundos antes de prosseguir para a próxima iteração do loop. Isso garante um intervalo entre o envio de mensagens para evitar problemas com limites de uso da API do WhatsApp.

keyboard.press_and_release('ctrl + w'): Essa linha simula a combinação de teclas "Ctrl + W", que fecha a janela ativa do navegador. Essa ação é realizada para fechar a janela do WhatsApp Web após o envio da mensagem, preparando para o próximo envio.

Após o loop, o código termina sua execução.
