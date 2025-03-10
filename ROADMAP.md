# 📍 Roadmap Técnico – Audio Transcriber Service

Este roadmap apresenta as etapas de evolução técnica do projeto `audio-transcriber-service`, com foco em organização, qualidade, testes e escalabilidade.

---

## 🔹 Fase 1 — Qualidade de Código e Arquitetura
✅ Já iniciado com sucesso, foco em:
- [x] Separação de responsabilidades por serviço (transcrição, alinhamento, diarização).
- [x] Melhoria no retorno da API (sem caminhos locais).
- [x] Organização modular e limpa.

### Ações pendentes:
- [ ] Adicionar docstrings detalhadas nos endpoints da FastAPI (Swagger/OpenAPI).
- [ ] Substituir `print()` por `logging` estruturado com níveis (`INFO`, `WARNING`, `ERROR`).
- [ ] Ajustar exceções específicas no `try/except` da transcrição.

---

## 🔹 Fase 2 — Melhorias Funcionais
- [ ] Adicionar parâmetros de qualidade no `whisper_service`:
  - `beam_size=5`, `best_of=5` como padrão (ou configurável via `.env`).
- [ ] Permitir desativar diarização via `.env` (`ENABLE_DIARIZATION=True/False`).
- [ ] Adicionar fallback se idioma não for suportado pelo modelo de alinhamento.

---

## 🔹 Fase 3 — Testes Automatizados
- [ ] Criar estrutura em `tests/` com `pytest`.
- [ ] Testar casos válidos e inválidos com `TestClient` da FastAPI.
- [ ] Cobrir serviços com testes unitários individuais (mock de whisperx).

---

## 🔹 Fase 4 — Produção e Performance
- [ ] Criar endpoint `/healthcheck` para uso com load balancers/monitoramento.
- [ ] Criar tarefa agendada para limpeza automática de arquivos antigos no `UPLOAD_FOLDER`.
- [ ] Adicionar middleware de CORS para facilitar integração com front-end externo.

---

## 🔹 Fase 5 — Docker & Deploy
- [ ] Refatorar `docker-compose.yml` para usar `env_file` ao invés de `environment` inline.
- [ ] Fixar tag da imagem base no `Dockerfile` (`python:3.12-slim`).
- [ ] Adicionar `build-essential` e `python3-dev` se pacotes futuros exigirem compilação.
- [ ] Criar imagem pública no DockerHub (opcional).

---

## 🔹 Fase 6 — Documentação e Contribuição
- [ ] Incluir badges no `README.md` (versão, status de build, licença).
- [ ] Adicionar `CONTRIBUTING.md` com boas práticas.
- [ ] Criar `CHANGELOG.md` com histórico das versões.
- [ ] Gerar versão traduzida do `README` em inglês (`README.en.md`).

---

## 📌 Prioridades recomendadas (curto prazo)
✅ Logging estruturado  
✅ Parametrização de beam search  
✅ Testes automatizados mínimos  
✅ Fallbacks robustos para evitar falhas silenciosas