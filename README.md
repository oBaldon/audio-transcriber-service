# 🎙️ Audio Transcriber Service

Este é um microserviço para **transcrição automática de arquivos de áudio** utilizando o modelo de transcrição **Whisper** da OpenAI. Ele oferece uma API RESTful baseada em **FastAPI** para receber arquivos de áudio, processá-los e retornar o texto transcrito. O serviço suporta múltiplos formatos de áudio e é otimizado para operação em ambientes de produção com Docker.

---

## 🚀 Funcionalidades

- Recepção de arquivos de áudio via endpoint HTTP.
- Transcrição automática utilizando o modelo **Whisper (original)**.
- Alinhamento palavra por palavra com **WhisperX**.
- Diarização de locutores (quem falou o quê) com **WhisperX + PyAnnote**.
- Suporte a formatos de áudio populares:
  - `wav`, `mp3`, `flac`, `ogg`, `webm`, `m4a`
- Configuração simplificada via Docker e `.env`.

---

## ✅ Requisitos

- **Python 3.12+**
- **ffmpeg** instalado no servidor
- Dependências definidas em `requirements.txt`

---

## ⚙️ Instalação e Execução

### 1. Clonar o repositório
```bash
git clone https://github.com/oBaldon/audio-transcriber-service.git
cd audio-transcriber-service
```

### 2. Criar e ativar o ambiente virtual
```bash
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

### 3. Instalar as dependências
```bash
pip install -r requirements.txt
```

### 4. Iniciar o microserviço
```bash
uvicorn app:app --host 0.0.0.0 --port 8000
```

---

## 📡 Uso da API

### **Endpoint:** `/transcribe/`
- **Método:** `POST`
- **Descrição:** Recebe um arquivo de áudio e retorna a transcrição completa com alinhamento e, se possível, diarização.

### **Exemplo de requisição com `curl`:**
```bash
curl -X POST "http://localhost:8000/transcribe/" \
     -F "file=@/path/to/sample_audio.wav;type=audio/wav"
```

### **Exemplo de resposta JSON:**
```json
{
  "language": "pt",
  "text": "Transcrição completa do áudio aqui.",
  "segments": [
    {
      "start": 0.0,
      "end": 3.2,
      "text": "Olá, tudo bem?",
      "words": [
        { "word": "Olá,", "start": 0.0, "end": 1.0 },
        { "word": "tudo", "start": 1.1, "end": 2.0 },
        { "word": "bem?", "start": 2.1, "end": 3.2 }
      ],
      "speaker": "SPEAKER_00"
    }
  ]
}
```

---

## 🧪 Testes (INDISPONÍVEL)

Os testes automatizados foram implementados utilizando **pytest**, cobrindo os principais fluxos do microserviço, incluindo:
- Upload de arquivos válidos.
- Verificação de erros em uploads inválidos.

### Para executar os testes:
```bash
pytest
```

---

## 📦 Execução com Docker

### 1. Construir a imagem Docker
```bash
docker build -t audio-transcriber-service .
```

### 2. Executar o contêiner
```bash
docker run -p 8000:8000 audio-transcriber-service
```

O serviço estará disponível em: [http://localhost:8000](http://localhost:8000)

### 3. Ou execute com Docker Compose:
```bash
docker-compose up --build
```

---

## ⚙️ Configuração por `.env`

Você pode definir as configurações no arquivo `.env`:

```env
APP_PORT=8000
DEBUG=True
WHISPER_MODEL=large
MAX_AUDIO_DURATION=300
UPLOAD_FOLDER=temp/
HUGGINGFACE_TOKEN=seu_token_aqui
COMPUTE_TYPE=auto
```

---

## 📁 Estrutura do Projeto

```
audio-transcriber-service/
│
├── app.py                  # Aplicação FastAPI principal
├── services/               # Serviços de transcrição, alinhamento, diarização
├── utils/                  # Manipulação de arquivos (uploads, SRT, JSON)
├── config/                 # Configurações de ambiente
├── tests/                  # Testes automatizados com pytest
├── Dockerfile              # Definição da imagem Docker
├── docker-compose.yml      # Orquestração com Docker Compose
├── requirements.txt        # Dependências Python
└── README.md               # Documentação do projeto
```

---

## 🛠 Tecnologias Utilizadas

- **Python 3.12**
- **FastAPI**
- **Whisper (OpenAI)**
- **WhisperX (alinhamento e diarização)**
- **ffmpeg**
- **Docker & Docker Compose**
- **pytest**

---

## 👤 Autor

Desenvolvido por [@oBaldon](https://github.com/oBaldon) e [@TiagoComeron](https://github.com/TiagoComeron)

Contribuições e sugestões são bem-vindas!

---

## 📎 Links úteis

- 📍 [ROADMAP Técnico do Projeto](./ROADMAP.md)
