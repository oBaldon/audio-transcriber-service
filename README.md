# **Whisper API**

## **Descrição**
A **Whisper API** é um serviço RESTful desenvolvido em Python, que utiliza o modelo **Whisper** da OpenAI para transcrição de áudio. Este projeto foi projetado para receber arquivos de áudio e retornar suas transcrições em texto de forma eficiente e escalável.

---

## **Características**
- Transcrição de áudio precisa utilizando o modelo **Whisper**.
- Suporte a múltiplos formatos de áudio.
- API modular e escalável com boas práticas de design.
- Verificação de integridade da API por meio de endpoints de health-check.
- Pronto para execução em ambientes de desenvolvimento e produção.

---

## **Estrutura do Projeto**
```plaintext
whisper-api/
│
├── app/
│   ├── __init__.py          # Inicializa a aplicação Flask
│   ├── main.py              # Ponto de entrada principal da API
│   ├── routes/              # Rotas organizadas modularmente
│   │   ├── transcribe.py    # Rota para transcrição de áudio
│   │   └── health.py        # Rota para health-check
│   ├── services/            # Lógica de negócios da API
│   │   └── transcriber.py   # Integração com o modelo Whisper
│   ├── utils/               # Utilitários para manipulação de áudio
│   │   └── audio_utils.py   # Funções para conversão de formatos de áudio
│   └── models/              # (Opcional) Modelos de dados
│
├── tests/                   # Testes automatizados
│   ├── test_transcribe.py   # Testes para a rota de transcrição
│   └── test_health.py       # Testes para a rota de health-check
│
├── .env                     # Variáveis de ambiente (não versionado)
├── .gitignore               # Arquivos/pastas ignorados pelo Git
├── requirements.txt         # Dependências do projeto
└── README.md                # Documentação do projeto
```

---

## **Instalação**

### **Pré-requisitos**
- Python 3.8 ou superior
- Pip (gerenciador de pacotes)
- Ambiente virtual Python (recomendado)
- Modelo Whisper da OpenAI

### **Passo a Passo**
1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/whisper-api.git
   cd whisper-api
   ```

2. Crie e ative um ambiente virtual:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Linux/MacOS
   venv\Scripts\activate     # Windows
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Inicie o servidor:
   ```bash
   python -m app.main
   ```

---

## **Uso**

### **Endpoints**
#### **1. Health Check**
- **URL:** `/health/`
- **Método:** `GET`
- **Descrição:** Verifica se a API está funcionando corretamente.
- **Exemplo de Resposta:**
  ```json
  {
    "status": "API is running"
  }
  ```

#### **2. Transcrição de Áudio**
- **URL:** `/transcribe/`
- **Método:** `POST`
- **Descrição:** Recebe um arquivo de áudio e retorna sua transcrição.
- **Parâmetros:**
  - `audio` (form-data): Arquivo de áudio a ser transcrito.
- **Exemplo de Resposta:**
  ```json
  {
    "transcription": "Texto transcrito do áudio"
  }
  ```

### **Exemplo de Requisição com cURL**
```bash
curl -X POST -F "audio=@/caminho/para/audio.wav" http://127.0.0.1:5000/transcribe/
```

---

## **Testes**
Para rodar os testes automatizados:
1. Instale o `pytest`:
   ```bash
   pip install pytest
   ```
2. Execute os testes:
   ```bash
   pytest tests/
   ```

---

## **Produção**
### **Usando Gunicorn**
Recomenda-se usar o Gunicorn para produção:
```bash
gunicorn -w 4 -b 0.0.0.0:5000 app.main:app
```

### **Usando Docker**
1. Construa a imagem:
   ```bash
   docker build -t whisper-api .
   ```
2. Execute o container:
   ```bash
   docker run -p 5000:5000 whisper-api
   ```

---

## **Contribuição**
Contribuições são bem-vindas! Sinta-se à vontade para abrir **issues** ou enviar **pull requests**.

---

## **Licença**


---
