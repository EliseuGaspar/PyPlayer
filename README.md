<img src="https://github.com/EliseuGaspar/PyPlayer/blob/master/assets/label-logo2.png" width="100%">



# Um modúlo perfeito para áudios MP3



PyPlayer é um modúlo para manipulação de áudios no formato MP3. O mesmo foi criado em Janeiro de 2023 com o objectivo de ser um modúlo fácil de usar e completo no contexto de manipulação de áudios MP3.

## O que o torna especial ?

O PyPlayer tende a ser especial porque cobre todas as necessidades que um desenvolvedor teria ao criar qualquer aplicação que envolva reprodução de áudios.

O PyPlayer foi criado principalmente com o intuito de apoiar a construção de um player de áudio. Inicialmente ele conta com o suporte a arquivos no formato MP3, mas é claro que no futuro poderá suportar também outros formatos como: [WAV,OGG,MP4].

O Nome do modúlo é PyPlayer e não Pyaudio ou PyPlayerAudio, ou seja o foco não é que o PyPlayer seja apenas um modúlo para áudios mas para videos[MP4,MKV] também.Exemplo do Modúlo PyPlayer

## Instalando o PyPlayer

```bash

pip install PyPlayer

```

## Exemplos de como alguns metódos e classes podem ser usados


```python
from PyPlayer import PlayerMixer as p

p.load(dir='D:/exemplo/mp3files');

p.play() # Este metódo toca a música corrente

p.pause() # Este metódo pausa a música corrente

p.restart() # Este metódo reinicia o player com o mesmo diretório
```

```python
from PyPlayer import PlayerMixer as p

p.load(file='D:/exemplo/mp3files/one.mp3');

p.play() # Este metódo toca a música corrente

p.pause() # Este metódo pausa a música corrente

p.restart() # Este metódo reinicia o player com o mesmo diretório
```
***Note que no primeiro exemplo passamos o caminho de um diretório para class `load()` usando o paramêtro `dir="path of folder with mp3 files"`. Já no segundo passamos o caminho de um arquivo  mp3 para a  class `load()` usando o paramêtro `file="path of mp3 files"`.***

# Metódos do PyPlayer

class | ação
:------- | :------
**load()** | <u>carrega os arquivos mp3</u>
 **play()** | <u>toca o arquivo em execução</u>
 **pause()** | <u>pausa a execução do arquivo em execução</u>
 **unpause()** | <u>descongela a execução do arquivo em execução</u>
 **stop()** | <u>para e reinicia a execução do arquivo em execução</u>
 **next_()** | <u>executa o proximo arquivo mp3 se houver</u>
 **back()** | <u>executa o arquivo anterior ao atual se houver</u>
 **getvolume()** | <u>retorna o nível atual do volume do áudio</u> 
 **setvolume()** | <u>altera o nível do volume do áudio</u> 
 **current_time()** |  <u>retorna o tempo atual do arquivo em execução</u>
 **settime()** | <u>muda o tempo atual do arquivo em execução</u>
 **duration()** | <u>retorna o tempo total do arquivo em execução</u>
 **current_file()** | <u>retorna o arquivo atual em execução</u> 
 **list_()** | <u>retorna em forma de lista todos os áudios encontrados no diretório carregado</u> 
 **tags()** | <u>retorna as tags do arquivo</u>

# Criando Um Player de Terminal

Supondo que tu já tenhas o PyPlayer instalado no seu computador vamos partir direto para o código.

**Passo 1:**

*Criar a estrutura do nosso diretório*

<img src="assets\label-estruture.png" alt="label-estruture"/>

> Primeiro criamos a pasta raíz **TerminalPlayer**, dentro dela criamos as pastas **audios** e **cgs** bem como o nosso arquivo **app.py**.
>
> O arquivo **app.py** será o responsável pela criação do nosso player.
>
> A pasta **audios** guardará os audios que iremos tocar.
>
> Já a pasta **cgs** que é necessária para o funcionamento do PyPlayer é nesta pasta onde o PyPlayer criará os arquivos que usará para rodar perfeitamente.

**Passo 2:**

*Codar o arquivo app.py*

```python
# Primeiro passo: Sem pacotes não há programa
import keyboard as k
from PyPlayer import PlayerMixer as p
from os import system

# Segundo passo: Um player sem audios não é um player
p.load(dir="audios") # Passamos para o paramêtro `dir` o caminho da pasta audios.
p.play() # Depois de carregado os arquivos tocamos eles.
print(
    "Welcome in TerminalPlayer 2023"
) # Pode até ser um `console application` mais não deixa de ser uma aplicação.

# Terceiro passo: Sem controles não é divertido

while True:

    print(
        f"Current_Music: {p.current_file()}"
    ) # Printamos na tela o retorno do metódo current_file --> que retorna a faixa que está sendo executada.

    print(
        f"time: {p.current_time()}/{p.duration()}"
    ) # Printamos aqui o tempo atual e o tempo total da faixa que está sendo tocada.
	
    # Este bloco de código lê as combinações de teclados passadas e executa o method ou class associados a elas
    if k.is_pressed('ctrl+space'):
        p.play()
    elif k.is_pressed('ctrl+u'):
        p.unpause()
    elif k.is_pressed('ctrl+p'):
        p.pause()
    elif k.is_pressed('ctrl+right'):
        p.next_()
    elif k.is_pressed('ctrl+left'):
        p.back()
    elif k.is_pressed('ctrl+left'):
        p.back()
    elif k.is_pressed('esc'):
        break

    system('cls')
    # Bom! Esperamos que esse exemplo te ajude muito ao usar este Pacote.
```

# Estrutura do PyPlayer

O **PyPlayer** foi criado usando outros modúlos como, ´Pygame´; ´Mutagen´; ´Json´.
O foco não é só criar um modúlo perfeito para a execução de **arquivos mp3(e outros formatos no futuro)**, o foco é tornar o **PyPlayer** um modúlo útil na edição dos mesmos  e também na execução de **arquivos mp4(videos)**.

## Documentação

> O PyPlayer ainda está em desenvolvimento e por isso não existe online uma documentação legal para o mesmo.

## Participações

> Sendo um modúlo gratuito e open source todo mundo(Python Dev's) é convidado para contribuir.

**Copyright © - Eliseu Gaspar** 