### **Audio Transcriber Service**
Este é um microserviço para **transcrição automática de arquivos de áudio** utilizando o modelo de transcrição **Whisper**. Ele oferece uma API RESTful baseada em **FastAPI** para receber arquivos de áudio, processá-los e retornar o texto transcrito. O serviço suporta múltiplos formatos de áudio e é otimizado para operação em ambientes de produção com Docker.

---

### **Funcionalidades**
- Recepção de arquivos de áudio via endpoint HTTP.
- Transcrição automática utilizando o modelo Whisper.
- Suporte a formatos de áudio populares:
  - `wav`
  - `mp3`
  - `flac`
  - `ogg`
  - `webm`
  - `m4a`
- Configuração simplificada via Docker e `.env`.

---

### **Requisitos**
- **Python 3.12+**
- **ffmpeg** instalado no servidor
- Dependências definidas em `requirements.txt`

---

### **Instalação e Execução**

#### **1. Clonar o repositório**
```sh
git clone https://github.com/oBaldon/audio-transcriber-service.git
cd audio-transcriber-service
```

#### **2. Criar e ativar o ambiente virtual**
```sh
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

#### **3. Instalar as dependências**
```sh
pip install -r requirements.txt
```

#### **4. Iniciar o microserviço**
```sh
uvicorn app:app --host 0.0.0.0 --port 8000
```

---

### **Uso da API**

#### **Endpoint:** `/transcribe/`
- **Método:** `POST`
- **Descrição:** Recebe um arquivo de áudio e retorna a transcrição em formato JSON.
  
**Exemplo de requisição usando `curl`:**
```sh
curl -X POST "http://localhost:8000/transcribe/" \
     -F "file=@/path/to/sample_audio.wav"
```

**Exemplo de resposta:**
```json
{
    "transcription": "Este é o texto transcrito do áudio."
}
```

---

### **Testes**

Os testes automatizados foram implementados utilizando **pytest**. Eles cobrem os principais fluxos do microserviço, incluindo:
- Upload de arquivos de áudio válidos.
- Manipulação de erros, como caminhos de arquivos inválidos.

Para executar os testes, utilize o comando:
```sh
pytest
```

---

### **Execução com Docker**

#### **1. Construir a imagem Docker**
```sh
docker build -t audio-transcriber-service .
```

#### **2. Executar o contêiner**
```sh
docker run -p 8000:8000 audio-transcriber-service
```

Agora o serviço estará disponível em `http://localhost:8000`.

---

### **Configuração**

Você pode utilizar um arquivo `.env` para definir variáveis de configuração como:

- **`APP_PORT`**: Porta em que o aplicativo será executado (padrão: `8000`).
- **`DEBUG`**: Define o modo de depuração (`True` ou `False`).
- **`WHISPER_MODEL`**: Modelo a ser utilizado pelo Whisper (`tiny`, `base`, `small`, `medium`, `large`). O padrão é **`large`**.
- **`MAX_AUDIO_DURATION`**: Limite máximo de duração do áudio em segundos (opcional).
- **`UPLOAD_FOLDER`**: Diretório temporário para upload de arquivos (opcional).

---

**Exemplo de `.env`:**
```env
APP_PORT=8000
DEBUG=True
WHISPER_MODEL=medium
MAX_AUDIO_DURATION=300
UPLOAD_FOLDER=/tmp/uploads
```

---

### **Estrutura do Projeto**

```
audio-transcriber-service/
│
├── app.py                # Código principal da aplicação FastAPI
├── services/             # Lógica de serviços (ex.: whisper_service.py)
├── utils/                # Utilitários para manipulação de arquivos
├── tests/                # Arquivos de teste (pytest)
├── Dockerfile            # Definição da imagem Docker
├── requirements.txt      # Dependências do projeto
└── README.md             # Documentação do projeto
```

---

### **Tecnologias Utilizadas**
- **Python 3.12**
- **FastAPI** (API REST)
- **Whisper** (Modelo de transcrição)
- **ffmpeg** (Manipulação de áudio)
- **Docker** (Conteinerização)
- **pytest** (Testes automatizados)

---

### **Autor**
Desenvolvido por...  
Contribuições e sugestões são bem-vindas! ✨

Se precisar de mais informações ou encontrar problemas, sinta-se à vontade para abrir uma **issue** no repositório.

--- 