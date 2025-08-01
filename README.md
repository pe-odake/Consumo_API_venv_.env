# 💸 Projeto de Cotação de Moedas com API

Este é um projeto simples de consulta de cotação de moedas, feito como exercício prático para fixação dos conceitos de:

- Ambiente virtual (`venv`)
- Variáveis de ambiente (`.env`)
- Git e `.gitignore`
- Gerenciamento de dependências com `requirements.txt`

---

## 📦 Tecnologias Usadas

- [Python](https://www.python.org/)
- [Requests](https://pypi.org/project/requests/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)
- [ExchangeRate API](https://www.exchangerate-api.com/)

---

## 🚀 Como Rodar o Projeto

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/cotacao_api.git
cd cotacao_api
```

### 2. Crie e ative o ambiente virtual

```bash
# Linux/macOS
python3 -m venv venv_seunome
source venv_seunome/bin/activate

# Windows
python -m venv venv_seunome
venv_seunome\Scripts\activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure sua variável de ambiente

Crie um arquivo `.env` na raiz do projeto com sua chave da ExchangeRate API:

```
API_KEY=sua_chave_aqui
```

Ou use o modelo existente:

```bash
cp .env.example .env
# Depois edite o arquivo com sua chave
```

### 5. Execute o script

```bash
python consulta.py
```

---

## 📁 Estrutura Esperada

```
cotacao_api/
├── consulta.py
├── .env              ← (não enviado ao GitHub)
├── .env.example      ← exemplo de configuração
├── .gitignore
├── requirements.txt
└── venv_seunome/     ← (não enviado ao GitHub)
```

---

## 📄 Exemplo de Arquivos

### .env.example

```env
API_KEY=
```

### .gitignore

```gitignore
.env
venv*/
__pycache__/
```

---

## 📌 Dicas Extras

* Você pode deletar a pasta local e clonar o repositório novamente do GitHub a qualquer momento.
* Após o clone, crie a venv novamente, ative e execute:

```bash
pip install -r requirements.txt
```

* Não se esqueça de recriar o arquivo `.env` com sua chave!

---

## ✅ Entregáveis

* `consulta.py` funcionando com requisição à API.
* `.env.example` com a linha `API_KEY=`.
* `requirements.txt` com as bibliotecas usadas.
* `.gitignore` corretamente configurado.
* `README.md` com todos os passos necessários.


