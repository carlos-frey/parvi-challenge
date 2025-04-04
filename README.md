# Parvi Challenge

Este é um projeto Django desenvolvido como parte do desafio Parvi. Ele utiliza Django REST Framework para criar APIs e inclui integração com variáveis de ambiente usando `python-dotenv`.

---

## Pré-requisitos

Certifique-se de ter os seguintes itens instalados em sua máquina:

- Python 3.13.2 ou superior
- Docker e Docker Compose (opcional, mas recomendado)
- Git

---

## Configuração do Ambiente

1. **Clone o repositório:**

   ```bash
   git clone <URL_DO_REPOSITORIO>
   cd parvi-challenge
   ```

## Defina um arquivo .env para apontar para uma API com informações sobre o overwatch

OVERWATCH_API_ENDPOINT=https://overfast-api.tekrop.fr

## Docker

1. **Execute com docker-compose:**

   ```bash
   docker-compose up --build
   ```
