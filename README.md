ChatBot - Aplicativo Python para Enviar Mensagens no WhatsApp

Este aplicativo é um script Python simples que permite enviar mensagens automatizadas no WhatsApp.

Recursos:

Agendamento do envio de mensagens para um horário específico
Conteúdo da mensagem personalizável
Interface amigável ao usuário
Tratamento de erros para entradas inválidas e falhas no envio

Requisitos:

Python 3.x
tkinter
pywhatkit
keyboard

Instalação:

Baixe os arquivos de script Python front.py e main.py.
Instale as bibliotecas necessárias usando pip install tkinter pywhatkit keyboard.

Uso:

Abra main.py em seu editor de texto preferido.
Execute o script usando python main.py.

Na interface do usuário, insira as seguintes informações:
Número do Contato: Número de telefone do destinatário (formato internacional com código do país).
Mensagem: Conteúdo da mensagem a ser enviada.
Horário (hh:mm): Hora para enviar a mensagem (formato 24 horas).
Clique no botão "Enviar Mensagem".
Se for bem-sucedido, uma caixa de mensagem confirmará o envio da mensagem.
O aplicativo fecha automaticamente a janela do navegador após o envio da mensagem.
Observação: Este aplicativo requer acesso à sua interface web do WhatsApp. Certifique-se de que seu telefone esteja conectado à Internet e o WhatsApp Web esteja aberto no seu navegador.

Contribuições:
Este aplicativo é de código aberto e aceita contribuições. Sinta-se à vontade para bifurcar o repositório e enviar solicitações de pull com melhorias ou novos recursos.

Exemplo de uso:
Para enviar uma mensagem para o número 55512345678 às 10h00, digite as seguintes informações na interface do usuário:

Número do Contato: 55512345678
Mensagem: Olá, tudo bem?
Horário (hh:mm): 10:00
Após clicar no botão "Enviar Mensagem", a seguinte caixa de mensagem será exibida:

Mensagem enviada com sucesso!
A mensagem também será enviada para o WhatsApp do destinatário.
