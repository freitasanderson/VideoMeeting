# REDES DE COMPUTADORES
## Conferência de vídeo em grupo

#### Esse projeto usa as bibliotecas asyncio e websockets para criar uma aplicação de videoconferência em grupo.

### Funcionamento do Projeto:
#### Servidor WebSocket: 
Inicia um servidor WebSocket que aceita conexões de múltiplos clientes. Quando recebe um frame de vídeo de um cliente, o servidor envia esse frame para todos os outros clientes conectados.

#### Cliente WebSocket: 
Conecta-se ao servidor WebSocket e inicia a captura de vídeo da câmera. Cada frame de vídeo capturado é convertido em Base64 e enviado para o servidor. O cliente também recebe os frames de vídeo dos outros clientes conectados e os exibe localmente usando OpenCV.

[Link do Vídeo de demonstação](https://youtube.com/shorts/MYzu-d4xWpQ?feature=share)

### Documentação das Bibliotecas e Conceitos Utilizados:
#### Asyncio (asyncio):
Biblioteca para escrever código assíncrono em Python. Facilita a escrita de programas concorrentes usando corrotinas e await.
asyncio.run(): Função para executar a corrotina principal.
async with: Context manager usado para lidar com a conexão WebSocket de forma assíncrona.

#### WebSockets (websockets):
Implementação assíncrona de WebSockets para Python.
websockets.serve(): Inicia um servidor WebSocket na interface especificada ("0.0.0.0" para todas as interfaces).
websockets.connect(): Conecta-se a um servidor WebSocket.

#### OpenCV (cv2):

Biblioteca de visão computacional usada para capturar, processar e exibir vídeo.
cv2.VideoCapture(): Inicia a captura de vídeo da câmera.
cv2.imencode(): Codifica um frame de imagem em um formato específico (neste caso, JPEG).
cv2.imdecode(): Decodifica um buffer de imagem em um array NumPy.

#### NumPy (numpy):
Biblioteca fundamental para computação numérica em Python.
np.frombuffer(): Cria um array NumPy a partir de um buffer de dados.

#### Base64 (base64):
Módulo Python para codificar e decodificar dados usando o algoritmo Base64.
Usado para converter os frames de imagem em strings Base64 antes de enviá-los pelo WebSocket e para decodificar os frames recebidos de volta para imagens.
